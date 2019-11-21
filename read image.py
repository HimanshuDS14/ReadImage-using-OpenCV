import cv2

#load color image
image = cv2.imread("lena.jpg" ,1)
#pixels
print(image)
#height  , width , RGB layer
print(image.shape)

#display a image
cv2.imshow("image" , image)


cv2.waitKey(0)
cv2.destroyAllWindows()



