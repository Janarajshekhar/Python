from PIL import Image
import numpy as np
img = Image.open("D:\DIP\Images\gray_image_5.jpg")

pixels = np.array(img)

print(pixels)