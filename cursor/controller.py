import math
import pyautogui
import time


class CursorController:
    def __init__(self):
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.01  
        self.lastClickTime = 0
        self.clickCooldown = 0.3 
        self.isDragging = False

    def moveCursor(self, x, y):
        pyautogui.moveTo(x, y)

    def leftClick(self):
        currentTime = time.time()
        if currentTime - self.lastClickTime > self.clickCooldown:
            pyautogui.click()
            self.lastClickTime = currentTime

    def rightClick(self):
        pyautogui.rightClick()

    def startDrag(self):
        if not self.isDragging:
            pyautogui.mouseDown()
            self.isDragging = True
    def stopDrag(self):
        if self.isDragging:
            pyautogui.mouseUp()
            self.isDragging = False

    def processGesture(self, gestureState):
        if gestureState is None:
            return
        if gestureState.get("pinch", False):
            self.leftClick()

        if gestureState.get("grab", False):
            if not self.isDragging:
                self.startDrag()
        else:
            if self.isDragging:
                self.stopDrag()


