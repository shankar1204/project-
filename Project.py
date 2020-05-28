import cv2   #importing the cv2 library
import numpy as np

cap = cv2.VideoCapture('twentytwovideo.mp4') #Declaring cap varaible & paramater of video
ret, frame1 = cap.read() #Reading first frame and declaringqq
ret, frame2 = cap.read() #Reading second frame and declaring
if (cap.isOpened() == False):  #using if condtionq
    print("Error opening video stream or file")  #shows such output if the parameter is  declared incorrectly.

while (cap.isOpened()): #using while condition
    diff = cv2.absdiff(frame1, frame2) #declaring a variable difference and using absdiff method
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) #covereting difference into grayscale beacuse we need to find contour
    blur = cv2.GaussianBlur(gray, (9, 9), 0) #using blur method passing the parameters(gray, ksize, sigma)
    _, thresh = cv2.threshold(blur, 90, 255, cv2.THRESH_BINARY) #_= first variable not needed, declaring threshold (blur, th.val, max val, type)
    dilated = cv2.dilate(thresh, None, iterations=5) # dilating to fill the holes for better contours, (th, kurnal, iter)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #findnig contours on dil image
    CLASSES = ["person", "background", "bicycle", "trees", "pottedplant", "motorbike", "car", "bird", "bus",
               "tvmonitor", "plants", "dinigtable", "motorbike", "train", "jeep", "dog", "cat"]

    results = []
    results = len(contours)
    print(results)

    contour = []
    list1 = len(contours)
    print("Total number of visitors are:" )
    if results < 700:
     print(results)


    for contour in contours:  # for loop
        (x, y, w, h) = cv2.boundingRect(contour)  # to save all contours and applying method gives x,y

        if cv2.contourArea(contour) < 700: # area of the contour is less then we continue, grater then draw
            continue   #continuing

        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 125, 255), 3)   #drawing rectangle argu (frame, point, colour, thickness)
        cv2.putText(frame1, "Status: {}".format("Movement"), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, #printing text if movemnet is observed, format method, origin, fontstyle
                    1, (0, 0, 255), 3)  #font scale, colour, thickness
    cv2.putText(frame1, "VisitorCount:" " {}".format(results), (10, 95), cv2.FONT_HERSHEY_SIMPLEX,
                # printing text if movemnet is observed, format method, origin, fontstyle
                1, (0, 0,255 ), 3)  # font scale, colour, thickness
    cv2.putText(frame1, "TotalCount: {}".format(contour), (10, 55), cv2.FONT_HERSHEY_SIMPLEX,
                # printing text if movemnet is observed, format method, origin, fontstyle
                1, (225, 0, 0), 3)  # font scale, colour, thickness



    #cv2.drawContours(frame1, contours, -1, (0, 225, 0), 2)

    if ret == True:
        cv2.imshow('SOLUTION FOR VISITOR FLOW USING COMPUTER VISION',  frame1) #display frame1
        frame1=frame2 #insde frame1 to frame
        ret, frame2 = cap.read() #inside frame2 adding new value

        if cv2.waitKey(25) &  0xFF == ord('q'):  #condition with waitkey 25
         break
    else:
        break
cap.release() #realse all capture
cv2.destroyAllWindows() #and close all windows