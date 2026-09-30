from PIL import Image
image = Image.open("D:\DIP\Images\gray_image_4.jpg")

horizontal_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
horizontal_flip.save("Horizontal_flip.jpg")

vertical_flip = image.transpose(Image.FLIP_TOP_BOTTOM)
vertical_flip.save("Vertical_flip.jpg")

image.show()
horizontal_flip.show()
vertical_flip.show()

print("Image Flip Successfully")