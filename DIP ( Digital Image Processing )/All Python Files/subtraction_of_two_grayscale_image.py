
from PIL import Image, ImageChops
import matplotlib.pyplot as plt

img1 = Image.open(r"D:\BCA\PROGRAMMING LANGUAGES\PYTHON\DIP ( Digital Image Processing )\Horizontal_flip.jpg").convert("L")
img2 = Image.open(r"D:\BCA\PROGRAMMING LANGUAGES\PYTHON\DIP ( Digital Image Processing )\Vertical_flip.jpg").convert("L")

img2 = img2.resize(img1.size)

img3 = ImageChops.subtract(img1, img2)

plt.subplot(1, 3, 1)
plt.imshow(img1, cmap='gray')
plt.title("Image 1")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(img2, cmap='gray')
plt.title("Image 2")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(img3, cmap='gray')
plt.title("Subtraction Result")
plt.axis('off')

plt.tight_layout()
plt.show()
