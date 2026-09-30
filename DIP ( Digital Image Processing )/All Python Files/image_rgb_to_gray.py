from PIL import Image
img = Image.open("D:\\DIP\\Images\\rgb_image_1.jpg")
gray_img = img.convert("L")
img.show()
gray_img.show()

gray_img.save("gray_image.jpg")