```python
!pip install -q kaggle
!mkdir ~/.kaggle

from google.colab import drive
drive.mount('/content/drive')

! cp "/content/drive/MyDrive/Colab Notebooks/Thesis/kaggle.json"  ~/.kaggle

! kaggle datasets download -d apollo2506/eurosat-dataset

! cp "/content/eurosat-dataset.zip" "/content/drive/MyDrive/Colab Notebooks/Thesis"

! unzip -q "/content/drive/MyDrive/Colab Notebooks/Thesis/eurosat-dataset.zip"

datasets_dir = "/content/EuroSAT"

IMG_SIZE = 128
BATCH_SIZE = 32
epochs = 30

import tensorflow as tf
tf.random.set_seed(42)

train_data = tf.keras.preprocessing.image_dataset_from_directory(
    directory = datasets_dir,
    image_size = (IMG_SIZE, IMG_SIZE),
    label_mode = 'categorical',
    color_mode="rgb",
    batch_size = BATCH_SIZE,
    seed=42,
    shuffle = True,
    validation_split=0.2,
    subset="training"

).cache().shuffle(1000).prefetch(buffer_size=tf.data.AUTOTUNE)


test_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    directory = datasets_dir,
    image_size =  (IMG_SIZE, IMG_SIZE),
    label_mode = 'categorical',
    color_mode="rgb",
    batch_size = BATCH_SIZE,
    seed=42,
    shuffle = True,
    validation_split=0.2,
    subset="validation"

)
class_names = test_dataset.class_names
test_data = test_dataset.cache().shuffle(1000).prefetch(buffer_size=tf.data.AUTOTUNE)
class_names

import tensorflow as tf

data_augmentation = tf.keras.Sequential([
  tf.keras.layers.experimental.preprocessing.RandomFlip("horizontal",input_shape=(IMG_SIZE, IMG_SIZE, 3)),
  tf.keras.layers.experimental.preprocessing.RandomRotation(0.2),
  tf.keras.layers.experimental.preprocessing.RandomZoom(0.2),
  tf.keras.layers.experimental.preprocessing.RandomHeight(0.2),
  tf.keras.layers.experimental.preprocessing.RandomWidth(0.2)
], name ="data_augmentation")

import matplotlib.pyplot as plt
import numpy as np

"""
ploting image
"""

plt.figure(figsize=(10,10))
"""
Take only one batch
Each batch size is now 32
so Every batch has 32 images
"""
for image_batch,label_batch in train_data.take(1):
    """Ploting only 8 pictures of them"""
    for i in range(0,12):
        """Subploting them 3 rows and 4 columns"""
        plt.subplot(3,4,i+1)
        """Image data 0-255"""
        plt.imshow(image_batch[i].numpy().astype("uint32"))
        plt.title(class_names[np.argmax(label_batch[i])])
        plt.axis("off")



plt.figure(figsize=(10,10))
for image_batch,label_batch in train_data.take(1):
    augmented_image_batch = data_augmentation(image_batch)
    image_plt_len = len(image_batch) if len(image_batch) < 4 else 4
    for i in range(0, image_plt_len):
        plt.subplot(image_plt_len,2,2*i+1)
        plt.imshow(image_batch[i].numpy().astype("uint32"))
        plt.title(class_names[np.argmax(label_batch[i])])
        plt.axis("off")
        plt.subplot(image_plt_len,2,2*i+2)
        img = augmented_image_batch[i]
        img = np.array(img, dtype=np.int32)
        plt.imshow(img)
        plt.title(f"augmented")
        plt.axis("off")



gdrive_path = "/content/drive/MyDrive/Colab Notebooks/Thesis"

checkpoint_path =f"{gdrive_path}/CheckPoint/cp.ckpt"
checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    checkpoint_path,
    monitor='val_accuracy',
    save_best_only=True
)

import tensorflow as tf

# Setup the base model and freeze its layers (this will extract features)
base_model = tf.keras.applications.EfficientNetB0(include_top=False)
base_model.trainable= False

#Setup model architecture with trainable top layers
inputs = tf.keras.layers.Input(shape=(IMG_SIZE,IMG_SIZE,3), name='input_layer')
x = data_augmentation(inputs)
x = base_model(x, training=False)
x = tf.keras.layers.GlobalAveragePooling2D(name='global_avg_pooling_layer')(x)
outputs = tf.keras.layers.Dense(len(class_names), activation='softmax', name='output_layer')(x)
model = tf.keras.Model(inputs, outputs)

tf.keras.utils.plot_model(
    model,
    to_file='model.png',
    # show_shapes=True,
    # show_dtype=False,
    # show_layer_names=True,
    # rankdir='TB',
    # expand_nested=False,
    dpi=96,
    # layer_range=None,
    # show_layer_activations=False,
    # show_trainable=False
)

model.compile(
    loss = 'categorical_crossentropy',
    optimizer = tf.keras.optimizers.Adam(),
    metrics = ['accuracy']
)

history = model.fit(
    train_data,
    epochs=epochs,
    steps_per_epoch=len(train_data),
    validation_data = test_data,
    validation_steps = len(test_data),
    callbacks = [
        checkpoint_callback
    ]
)

def plot_loss_curves(history):
  loss = history.history['loss']
  val_loss = history.history['val_loss']

  accuracy = history.history['accuracy']
  val_accuracy = history.history['val_accuracy']

  epochs = range(len(history.history['loss']))

  plt.figure(figsize=(12,6))
  # Plot loss
  plt.subplot(1,2,1)
  plt.plot(epochs, loss, label='training_loss')
  plt.plot(epochs, val_loss, label='val_loss')
  plt.title('Loss')
  plt.xlabel('Epochs')
  plt.legend()

  # Plot accuracy
  plt.subplot(1,2,2)
  plt.plot(epochs, accuracy, label='training_accuracy')
  plt.plot(epochs, val_accuracy, label='val_accuracy')
  plt.title('Accuracy')
  plt.xlabel('Epochs')
  plt.legend()

  plot_loss_curves(history)

  model.evaluate(train_data), model.evaluate(test_data)

  import itertools
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix

# Our function needs a different name to sklearn's plot_confusion_matrix
def make_confusion_matrix(y_true, y_pred, classes=None, figsize=(10, 10), text_size=15, norm=False):

  # Create the confustion matrix
  cm = confusion_matrix(y_true, y_pred)
  cm_norm = cm.astype("float") / cm.sum(axis=1)[:, np.newaxis] # normalize it
  n_classes = cm.shape[0] # find the number of classes we're dealing with
  # Plot the figure and make it pretty
  fig, ax = plt.subplots(figsize=figsize)
  cax = ax.matshow(cm, cmap=plt.cm.Blues) # colors will represent how 'correct' a class is, darker == better
  fig.colorbar(cax)

  # Are there a list of classes?
  if classes:
    labels = classes
  else:
    labels = np.arange(cm.shape[0])

  # Label the axes
  ax.set(title="Confusion Matrix",
         xlabel="Predicted label",
         ylabel="True label",
         xticks=np.arange(n_classes), # create enough axis slots for each class
         yticks=np.arange(n_classes),
         xticklabels=labels, # axes will labeled with class names (if they exist) or ints
         yticklabels=labels,
         )

  # Make x-axis labels appear on bottom
  ax.tick_params(axis='x', labelrotation=90)
  ax.xaxis.set_label_position("bottom")
  ax.xaxis.tick_bottom()

  # Set the threshold for different colors
  threshold = (cm.max() + cm.min()) / 2.

  # Plot the text on each cell
  for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
    if norm:
      plt.text(j, i, f"{cm[i, j]} ({cm_norm[i, j]*100:.1f}%)",
              horizontalalignment="center",
              color="white" if cm[i, j] > threshold else "black",
              size=text_size)
    else:
      plt.text(j, i, f"{cm[i, j]}",
              horizontalalignment="center",
              color="white" if cm[i, j] > threshold else "black",
              size=text_size)



y_true = np.array([])
y_pred = np.array([])
for x, y in test_data:
    y_true = np.concatenate([y_true, np.argmax(y, axis=-1)], axis=0)
    y_pred = np.concatenate([y_pred, np.argmax(model.predict(x), axis=-1)], axis=0)


make_confusion_matrix(y_true, y_pred, class_names)



import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12,12))
for image_batch,label_batch in test_data.take(1):
    predictions = model.predict(image_batch)
    predictions = np.argmax(predictions, axis=-1)
    for i in range(0,len(predictions) if len(predictions)<12 else 12):
        plt.subplot(3,4,i+1)
        plt.imshow(image_batch[i].numpy().astype("uint32"))
        true_class = class_names[np.argmax(label_batch[i])]
        predict_class = class_names[predictions[i]]
        title = f"""True: {true_class}\n Predict: {predict_class}"""
        plt.title(title, color='g' if true_class==predict_class else 'r')
        plt.axis("off")
```

