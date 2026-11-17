from PIL import Image
import numpy as np
img = Image.open(r"D:\BCA\PROGRAMMING LANGUAGES\PYTHON\DIP ( Digital Image Processing )\Images\gray_image_5.jpg")

pixels = np.array(img)

print(pixels)