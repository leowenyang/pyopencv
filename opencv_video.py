# -*- coding: utf-8 -*-
import cv2
import numpy as np

def videoCapture():
    cap = cv2.VideoCapture(0)
    # set capture value
    #  0 : cv2.cv.CV_CAP_PROP_POS_MSEC
    #  1 : cv2.cv.CV_CAP_PROP_POS_FRAMES
    #  2 : cv2.cv.CV_CAP_PROP_POS_AVI_RATIO
    #  3 : cv2.cv.CV_CAP_PROP_FRAME_WIDTH
    #  4 : cv2.cv.CV_CAP_PROP_FRAM_HEIGHT
    #  5 : cv2.cv.CV_CAP_PROP_FPS
    #  6 : cv2.cv.CV_CAP_PROP_FOURCC
    #  7 : cv2.cv.CV_CAP_PROP_FRAME_COUNT 
    #  8 : cv2.cv.CV_CAP_PROP_FORMAT 
    #  9 : cv2.cv.CV_CAP_PROP_MODE 
    #  10 : cv2.cv.CV_CAP_PROP_BRIGHTNESS 
    #  11 : cv2.cv.CV_CAP_PROP_CONTRAST 
    #  12 : cv2.cv.CV_CAP_PROP_SATURATION
    #  13 : cv2.cv.CV_CAP_PROP_HUE 
    #  14 : cv2.cv.CV_CAP_PROP_GAIN 
    #  15 : cv2.cv.CV_CAP_PROP_EXPOSURE
    #  16 : cv2.cv.CV_CAP_PROP_CONVERT_RGB
    #  17 : cv2.cv.CV_CAP_PROP_WHITE_BALANCE 
    #  18 : cv2.cv.CV_CAP_PROP_RECTIFICATION
    print cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
    print cap.get(4)
    cap.set(3, 800)
    cap.set(4, 600)

    while True:
        # capture frame by frame
        ret, frame = cap.read()

        print cap.get(6)

        # operation cap
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def capture2File():
    cap = cv2.VideoCapture(0)
    #fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fourcc = cv2.cv.CV_FOURCC("X", "V", "I", "D")
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.flip(frame, 0)

            out.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

def playVideoFile():
    cap = cv2.VideoCapture('output.avi')

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    #videoCapture()
    #capture2File()
    playVideoFile()

if __name__ == '__main__':
    main()