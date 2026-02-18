import cv2
import numpy as np


PATH = "img.png"

im = cv2.imread(PATH)



def pipeline(path):
    
    image = cv2.imread(PATH)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (7,7), 0)
    canny =cv2.Canny(blurred_image, 0.05, 0.10)

    c = 0
    for row in canny:
        for col in row:
            c += int(col)
    
    
    print(c)
    cv2.imshow("fart",canny)
    cv2.waitKey(0)

pipeline(PATH)