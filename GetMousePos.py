import random
import time
import sys
import pyautogui
from pynput.mouse import Button as pynputButton
from pynput.mouse import Controller as pynputController
import cv2
import numpy as np
import array as arr

def delay(duration):
    time.sleep(duration)

def sleep(duration):
    time.sleep(duration)

def imageSearchMultiple(image, precision=0.8):
        im = pyautogui.screenshot()
        img_rgb = np.array(im)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(image, 0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        points = []

        delete_loc = np.where( res >= precision)
        for pt in zip(*delete_loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)
            points.append(pt)
            print(pt)

        if points:
            realPoints = [points[0]]
            c = 0
            x = points[0][0]
            y = points[0][1]
            for i in points:
                if (abs(x - i[0]) > 5) or (abs(y - i[1]) > 5):
                    x = i[0]
                    y = i[1]
                    realPoints.append(i)

            print(realPoints)

        cv2.imwrite('testMultiple.png', img_rgb)
        if max_val < precision:
            return [-1, -1]
        return realPoints

if __name__ == "__main__":

    mouse = pynputController()
    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()

    print(pyautogui.position())