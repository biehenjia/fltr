import cv2, numpy




def test(img: numpy.ndarray):
    gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 1.4)
    edges = cv2.Canny(blur, 50, 150)
    return edges



img = cv2.imread("img.jpg")
scale = 0.09
resized = cv2.resize(img, None, fx=scale,fy=scale, interpolation=cv2.INTER_AREA )
a = test(resized)

cv2.imshow('a',a)
cv2.waitKey(0)
