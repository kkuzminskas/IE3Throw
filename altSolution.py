import cv2
from matplotlib import pyplot as plt

left = cv2.VideoCapture(0)
right = cv2.VideoCapture(1)

while True:
    if not (left.grab() and right.grab()):
        print("No more frames")
        break

    _, leftFrame = left.retrieve()
    _, rightFrame = right.retrieve()

    #cv2.imshow('left', leftFrame)
    #cv2.imshow('right', rightFrame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    lfn = cv2.cvtColor(leftFrame, cv2.COLOR_BGR2GRAY)
    rfn = cv2.cvtColor(rightFrame, cv2.COLOR_BGR2GRAY)
    
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    stereo.setMinDisparity(4)
    stereo.setNumDisparities(128)
    stereo.setBlockSize(21)
    stereo.setSpeckleRange(16)
    stereo.setSpeckleWindowSize(45)
    disparity = stereo.compute(lfn,rfn)
    DEPTH_VISUALIZATION_SCALE = 2048
    cv2.imshow('depth', disparity / DEPTH_VISUALIZATION_SCALE)

left.release()
right.release()
cv2.destroyAllWindows()