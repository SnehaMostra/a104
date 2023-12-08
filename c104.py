import cv2
image = cv2.imread("poster.jpg")
msg="lets go to the moon"
cv2.putText(image,msg,(20,200),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1.5,color=(3,9,255))
rocket= image[120:360,400:500]
image[0:240,500:600]= rocket
cv2.imshow("card",image)
cv2.waitKey(0)