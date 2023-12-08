import cv2
image = cv2.imread("solar-system.jpg")

cv2.putText(image,"sun",(20,200),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1.5,color=(0,0,0))
cv2.putText(image,"mercury",(120,180),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(255,255,255))
cv2.imshow("card",image)
cv2.waitKey(2000)