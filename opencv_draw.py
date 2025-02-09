# -*- coding: utf-8 -*-
import cv2
import numpy as np

def drawLine():
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def drawRect():
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.rectangle(img, (384, 8), (510, 128), (0, 255, 0), 3)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def drawCircle():
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.circle(img,(447,63),  63,  (0,0,255),  -1)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def drawEllipse():
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.ellipse(img,(256,256),(100,50),0,0,360,255,-1)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def drawText():
    img = np.zeros((512, 512, 3), np.uint8)
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'OpenCV',(10,500),  font,  4,(255,255,255),2)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    #drawLine()
    #drawRect()
    #drawCircle()
    #drawEllipse()
    drawText()

if __name__ == '__main__':
    main()