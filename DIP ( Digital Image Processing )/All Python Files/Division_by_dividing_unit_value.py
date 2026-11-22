
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open(r"D:\BCA\PROGRAMMING LANGUAGES\PYTHON\DIP ( Digital Image Processing )\Horizontal_flip.jpg").convert("L")

value = 2

img2 = (np.array(img, dtype=float) / value).astype(np.uint8)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(img2, cmap='gray')
plt.title("Division Result")
plt.axis('off')

plt.tight_layout()
plt.show()
