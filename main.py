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


class ButtonLayout(GridLayout):
    def __init__(self, **kwargs):
        super(ButtonLayout, self).__init__(**kwargs)
        self.cols = 3
        self.add_widget(Button(text="CollectCampaignLoop", on_press=lambda a: CollectCampaignLoop()))
        self.add_widget(Button(text="CelestialIsland", on_press=lambda a: CelestialIsland()))
        self.add_widget(Button(text="HandOfMidas", on_press=lambda a: HandOfMidas()))
        self.add_widget(Button(text="EventRaid", on_press=lambda a: EventRaid()))
        self.add_widget(Button(text="Arena", on_press=lambda a: Arena()))
        self.add_widget(Button(text="SealLand", on_press=lambda a: SealLand()))
        self.add_widget(Button(text="LookAtAds", on_press=lambda a: LookAtAds()))
        self.add_widget(Button(text="Everything", on_press=lambda a: Everything()))
        self.add_widget(Button(text="Exit", on_press=lambda a: Exit()))

class ControllWindow(App):
    def build(self):
        return ButtonLayout()

def delay(duration):
    time.sleep(duration)

def click(x, y):
    mouse.position = (x, y)
    mouse.click(pynputButton.left)
    delay(0.7)

def MoveMainScreen(direction, i=2):
    x = screenWidth/2
    y = screenHeight/2
    drag = 900

    for _ in range(i):
        if direction == "left":
            pyautogui.moveTo(x=x - 500, y=y)
            mouse.press(pynputButton.left)
            pyautogui.moveTo(x=x + 200, y=y, duration=0.3)
            mouse.release(pynputButton.left)
        elif direction == "right":
            pyautogui.moveTo(x=x + 500, y=y)
            mouse.press(pynputButton.left)
            pyautogui.moveTo(x=x - 200, y=y, duration=0.3)
            mouse.release(pynputButton.left)

def LookAtAds():
    print("LookAtAds")
    targetNox()
    adsPos = imageSearch.imageSearch("collection/ads.png")
    while adsPos[0] != -1:
        imageSearch.click_image("collection/ads.png", adsPos, "left", 0.1)
        delay(1.5)
        pos = imageSearch.imageSearch("collection/ads_ok.png")
        imageSearch.click_image("collection/ads_ok.png", pos, "left", 0.1)
        delay(2)
        pos = imageSearch.imageSearch("collection/home.png")
        imageSearch.click_image("collection/home.png", pos, "left", 0)
        delay(2)
        pos = imageSearch.imageSearch("collection/StartAppIcon.png")
        imageSearch.click_image("collection/StartAppIcon.png", pos, "left", 0)
        while True:
            delay(0.3)
            pos = imageSearch.imageSearch("collection/AnchorMainMenu.png")
            if pos[0] != -1:
                break
        delay(0.3)
        adsPos = imageSearch.imageSearch("collection/ads.png")

def old_LookAtAds():
    for _ in range(5):
        click(500, 825)
        click(1080, 640)
        for i in range(75):
            delay(1)
            print(i)
        click(1620, 785)
        delay(5)

def waitForImageThenClick(path):
    pos = imageSearch.imageSearch(path)
    while pos[0] == -1:
        delay(0.1)
        pos = imageSearch.imageSearch(path)
    imageSearch.click_image(path, pos, "left", 0)

def Arena():
    print("Arena")
    targetNox()
    
    pos = imageSearch.imageSearch("collection/MainMenu_Arena.png")
    while pos[0] == -1:
        pos = imageSearch.imageSearch("collection/AnchorMainMenu.png")
        if pos[0] == -1:
            GotoMainMenu()
        else:
            MoveMainScreen("right")
        pos = imageSearch.imageSearch("collection/MainMenu_Arena.png")
    imageSearch.click_image("collection/MainMenu_Arena.png", pos, "left", 0.1) # click arena
    waitForImageThenClick("collection/Arena_Join.png")
    delay(0.3)
    for _ in range(3):
        delay(0.3)
        pos = imageSearch.imageSearch("collection/Arena_Battle.png")
        while pos[0] != -1:
            waitForImageThenClick("collection/Arena_Battle.png") # click battle
            delay(0.2)
            pos = imageSearch.imageSearch("collection/Arena_Battle.png")
        click(1264, 744) # click battle from list
        waitForImageThenClick("collection/Arena_Fight.png") # click battle
        waitForImageThenClick("collection/Arena_CollectReward.png")
        delay(0.3)
        click(972, 762) # remove reward window
        click(972, 762) # click ok
    delay(0.3)
    GotoMainMenu() # click back (to main menu)

