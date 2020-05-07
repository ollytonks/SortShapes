import numpy as np
import matplotlib.pyplot as plt
import cv2
import math 
import sys

# Create VideoCapture object to look through camera '0' (default)

cap = cv2.VideoCapture(0)

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,240)
cv2.createTrackbar("Max Thresh","Parameters",255,255,np.empty)
cv2.createTrackbar("Min Thresh","Parameters",125,255,np.empty)
cv2.createTrackbar("Scale Percent","Parameters",50,200,np.empty)
cv2.createTrackbar("Area","Parameters",5000,30000,np.empty)

def stackImages(images, percent=25):
    rows = len(images)
    cols = len(images[0])
    rowScale = percent/(rows)
    stackedRows = []
    for row in images:
        stackedRow = rescaleFrame(stackHorizontal(row, cols), rowScale)
        stackedRows.append(stackedRow)

    return cv2.vconcat(stackedRows)
        

def stackHorizontal(images, n):
    length = len(images)
    for i in range(length):
        if len(images[i].shape) == 2:
            images[i] = cv2.cvtColor(images[i], cv2.COLOR_GRAY2BGR)
    
    for i in range(length,n):
        blank = np.zeros(images[0].shape, np.uint8)
        images.append(blank)
    return cv2.hconcat(images)
                

def rescaleFrame(frame, percent):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

def getContours(image, contourImage):
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    minArea = cv2.getTrackbarPos("Area", "Parameters")
    for contour in contours:
        area = cv2.contourArea(contour)
        if area >= minArea:
            cv2.drawContours(contourImage, contour, -1, (0,255,0), 7)

            #get perimeter of contour
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
            shape = shapeCheck(approx)
            x , y , w, h = cv2.boundingRect(approx)
            cv2.rectangle(contourImage, (x , y ), (x + w , y + h ), (255, 255, 0), 5)

            cv2.putText(contourImage, "Points: " + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, .7,
                        (0, 255, 0), 2)
            cv2.putText(contourImage, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 255, 0), 2)
            cv2.putText(contourImage, "Shape: " + shape, (x + w + 20, y + 70), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 0, 255), 2)
            cv2.putText(contourImage, "Num Vertices: " + str(len(approx)), (x + w + 20, y + 95), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 0, 255), 2)
                

def shapeCheck(contour):
    vertices = len(contour)
    if vertices == 3:
        return "Triangle"
    elif vertices == 4:
        return " Quadrilateral"
    elif vertices >= 8 and vertices <= 20:
        return "Circle"
    return "Unidentifiable"

while True:

    kernel = (5,5)
    maxThresh = cv2.getTrackbarPos("Max Tresh", "Parameters")
    minThresh = cv2.getTrackbarPos("Min Thresh", "Parameters")
    scalePercent = cv2.getTrackbarPos("Scale Percent", "Parameters")

    _, image = cap.read() 
    contourImage = image.copy()
    blurImage = cv2.GaussianBlur(image, kernel,1)
    greyImage = cv2.cvtColor(blurImage, cv2.COLOR_BGR2GRAY)
    edgeImage = cv2.Canny(greyImage,minThresh,maxThresh)

    # take edge image and dilate it to make it more visible
    dilateImage = cv2.dilate(edgeImage, np.ones(kernel), iterations=1)
    getContours(dilateImage, contourImage)
    
    output = stackImages([[image,edgeImage],[dilateImage,contourImage]], scalePercent)

    cv2.imshow("Image Stack", output)

    # When looking at images, press q to exit
    if cv2.waitKey(1) == ord("q"):
        break

# Release video capture object
cap.release()
cv2.destroyAllWindows()