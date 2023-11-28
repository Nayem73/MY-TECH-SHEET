import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from numpy import cos, sin, pi

def on_key(event):
    if event.key == 'left':
        rotate_circle(45)

def rotate_circle(angle):
    global circle, large_circle
    large_center = large_circle.center
    small_center = circle.center

    angle_rad = angle * (pi / 180.0)  
    delta_x = small_center[0] - large_center[0]
    delta_y = small_center[1] - large_center[1]
    new_x = large_center[0] + (delta_x * cos(angle_rad) - delta_y * sin(angle_rad))
    new_y = large_center[1] + (delta_x * sin(angle_rad) + delta_y * cos(angle_rad))

    circle.set_center((new_x, new_y))
    plt.draw()

fig, ax = plt.subplots()

ax.spines['left'].set_position(('data', -20))
ax.spines['bottom'].set_position(('data', -20))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.plot([-20, 20], [0, 0], color='black')  
plt.plot([0, 0], [-20, 20], color='black') 

large_circle = Circle((0, 0), 10, color='white', alpha=0.5)
ax.add_patch(large_circle)

circle = Circle((9, 0), 2, color='blue', alpha=0.5)
ax.add_patch(circle)

fig.canvas.mpl_connect('key_press_event', on_key)

plt.axis('equal')
plt.title('rotate')
plt.show()
