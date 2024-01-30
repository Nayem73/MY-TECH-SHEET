# Introduction

1. Remote sensing is a powerful technology that captures information about the Earth’s surface from a distance. For example, using satellite, Aircrafts, drones or any other medium that can capture Earth Data in a large quantity.

# Objectives

1. For this research, we have quite a few objectives. First of all, our objective is to ..
2. Train with low number of epochs

# Literature Review

1. From this paper, I learnt how deep learning models can do extremely well in terms of large scale remote sensing image data.

[The paper you mentioned](https://sci-hub.se/10.1109/ACCESS.2021.3051085)[1](https://sci-hub.se/10.1109/ACCESS.2021.3051085) proposes a novel method for classifying remote sensing images using a deep convolutional neural network (CNN) model with attention mechanism. The paper does the following:

- It introduces a new dataset, named RSI-ATT, which contains 10,000 images of size 224 × 224 pixels covering 10 classes of land use and land cover types. [The dataset is derived from the EuroSAT dataset](https://sci-hub.se/10.1109/ACCESS.2021.3051085)[2](https://www.researchgate.net/profile/Haikel-Alhichri/publication/271913544_Clustering_of_Hyperspectral_Images_with_an_Ensemble_Method_Based_on_Fuzzy_C-Means_and_Markov_Random_Fields/links/6134ee6ec69a4e48797d9790/Clustering-of-Hyperspectral-Images-with-an-Ensemble-Method-Based-on-Fuzzy-C-Means-and-Markov-Random-Fields.pdf) by applying different image processing techniques such as contrast enhancement, histogram equalization, and gamma correction.
- [It adopts the EfficientNet-B3 CNN model](https://orcid.org/0000-0003-2164-043X)[3](https://orcid.org/0000-0003-2164-043X), which is a state-of-the-art model for image classification that can achieve high accuracy with fewer parameters and computational cost. The model consists of several blocks of inverted residual bottleneck layers with squeeze-and-excitation modules and skip connections.
- It incorporates an attention mechanism into the EfficientNet-B3 model to enhance its performance on remote sensing images. The attention mechanism consists of two components: a spatial attention module and a channel attention module. The spatial attention module learns to focus on the most informative regions of the image, while the channel attention module learns to emphasize the most relevant spectral bands of the image.
- It evaluates the proposed method on the RSI-ATT dataset and compares it with several baseline methods, such as ResNet-50, DenseNet-121, and Inception-v3. The paper shows that the proposed method achieves the highest accuracy of 99.21% on the RSI-ATT dataset and outperforms the baseline methods by a large margin.

The paper contributes to the field of remote sensing image classification by proposing a novel method that can effectively exploit the spatial and spectral information of the images using a deep CNN model with attention mechanism. The paper also provides a new dataset that can be used for further research and development of remote sensing image classification methods.

[](https://sci-hub.se/10.1109/ACCESS.2021.3051085)[1](https://sci-hub.se/10.1109/ACCESS.2021.3051085): Alhichri H, Alswayed AS, Bazi Y, Ammour N, Alajlan NA. Classification of remote sensing images using EfficientNet-B3 CNN model with attention. IEEE access. [2021 Jan 12;9:14078-94.](https://sci-hub.se/10.1109/ACCESS.2021.3051085) [2](https://www.researchgate.net/profile/Haikel-Alhichri/publication/271913544_Clustering_of_Hyperspectral_Images_with_an_Ensemble_Method_Based_on_Fuzzy_C-Means_and_Markov_Random_Fields/links/6134ee6ec69a4e48797d9790/Clustering-of-Hyperspectral-Images-with-an-Ensemble-Method-Based-on-Fuzzy-C-Means-and-Markov-Random-Fields.pdf): Helber, P., Bischke, B., Dengel, A., & Borth, D. (2019). Eurosat: A novel dataset and deep learning benchmark for land use and land cover classification. [IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 12(7), 2217-2226.](https://orcid.org/0000-0003-2164-043X) [3](https://orcid.org/0000-0003-2164-043X): Tan, M., & Le, Q. V. (2019). Efficientnet: Rethinking model scaling for convolutional neural networks. In International Conference on Machine Learning (pp. 6105-6114). PMLR.

2. # Methodology
- k = 2, which is akin to a 50% reduction in image dimension,

# Result

- k = 2 = almost 50%, even in thisc case, the accuracy is still basically the same!

- Even if we completely half the image to a size of 64x64, all the way from 128x128, we can see that, our model's accuracy is still close to 90%. Not only that, in this case, the train accuracy and test accuracy is even closer, with only a 2% difference, means that after training with half the resolution of original images, our model performs really well with unseen remote sensing images.

# Question

- swapping the models. Will there be differences?

Swapping the order of the models (i.e., using ResNet50 as `base_model1` and EfficientNetB0 as `base_model2`) would not fundamentally change the architecture of your hybrid model. The models are still being used to extract features from the input, and these features are still being concatenated together to form the input for the subsequent layers.

However, the order of concatenation will change, meaning the order in which the features extracted by ResNet50 and EfficientNetB0 are combined will be different. This could potentially lead to slight differences in performance due to the way these features interact in the subsequent layers of the model.

Also, the layers you’re fine-tuning will change. In your original code, you’re fine-tuning the last 50 layers of EfficientNetB0 and the last 20 layers of ResNet50. If you swap the models, you’ll be fine-tuning the last 50 layers of ResNet50 and the last 20 layers of EfficientNetB0. Since these models have different architectures, the specific layers you’re fine-tuning will be different, which could also impact the model’s performance.

In summary, while the high-level architecture of your model remains the same, the specific features it learns and the way it learns them might vary, which could lead to differences in performance. It’s hard to say without experimenting whether this change would improve or degrade the performance of your model. It’s always a good idea to try different configurations and see what works best for your specific task. 😊

- what does this number mean in support? (classification_report)

----

[According to the paper that introduced the EfficientNet family of models](https://keras.io/api/applications/efficientnet/)[1](https://keras.io/api/applications/efficientnet/), the most efficient and lightweight version is EfficientNet-B0, which has the lowest number of parameters (5.3 million) and the lowest computational cost (0.39 billion FLOPS) among the variants. The paper also shows that EfficientNet-B0 achieves state-of-the-art accuracy on various image classification benchmarks, such as ImageNet, CIFAR-100, and Stanford Cars.

[](https://keras.io/api/applications/efficientnet/)[1](https://keras.io/api/applications/efficientnet/): Tan, M., & Le, Q. V. (2019). Efficientnet: Rethinking model scaling for convolutional neural networks. In International Conference on Machine Learning (pp. 6105-6114). PMLR.

----
