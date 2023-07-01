import cv2 as cv
import pytesseract as pyt

img=cv.imread("images/img.jpeg")
# def resizeframe(frame,scale=0.75):
#     width=int(img.shape[1]*scale)
#     length=int(img.shape[0]*scale)
#     dimension=(width,length)
#     return cv.resize(frame,dimension)
# resizdd=resizeframe(img,0.5)


# cv.destroyAllWindows()
resizdd=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("inoice",resizdd)
cv.waitKey(1)
text=pyt.image_to_string(img)
print(text)