import random
import cv2
import numpy as np
import pyautogui

# https://github.com/drov0/python-imagesearch

class ImageSearch:
    def __init__(self):
        pass

    def click_image(self, image, pos, action, timestamp):
        img = cv2.imread(image)
        height, width, channels = img.shape
        pyautogui.moveTo(pos[0] + (width / 2), pos[1] + (height / 2), timestamp)
        pyautogui.click(button=action)


    def imageSearch(self, image, precision=0.8):
        im = pyautogui.screenshot()
        img_rgb = np.array(im)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(image, 0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        delete_loc = np.where( res >= precision)
        for pt in zip(*delete_loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        cv2.imwrite('test.png', img_rgb)

        if max_val < precision:
            return [-1,-1]
        return max_loc


    def imageSearchMultiple(self, image, precision=0.8):
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

        if points:
            points.sort()
            realPoints = [points[0]]
            c = 0
            x = points[0][0]
            y = points[0][1]
            for i in points:
                if (abs(x - i[0]) > 5) or (abs(y - i[1]) > 5):
                    x = i[0]
                    y = i[1]
                    realPoints.append(i)

        cv2.imwrite('testMultiple.png', img_rgb)
        if max_val < precision:
            return [-1, -1]
        return realPoints
