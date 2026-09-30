from PIL import Image
img = Image.open("D:\DIP\Images\gray_image_1.jpg")
width,height = img.size
total_pixel = width * height
print("Width",width)
print("Height",height)
print("Total number of pixels",total_pixel)