def Arena2():
    print("Arena2")
    targetNox()  
    pos = imageSearch.imageSearch("collection/MainMenu_Arena.png")
    while pos[0] == -1:
        pos = imageSearch.imageSearch("collection/AnchorMainMenu.png")
        if pos[0] == -1:
            GotoMainMenu()
        else:
            MoveMainScreen("right")
        pos = imageSearch.imageSearch("collection/MainMenu_Arena.png")
    imageSearch.click_image("collection/MainMenu_Arena.png", pos, "left", 0.1) # click arena
    delay(0.3)
    click(624, 475)
    delay(0.3)
    click(1142, 746)
    delay(0.3)
    for _ in range(50):
        pos = imageSearch.imageSearch("collection/Arena_Battle.png")
        while pos[0] != -1:
            waitForImageThenClick("collection/Arena_Battle.png") # click battle
            delay(0.1)
            pos = imageSearch.imageSearch("collection/Arena_Battle.png")
        click(1264, 744) # click battle from list
        delay(0.3)
        click(990, 771)
        delay(0.3)
        waitForImageThenClick("collection/Arena_CollectReward.png")
        delay(0.3)
        click(972, 762) # remove reward window
        click(972, 762) # click ok
    delay(0.3)
    GotoMainMenu() # click back (to main menu)

def CheckIn():
    print("CheckIn")
    targetNox()
    click(479, 227)
    click(1297, 766)
    click(720, 881)
    pyautogui.press("escape")
    GotoMainMenu()

def HandOfMidas():
    print("HandOfMidas")
    targetNox()
    click(921, 201)
    click(841, 662)
    click(720, 881)
    click(1373, 327)

def CollectCampaign():
    print("CollectCampaign")
    targetNox()
    MoveMainScreen("right")
    click(430, 535)
    delay(0.5)
    click(1453, 312)
    click(1415, 607)
    click(950, 774)
    click(367, 211)

def CollectCampaignLoop():
    while True:
        print("CollectCampaignLoop")
        targetNox()
        MoveMainScreen("right")
        click(430, 535)
        delay(0.5)
        click(1453, 312)
        click(1415, 607)
        click(950, 774)
        click(367, 211)
        delay(7200)

def SealLand():
    print("SealLand")
    targetNox()
    while True:
        pos = imageSearch.imageSearch("collection/MainMenu_SealLand.png")
        if pos[0] != -1:
            break
        MoveMainScreen("right", 1)
    imageSearch.click_image("collection/MainMenu_SealLand.png", pos, "left", 0.1) # click pos of the gate
    delay(0.3)
    click(655, 877)
    delay(0.3)
    click(960, 813)
    delay(0.3)
    click(1227, 332)
    delay(0.3)
    click(1165, 507)
    delay(0.3)
    click(966, 668)
    delay(0.3)
    click(958, 772)
    delay(0.3)
    click(351, 213)
    delay(0.3)
    click(351, 213)
    delay(0.3)

def UpdateBestSealLand():
    targetNox()
    pos = imageSearch.imageSearch("collection/AnchorMainMenu.png")
    if pos[0] == -1:
        GotoMainMenu()

    MoveMainScreen("right") # Move camera to find the Seal Land gate
    delay(5)

    pos = imageSearch.imageSearch("collection/MainMenu_SealLand.png") # Search screen for the gate
    if pos[0] == -1:
        print("Error, Seal Land")
        return
    
    imageSearch.click_image("collection/MainMenu_SealLand.png", pos, "left", 0.1) # click pos of the gate
    delay(0.3)

    pos = imageSearch.imageSearch("collection/Sealland_IsSealland.png") # Have we arrived at the Seal Land?
    if pos[0] == -1:
        print("Error, Seal Land")
        return

    print("it works so far")

    #pos = imageSearch.imageSearch("collection/Sealland_20.png")
    #if pos[0] == -1:
    pass

