from PIL import Image
img = Image.open(r"D:\BCA\PROGRAMMING LANGUAGES\PYTHON\DIP ( Digital Image Processing )\Images\rgb_image_1.jpg")
gray_img = img.convert("L")
img.show()
gray_img.show()

gray_img.save("gray_image.jpg")