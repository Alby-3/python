import cv2
image = cv2.imread("81993.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Color Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)

cv2.destroyAllWindows()