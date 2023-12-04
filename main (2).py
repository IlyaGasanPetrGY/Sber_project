import cv2
import numpy as np
import math

img = cv2.imread("test.jpg")

vid_capture = cv2.VideoCapture('test.mp4')

naturalWidth = 300

V = []
VShugar = []

if __name__ == '__main__':
    def nothing(*arg):
        pass

cv2.namedWindow( "result" )
cv2.namedWindow( "settings" )

cv2.createTrackbar('h1', 'settings' , 0, 255, nothing)
cv2.createTrackbar('s1', 'settings', 0, 255, nothing)
cv2.createTrackbar('v1', 'settings', 0, 255, nothing)
cv2.createTrackbar('h2', 'settings', 255, 255, nothing)
cv2.createTrackbar('s2', 'settings', 255, 255, nothing)
cv2.createTrackbar('v2', 'settings', 186, 255, nothing)
cv2.createTrackbar('bloor', 'settings', 6, 10, nothing)
cv2.createTrackbar('param1', 'settings', 50, 200, nothing)
cv2.createTrackbar('param2', 'settings', 8, 100, nothing)
cv2.createTrackbar('paramQ1', 'settings', 1, 10, nothing)
cv2.createTrackbar('width', 'settings', 1, 10, nothing)


while True:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    height, width = img.shape[:2]
    countPixelesMM = naturalWidth/width
    bloor = cv2.getTrackbarPos('bloor', 'settings')
    h1 = cv2.getTrackbarPos('h1', 'settings')
    s1 = cv2.getTrackbarPos('s1', 'settings')
    v1 = cv2.getTrackbarPos('v1', 'settings')
    h2 = cv2.getTrackbarPos('h2', 'settings')
    s2 = cv2.getTrackbarPos('s2', 'settings')
    v2 = cv2.getTrackbarPos('v2', 'settings')
    par1 = cv2.getTrackbarPos('param1', 'settings')
    par2 = cv2.getTrackbarPos('param2', 'settings')
    parq1 = cv2.getTrackbarPos('paramQ1', 'settings')
    width = cv2.getTrackbarPos('width', 'settings')

    if bloor % 2 == 0:
        bloor = bloor + 1
    h_min = np.array((h1, s1, v1), np.uint8)
    h_max = np.array((h2, s2, v2), np.uint8)


    hsv = cv2.GaussianBlur(hsv, (bloor, bloor), 2)
    thresh = cv2.inRange(hsv, h_min, h_max)
    thresh = 255 - thresh
    rows = thresh.shape[0]
    rez = 0
    rez = cv2.imread("test.jpg")


    contours, hierarchy = cv2.findContours( thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_L1)
    thresh = cv2.drawContours( thresh, contours, -1, (0,0,0), 30, cv2.LINE_AA, hierarchy, 1 )
    cv2.imshow('result1', thresh)
    contours, hierarchy = cv2.findContours( thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_L1)
    thresh = cv2.drawContours(thresh, contours, -1, (255,255,255), 15, cv2.LINE_AA, hierarchy, 1 )
    contours, hierarchy = cv2.findContours( thresh.copy(), cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_TC89_L1)
    i = 0

    while (True):
        key = cv2.waitKey(20)
        if (key == ord('q') or key == 27):
            rez = cv2.drawContours(rez, contours, i, (255, 0, 255), width, cv2.LINE_AA, hierarchy, 1)
            (x, y), radius = cv2.minEnclosingCircle(contours[i])
            radius = radius * countPixelesMM
            V.append(math.pi*(2*radius)**3/6)
            VShugar.append((math.pi*(2*(radius+2))**3/6)-(math.pi*(2*radius)**3/6))
            cv2.imshow('result', rez)
            cv2.imshow('result1', thresh)
            print(V[i])
            print(VShugar[i])

            i += 1


    print(len(contours))
    cv2.imshow('result', rez)
    cv2.imshow('result1', thresh)

    ch = cv2.waitKey(5)
    if ch == 27:
        break

