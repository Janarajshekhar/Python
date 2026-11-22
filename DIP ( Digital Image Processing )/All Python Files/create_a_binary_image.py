
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open(r"D:\BCA\PROGRAMMING LANGUAGES\PYTHON\DIP ( Digital Image Processing )\Horizontal_flip.jpg").convert("L")

threshold = 128

binary_img = img.point(lambda x: 255 if x > threshold else 0)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Grayscale Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(binary_img, cmap='gray')
plt.title("Binary Image")
plt.axis('off')

plt.tight_layout()
plt.show()

binary_img.save("binary_image.jpg")
