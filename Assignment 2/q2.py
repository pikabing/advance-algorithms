''' Author: Pratik Gupta
Reg No: 183
10 Aug, 2019 '''      

import cv2
 import numpy as np
import sys

if __name__ == "__main__":
    if(len(sys.argv)) < 2:
        file_path = "sample.jpg"
    else:
        file_path = sys.argv[1]

    # read image
    src = cv2.imread(file_path, 1)
    
    # show source image
    cv2.imshow("Source", src)

    # convert image to gray scale
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
     
    # blur the image
    blur = cv2.blur(gray, (3, 3))
    
    # binary thresholding of the image
    ret, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)
    
    # find contours
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, \
            cv2.CHAIN_APPROX_SIMPLE)
    
    # create hull array for convexHull points
    hull = []
    
    # calculate points for each contour
    for i in range(len(contours)):
        hull.append(cv2.convexHull(contours[i], False))
    
    # create an empty black image
    drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
    
    max_x = []
    min_x = []
    max_y = []
    min_y = []
    for i in hull:
        temp = np.max(i, axis = 0)
        temp2 = np.min(i, axis = 0)
        max_x.append(temp[0][0])
        max_y.append(temp[0][1])
        min_x.append(temp2[0][0])
        min_y.append(temp2[0][1])
    
    count = 0
    for i in range(len(hull)):
        for j in range(len(hull)):
            if(min_y[j] < min_y[i] and max_y[i] < max_y[j] and min_x[j] < min_x[i] and max_x[i] < max_x[j]):
                color_contours = (0, 250, 0)
                color = (255,255,255)
                cv2.drawContours(drawing, hull, i, color, 2, 8)
                count=count+1
                print(min_y[j] ,"<" ,min_y[i], "and", max_y[i] ,"<", max_y[j] ,"and" ,min_x[j], "<", min_x[i], "and", max_x[i] ,"<", max_x[j])
                # del hull[i:i+1]
    print(count)

    # draw contours and hull points
    for i in range(len(contours)):
        color_contours = (0, 255, 0) # color for contours
        color = (255, 255, 255) # color for convex hull
        # draw contours
        # cv2.drawContours(drawing, contours, i, color_contours, 2, 8, hierarchy)
        # draw convex hull
        # cv2.drawContours(drawing, hull, i, color, 2, 8)
    
    # max_x contains maximum x co-rodinate of each hull 
    # for i in range(len(hull)):
    #     color_contours = (0, 250, 0)
    #     color = (255,255,255)
    #     cv2.drawContours(drawing, hull, i, color, 2, 8)
    cv2.imshow("Output", drawing)

    cv2.waitKey(0)
    cv2.destroyAllWindows()