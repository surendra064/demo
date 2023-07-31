import glob
import cv2 as cv
import os
# import pytesseract

fpath = "C:\\Users\\SURENDRA\\Documents\\demoo\\logoss\\**\\*.png"
i=0
def th(file,i):
    dire="C:\\Users\\SURENDRA\\Documents\\demoo\\thersold"
    img=cv.imread(file,cv.IMREAD_GRAYSCALE)
    down_width = 300
    down_height = 200
    down_points = (down_width, down_height)
    img = cv.resize(img, down_points, interpolation= cv.INTER_LINEAR)
    th1=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,12)
    os.chdir(dire)
    text="logo"+str(i)
    filename=str(text)+".jpg"
    print(filename)
    cv.imwrite(filename,th1)
    
    


for file in glob.glob(fpath, recursive=True):
    print(f"Processing {file}")
    img=th(file,i)
    i=i+1