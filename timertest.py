import random
import time
import sys
import pyautogui
from pynput.mouse import Button as pynputButton
from pynput.mouse import Controller as pynputController
from imagesearch import *
from kivy.app import App
from kivy.uix.button import *
from kivy.uix.gridlayout import *
from kivy.config import Config

def delay(duration):
    time.sleep(duration)


def EventRaid():
    print("EventRaid")

    pos = imageSearch.imageSearchMultiple("collection/Event_Choose_Level.png")
    print(pos)
    pos = sorted(pos, key=lambda x: x[1], reverse=True)
    pos = pos[0]

    temp = imageSearch.imageSearch("collection/Event_Battle_Remaining.png")
    if temp[0] == -1:
        imageSearch.click_image("collection/Event_Choose_Level.png", pos, "left", 0.1)
        delay(0.4)
        pos = imageSearch.imageSearch("collection/Event_Start_Battle.png")

if __name__ == "__main__":

    mouse = pynputController()
    imageSearch = ImageSearch() 
    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()

    Config.set('graphics', 'width', '480')
    Config.set('graphics', 'height', '270')

    EventRaid()