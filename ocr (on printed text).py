# First download the tesseract engine from https://github.com/UB-Mannheim/tesseract/wiki (for Windows)
# or from https://tesseract-ocr.github.io/tessdoc/ (for other OS)

# Install the .exe file (the one you just downloaded), and don't change the default path of the file while installing
# If everything is set to default, the Tesseract Engine will be installed in 'C:\Program Files\Tesseract-OCR'


import cv2 as cv
import pytesseract

# if everything goes normally and you don't mess up anything, then there'll be a file tesseract.exe in the default path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

lsa = cv.imread('lsa.jpg')  # reading image
lsa = cv.resize(lsa, (int(lsa.shape[1]*0.4), int(lsa.shape[0]*0.4)), interpolation=cv.INTER_AREA) #rescaling image
bw_lsa = cv.cvtColor(lsa, cv.COLOR_BGR2GRAY)  # converting the image to black and white

#thresh = cv.adaptiveThreshold(bw_lsa, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
# I tried adaptiveThreshold but it performed worse

config = '--psm 3'  # default configuration
# pagesegmode values are :
# 0 : Orientation and Script Detection (OSD) only
# 1 : Automatic page segmentation with OSD
# 2 : Automatic page segmentation, but no OSD, or OCR
# 3 : Fully automatic page segmentation, but no OSD (default)
# 4 : Assume a single column of text of variable sizes.
# 5 : Assume a single uniform block of vertically aligned text
# 6 : Assume a single uniform block of text
# 7 : Treat the image as single text line
# 8 : Treat the image as a single word
# 9 : Treat the image as a single word in a circle
# 10: Treat the image as single character


text = pytesseract.image_to_string(bw_lsa, config=config, lang='eng')
print(text)

cv.imshow("LSA notes", bw_lsa)
cv.waitKey(0)
cv.destroyAllWindows()