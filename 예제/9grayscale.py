import cv2

src = cv2.imread("res/1.jpg", cv2.IMREAD_COLOR)

dst = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