def targetNox():
    pos = imageSearch.imageSearch("collection/TargetNox.png") # Target window
    imageSearch.click_image("collection/TargetNox.png", pos, "left", 0.1)

def GotoMainMenu():
    targetNox()

    while True:
        pos = imageSearch.imageSearch("collection/AnchorMainMenu.png")
        if pos[0] != -1:
            break
        pyautogui.press("esc")
        delay(0.3)

def CelestialIsland():
    print("CelestialIsland")
    targetNox()
    while True:
        pos = imageSearch.imageSearch("collection/CelestialIsland.png")
        if pos[0] != -1:
            break
        MoveMainScreen("left", 1)
    GotoMainMenu()

def Everything():
    CollectCampaign()
    HandOfMidas()
    CheckIn()
    Arena()
    SealLand()
    LookAtAds() 
    CollectMail()
    EventRaid()
    print("Done")

def CollectMail():
    print("CollectMail")
    targetNox()
    delay(0.5)
    click(364, 534)
    delay(0.5)
    click(652, 306)
    delay(0.5)
    click(1410, 244)

def EventRaid():
    print("EventRaid")

    pos = imageSearch.imageSearch("collection/Event_Start.png")
    imageSearch.click_image("collection/Event_Start.png", pos, "left", 0.1)
    delay(0.5)

    challengePos = imageSearch.imageSearchMultiple("collection/Event_Choose_Challenge.png")
    print(challengePos)
    delay(0.5)
    for elem in challengePos:
        imageSearch.click_image("collection/Event_Choose_Challenge.png", elem, "left", 0.1)
        delay(0.4)
        pos = imageSearch.imageSearch("collection/Event_Identifier.png")
        if pos[0] != -1:
            # Event_Buy_Plus.png
            pos = imageSearch.imageSearch("collection/Event_Buy_Plus.png")
            imageSearch.click_image("collection/Event_Buy_Plus.png", pos, "left", 0.1)
            delay(0.2)
            # Event_Buy_Max.png
            pos = imageSearch.imageSearch("collection/Event_Buy_Max.png")
            if pos[0] != -1:
                imageSearch.click_image("collection/Event_Buy_Max.png", pos, "left", 0.1)
            # Event_Buy_Ok.png
                pos = imageSearch.imageSearch("collection/Event_Buy_Ok.png")
                imageSearch.click_image("collection/Event_Buy_Ok.png", pos, "left", 0.1)
                delay(0.5)
            else:
                delay(3.5)
                
        pos = imageSearch.imageSearchMultiple("collection/Event_Choose_Level.png")
        print(pos)
        pos = sorted(pos, key=lambda x: x[1], reverse=True)
        pos = pos[0]

        temp = imageSearch.imageSearch("collection/Event_Battle_Remaining.png")
        if temp[0] == -1:
            imageSearch.click_image("collection/Event_Choose_Level.png", pos, "left", 0.1)
            delay(0.4)
            pos = imageSearch.imageSearch("collection/Event_Start_Battle.png")
            imageSearch.click_image("collection/Event_Start_Battle.png", pos, "left", 0.1)

            # Handles the battles itself and the repeat thing
            while True:
                #Waiting for the battle to end and show the Victory Screen (OK Button)
                while True:
                    pos = imageSearch.imageSearch("collection/Event_Battle_Ok.png")
                    if pos[0] != -1:
                        break
                delay(0.1)
                
                # Press Next if it exists, OK if it doesn't exist
                pos = imageSearch.imageSearch("collection/Event_Next_Battle.png")
                if pos[0] == -1:
                    pos = imageSearch.imageSearch("collection/Event_Battle_Ok.png")
                    imageSearch.click_image("collection/Event_Battle_Ok.png", pos, "left", 0.1)
                    break
                else:
                    imageSearch.click_image("collection/Event_Next_Battle.png", pos, "left", 0.1)
            delay(0.5)
        pyautogui.press("esc")
        delay(0.5)
    pyautogui.press("esc")

def Exit():
    ControllWindow().stop()

if __name__ == "__main__":

    mouse = pynputController()
    imageSearch = ImageSearch() 
    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()

    Config.set('graphics', 'width', '480')
    Config.set('graphics', 'height', '270')
    ControllWindow().run()