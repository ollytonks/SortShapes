import numpy as np
import matplotlib.pyplot as plt
import cv2
import math 
import sys

def paramInit():
    """ Creates trackbar objects to alter parameters for image breakdown
    """
    cv2.namedWindow("Parameters")
    cv2.resizeWindow("Parameters",640,240)
    cv2.createTrackbar("Max Thresh","Parameters",255,255,np.empty)
    cv2.createTrackbar("Min Thresh","Parameters",188,255,np.empty)
    cv2.createTrackbar("Scale Percent","Parameters",75,200,np.empty)
    cv2.createTrackbar("Area","Parameters",5000,30000,np.empty)

def stackImages(images, percent=25):
    """ Take a 2D array of images, stack each row into a single image and 
        then stack that vertically using matrix concatenation
    """
    rows = len(images)
    cols = len(images[0])
    rowScale = percent/(rows)
    stackedRows = []
    # For each array row, create the stacked row, rescale it and append it to 
    # the arrays to be stacked vertically
    for row in images:
        stackedRow = rescaleFrame(stackHorizontal(row, cols), rowScale)
        stackedRows.append(stackedRow)

    # Combine vertically
    return cv2.vconcat(stackedRows)
        

def stackHorizontal(images, n):
    """ Breakdown image stacking into horizontal image tiles and return a
        stacked row
    """
    length = len(images)

    # CV image matrix must have same shape to match, convert grey images to
    # colour to match matrix dimensions, need three colour channels
    for i in range(length):
        if len(images[i].shape) == 2:
            images[i] = cv2.cvtColor(images[i], cv2.COLOR_GRAY2BGR)
    
    # If have a maximum row size that's bigger than available images, append
    # blanks
    for i in range(length,n):
        blank = np.zeros(images[0].shape, np.uint8)
        images.append(blank)
    
    # Stack images using horizontal matrix concatenation
    return cv2.hconcat(images)
                

def rescaleFrame(frame, percent):
    """Take an image and resize it according to a percentage
    """

    # Get dims
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)

    # resize with opencv
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

def getContours(image, contourImage):
    """ Take an image to analyse and a copy of that image to draw shapes on.
        OpenCV contours looks at the intensity and colour of pixels and finds
        continous lines. This works best on binary images
    """

    # OpenCV implements contour detection, utilising chain approximation to show
    # complete outline
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Another way to minimise noise is making a minimum area for shapes to be
    minArea = cv2.getTrackbarPos("Area", "Parameters")
    for contour in contours:

        # Find area using Green Formula, implements some high level 
        # multivariable calculus
        area = cv2.contourArea(contour)
        if area >= minArea:
            cv2.drawContours(contourImage, contour, -1, (0,255,0), 7)

            #get perimeter of contour
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
            describeShape(contourImage,approx,area)
                
def describeShape(image, approx, area):
    """ Take an image to draw on, a polygon approximation of a contour and
        area and add text to the image, describing the contour detected.
    """
    shape = shapeCheck(approx)
    x , y , w, h = cv2.boundingRect(approx)
    numVertices = len(approx)
    cv2.rectangle(image, (x , y ), (x + w , y + h ), (255, 255, 0), 5)

    # Commented out below to reduce visual clutter
    '''cv2.putText(image, "Points: " + str(numVertices), (x + w + 20, y + 20), \
        cv2.FONT_HERSHEY_COMPLEX, .7,(0, 255, 0), 2)
    cv2.putText(image, "Area: " + str(int(area)), (x + w + 20, y + 45), \
        cv2.FONT_HERSHEY_COMPLEX, 0.7,(0, 255, 0), 2)'''
    cv2.putText(image, "Shape: " + shape, (x + w + 20, y + 70), \
        cv2.FONT_HERSHEY_COMPLEX, 0.7,(0, 0, 255), 2)


def shapeCheck(contour):
    """ Take a contour, count the number of vertices and categorise the shape
        that the contour makes
    """
    vertices = len(contour)
    if vertices == 3:
        return "Triangle"
    elif vertices == 4:
        return " Quadrilateral"
    elif vertices >= 8 and vertices <= 20:
        return "Circle"
    return "Unidentifiable"

def detect(inputImage=None, live=False, cap=None):
    """ Takes an image or a video capture object and detects shapes within the
        image. Continuously analyses until user quits with 'q' press
    """

    while True:
        # Get the parameters for creating binary image and the matrix size
        # of the kernel for image blurring and dilation
        kernel = (5,5)
        maxThresh = cv2.getTrackbarPos("Max Tresh", "Parameters")
        minThresh = cv2.getTrackbarPos("Min Thresh", "Parameters")
        scalePercent = cv2.getTrackbarPos("Scale Percent", "Parameters")

        # Determine if working with static or live imput
        if live:
            _, image = cap.read() 
        else:
            image = cv2.imread(inputImage)

        # Perform preprocessing on image to make contour detection accurate
        contourImage = image.copy()
        blurImage = cv2.GaussianBlur(image, kernel,1)
        greyImage = cv2.cvtColor(blurImage, cv2.COLOR_BGR2GRAY)

        # Edge image created using canny algorithm, takes greyscale image
        edgeImage = cv2.Canny(greyImage,minThresh,maxThresh)

        # Take the edge image and dilate the lines for visibility
        dilateImage = cv2.dilate(edgeImage, np.ones(kernel), iterations=1)

        # Get the shapes
        getContours(dilateImage, contourImage)
        
        # Stack the shapes into easy to consume output
        output = stackImages([[image,edgeImage],[dilateImage,contourImage]],\
            scalePercent)

        #Display
        cv2.imshow("Image Stack", output)

        # When looking at images, press q to exit
        if cv2.waitKey(1) == ord("q"):
            break

    # Release video capture object
    if live:
        cap.release()

    # Close frame
    cv2.destroyAllWindows()

def main():

    # Get either static input, or if no files to look at, initalise live feed
    argc = len(sys.argv)
    if argc > 1:

        # Can have multiple files input
        for i in range(1,argc):

            # Parameter creation and image detection
            paramInit()
            detect(inputImage=sys.argv[i])
    else:
        # Initialise video capture object and parameters
        cap = cv2.VideoCapture(0)
        paramInit()
        detect(live=True, cap=cap)


if __name__ == "__main__":
    main()