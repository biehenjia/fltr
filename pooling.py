import cv2, numpy

PATH = "img.jpg" 

B = 100

img = cv2.imread(PATH)

h,w = img.shape[:2]
small = cv2.resize(img, (w//B,h//B), interpolation=cv2.INTER_AREA)
pixelated = cv2.resize(small, (w,h), interpolation=cv2.INTER_NEAREST)
cv2.imwrite("pixelated.png", pixelated)