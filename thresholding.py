import cv2 as cv 
img=cv.imread("G:\learn opencv/DIP.jpg")
cv.imshow("original image", img)
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray scale image", gray_img)
#simple binary thresholding
threshold,threshed_img=cv.threshold(gray_img,127,255,cv.THRESH_BINARY) #threshold is exactly the same value we pass to function 
#maxval is the value assigned to pixels with higher value than threshold 
cv.imshow("threshed image", threshed_img)
cv.waitKey(0)