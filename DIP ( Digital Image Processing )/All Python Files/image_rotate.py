from PIL import Image
img = Image.open("D:\DIP\Images\gray_image_3.jpg")
rotated = img.rotate(45)
rotated.save("rotated.jpg")
rotated.show()
print("Image rotated successfully")