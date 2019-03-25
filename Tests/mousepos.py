import pyautogui

if __name__ == "__main__":
    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()
    
    print(pyautogui.position())