This code performs several tasks related to working with a machine learning model for image classification using the EuroSAT dataset. Let's break it down step by step:

1. **Kaggle Setup:**
   
   - Installs the Kaggle library using `!pip install -q kaggle`.
   - Creates a directory `~/.kaggle` to store Kaggle API key.

2. **Google Drive Setup:**
   
   - Mounts Google Drive using Google Colab's `drive.mount('/content/drive')`.
   - Copies the Kaggle API key (`kaggle.json`) from Google Drive to the Kaggle directory.

3. **Dataset Download and Extraction:**
   
   - Downloads the EuroSAT dataset from Kaggle using the Kaggle API.
   - Copies the downloaded ZIP file to a specified directory in Google Drive.
   - Extracts the dataset using `unzip`.

4. **Data Preparation:**
   
   - Sets up variables for image size, batch size, and number of epochs.
   - Imports TensorFlow and sets a random seed.
   - Loads the training and validation datasets using `tf.keras.preprocessing.image_dataset_from_directory`.
   - Defines data augmentation techniques using TensorFlow's Sequential API.

5. **Data Visualization:**
   
   - Plots a batch of original images from the training dataset.
   - Plots a batch of augmented images to visualize the effects of data augmentation.

6. **Model Setup:**
   
   - Defines the file path for model checkpoints.
   - Sets up callbacks for model training, specifically for saving the best model based on validation accuracy.
   - Imports TensorFlow and loads a pre-trained EfficientNetB0 model, freezing its layers.
   - Creates a new model architecture by adding a global average pooling layer and a dense output layer with softmax activation.

