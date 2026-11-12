from PIL import Image
img = Image.open("D:\BCA\PROGRAMMING LANGUAGES\PYTHON\DIP ( Digital Image Processing )\Images\gray_image_3.jpg")
print("Total number of pixel of image",img.size)
resize_image = img.resize((200,200))
resize_image.save("resize_image.jpg")
img.show()
resize_image.show()
print("Image Resize Successfully")