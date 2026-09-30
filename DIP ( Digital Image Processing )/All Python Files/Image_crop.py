import cv2
image = cv2.imread("D:\DIP\Images\gray_image_3.jpg")
if image is None :
    print("Error Image Not Found !")
    exit()
cropped = image[100:400, 150:450]
cv2.imshow("Original Image",image)
cv2.imshow("Cropped image",cropped)
cv2.imwrite("Cropped_image.jpg",cropped)
cv2.waitKey(0)