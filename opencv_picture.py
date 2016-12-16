# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt

def showPic():
    # load an image
    #   cv2.IMREAD_COLOR
    #   cv2.IMREAD_GRAYSCALE
    #   cv2.IMREAD_UNCHANGED
    img = cv2.imread('football.jpg', cv2.IMREAD_UNCHANGED)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def creatWindow():
    # create an image
    #   cv2.WINDOW_NORMAL
    #   cv2.WINDOW_AUTO
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    img = cv2.imread('football.jpg', cv2.IMREAD_UNCHANGED)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def savePic():
    img = cv2.imread('football.jpg', cv2.IMREAD_UNCHANGED)
    cv2.imshow('image', img)
    cv2.imwrite('message.png', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def keywordOpe():
    img = cv2.imread('football.jpg', cv2.IMREAD_UNCHANGED)
    cv2.imshow('image', img)
    key = cv2.waitKey(0)&0xFF
    if key == 27: # wait for ESC
        cv2.destroyAllWindows()
    elif key == ord('s'):
        cv2.imwrite('save.jpg', img)
        cv2.destroyAllWindows()

def matPlotPic():
    img = cv2.imread('football.jpg', cv2.IMREAD_COLOR)
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])
    plt.show()

def getBGR():
    img = cv2.imread('football.jpg')
    px = img[100, 100]
    print px # B G R
    blue = img[100, 100, 0]
    print blue # B

def setBGR():
    img = cv2.imread('football.jpg')
    img[100, 100] = [255, 255, 255]
    px = img[100, 100]
    print px

def getImgProp():
    img = cv2.imread('football.jpg')
    print img.shape # line row alpha 
    print img.size  # px number
    print img.dtype # type

def setROI():
    img = cv2.imread('football.jpg')
    ball = img[1:49, 154:210]
    img[101:149, 154:210] = ball
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def setAlpha():
    img = cv2.imread('football.jpg')
    img[:, :, 2] = 0
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    #showPic()
    #creatWindow()
    #savePic()
    #keywordOpe()
    #matPlotPic()
    #getBGR()
    #setBGR()
    #getImgProp()
    #setROI()
    setAlpha()

if __name__ == '__main__':
    main()