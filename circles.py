import cv2, numpy

def pipeline(path):
    image = cv2.imread(path)
    if image is None:
        raise ValueError("Image not found")

    # shape = (height, width, channels)
    height, width, channels = image.shape

    ratio = width / height
    height = 400
    width = int(ratio * height)

    resized = cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)
    cv2.imshow("resized", resized)

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7,7), 0)
    canny = cv2.Canny(blurred, 100, 200)

    pixel_size = 7
    p_width = width // pixel_size
    p_height = height // pixel_size

    canny_color = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)
    pixels = numpy.zeros((p_width+2,p_height+2))
    for i in range(p_height+2):
        for j in range(p_width+2):
            x = j * pixel_size
            y = i * pixel_size
            cv2.circle(canny_color, (x, y), 2, (0,255,0), -1)

    cv2.imshow("grid", canny_color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

path = "img.jpg"
pipeline(path)