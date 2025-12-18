import numpy as np


class CursorMapper:
    def __init__(self, screenWidth, screenHeight):
        self.ScreenWidth = screenWidth
        self.ScreenHeight = screenHeight

    def Map(self, landmark):
        
        # landmark: dict with x, y in normalized space (0–1)
        
        # removed x = int(landmark["x"] * self.ScreenWidth)
        # Mirror X coordinate for natural webcam feel  - claude 4.5 
        x = int((1 - landmark["x"]) * self.ScreenWidth)
        #---

        
        y = int(landmark["y"] * self.ScreenHeight)

        # clamp
        x = max(0, min(self.ScreenWidth, x))
        y = max(0, min(self.ScreenHeight, y))

        return x, y