7. **Model Compilation and Training:**
   
   - Compiles the model with categorical crossentropy loss, Adam optimizer, and accuracy metric.
   - Trains the model on the prepared datasets, using the specified number of epochs and the previously defined callbacks.

8. **Training History Visualization:**
   
   - Defines a function (`plot_loss_curves`) to plot the training and validation loss/accuracy curves.
   - Calls the function to visualize the training history.

9. **Model Evaluation:**
   
   - Evaluates the model on both the training and test datasets.

10. **Confusion Matrix:**
    
    - Defines a function (`make_confusion_matrix`) to create and visualize a confusion matrix.
    - Calculates and visualizes the confusion matrix for the test dataset.

11. **Image Batch Prediction:**
    
    - Plots a batch of images from the test dataset along with their true and predicted classes.

In summary, this code sets up the environment, downloads and preprocesses the EuroSAT dataset, defines a deep learning model, trains the model, and evaluates its performance through various visualizations and metrics.

##### for above code, in your explanation, I don't understand point 4: Data preparation. Go through every line of code of point 4 and explain intensively.

Certainly! Let's break down point 4 (Data Preparation) step by step:

pythonCopy code

`datasets_dir = "/content/EuroSAT"`

This line defines the directory where the EuroSAT dataset will be extracted.

pythonCopy code

`IMG_SIZE = 128 BATCH_SIZE = 32 epochs = 30`

These lines define constants for image size (`IMG_SIZE`), batch size (`BATCH_SIZE`), and the number of training epochs (`epochs`).

pythonCopy code

`import tensorflow as tf tf.random.set_seed(42)`

Imports the TensorFlow library and sets a random seed for reproducibility.

pythonCopy code

`train_data = tf.keras.preprocessing.image_dataset_from_directory(     directory=datasets_dir,     image_size=(IMG_SIZE, IMG_SIZE),     label_mode='categorical',     color_mode="rgb",     batch_size=BATCH_SIZE,     seed=42,     shuffle=True,     validation_split=0.2,     subset="training" ).cache().shuffle(1000).prefetch(buffer_size=tf.data.AUTOTUNE)`

Uses the `image_dataset_from_directory` function to create a training dataset. It loads images from the specified directory, resizes them to the defined `IMG_SIZE`, converts labels to categorical format, and sets other parameters like color mode, batch size, and shuffling. The dataset is then cached, shuffled, and prefetched for better performance during training.

pythonCopy code

`test_dataset = tf.keras.preprocessing.image_dataset_from_directory(     directory=datasets_dir,     image_size=(IMG_SIZE, IMG_SIZE),     label_mode='categorical',     color_mode="rgb",     batch_size=BATCH_SIZE,     seed=42,     shuffle=True,     validation_split=0.2,     subset="validation" )`

Similar to the training dataset, this code creates a validation/test dataset using a subset of the EuroSAT dataset.

pythonCopy code

`class_names = test_dataset.class_names`

Gets the class names from the test dataset.

pythonCopy code

`test_data = test_dataset.cache().shuffle(1000).prefetch(buffer_size=tf.data.AUTOTUNE)`

Caches, shuffles, and prefetches the test dataset for better performance during evaluation.

In summary, this part of the code prepares the training and test datasets for the image classification task. It sets up parameters, loads the data, and applies preprocessing steps using TensorFlow's utility functions.
