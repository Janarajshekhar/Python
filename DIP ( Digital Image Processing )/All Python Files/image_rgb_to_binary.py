from PIL import Image

img = Image.open("D:\\DIP\\Images\\rgb_image_1.jpg")
gray_img = img.convert("L")
threshold = 128

binary_img = gray_img.point(lambda x:255 if x>threshold else 0)

binary_img.show()
binary_img.save("binary_image.jpg")