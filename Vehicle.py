import cv2
import numpy as np  

# load video file (you can also use webcam by putting 0 instead of 'video.mp4')
cap = cv2.VideoCapture('video.mp4')

# minimum width & height of a vehicle (so that small noise won’t be counted)
min_width_react = 80
min_height_react = 80

# line position where we want to count vehicles
count_line_position = 550

# background subtractor to detect moving objects
# NOTE: if cv2.bgsegm doesn’t work, replace with cv2.createBackgroundSubtractorMOG2()
algo = cv2.bgsegm.createBackgroundSubtractorMOG()

# function to get the center point of a rectangle (vehicle box)
def center_handle(x, y, w, h):
    x1 = int(w/2)
    y1 = int(h/2)
    cx = x + x1
    cy = y + y1
    return cx, cy

detect = []       # list to store detected vehicle centers
offset = 6        # margin of error for line crossing
counter = 0       # total vehicle count

while True:
    ret, frame1 = cap.read()
    if not ret:
        break  # stop if video is finished or frame not read

    # convert frame to grayscale for easier processing
    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    # blur image a little to remove noise
    blur = cv2.GaussianBlur(grey, (3, 3), 5)

    # apply background subtraction (find moving objects)
    img_sub = algo.apply(blur)

    # dilate image (make white regions bigger, helps to detect cars better)
    dilat = cv2.dilate(img_sub, np.ones((5, 5)))

    # create a kernel (shape used for morphology operations)
    kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

    # apply morphology to remove small holes and join broken parts
    dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernal)
    dilatada = cv2.morphologyEx(dilatada, cv2.MORPH_CLOSE, kernal)

    # find contours (shapes of moving objects)
    countersahpe, h = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # draw the counting line
    cv2.line(frame1, (25, count_line_position), (1200, count_line_position), (255, 127, 0), 3)

    # loop through each detected object
    for (i, c) in enumerate(countersahpe):
        (x, y, w, h) = cv2.boundingRect(c)
        validate_counter = (w >= min_width_react) and (h >= min_height_react)

        # skip if object is too small
        if not validate_counter:
            continue

        # draw rectangle around detected vehicle
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # temporary text above vehicle (just for debugging)
        cv2.putText(frame1, "Vehicle Counted : " + str(counter), (x, y - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (248, 131, 121), 5)

        # get the center of the vehicle and mark it
        center = center_handle(x, y, w, h)
        detect.append(center)
        cv2.circle(frame1, center, 4, (0, 0, 255), -1)

        # check if vehicle crosses the counting line
        for (x, y) in detect:
            if y < (count_line_position + offset) and y > (count_line_position - offset):
                counter += 1
                cv2.line(frame1, (25, count_line_position), (1200, count_line_position), (0, 127, 255), 3)
                detect.remove((x, y))  # remove once counted
                print("Vehicle Counted : " + str(counter))

        # show vehicle counter on top of video
        cv2.putText(frame1, "Vehicle Counted : " + str(counter), (450, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (159, 69, 118), 5)

    # show the video output with detection
    cv2.imshow('video Original', frame1)

    # press Enter (key code 13) to exit
    if cv2.waitKey(1) == 13:
        break

# cleanup
cv2.destroyAllWindows()
cap.release()
