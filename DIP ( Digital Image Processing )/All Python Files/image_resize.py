from PIL import Image
img = Image.open("D:\DIP\Images\gray_image_1.jpg")
print("Total number of pixel of image",img.size)
resize_image = img.resize((200,200))
resize_image.save("resize_image.jpg")
img.show()
resize_image.show()
print("Image Resize Successfully")