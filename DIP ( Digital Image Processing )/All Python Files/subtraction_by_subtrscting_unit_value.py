
from PIL import Image, ImageChops
import matplotlib.pyplot as plt

img = Image.open(r"D:\BCA\PROGRAMMING LANGUAGES\PYTHON\DIP ( Digital Image Processing )\Horizontal_flip.jpg").convert("L")

value = 50

img2 = ImageChops.subtract(img, Image.new("L", img.size, value))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(img2, cmap='gray')
plt.title("Subtraction Result")
plt.axis('off')

plt.tight_layout()
plt.show()
