import numpy as np
from smoothing.filters import Smoother


class CursorMapper:
    def __init__(self, screenWidth, screenHeight):
        self.ScreenWidth = screenWidth
        self.ScreenHeight = screenHeight
        
        self.thumbSmoother = Smoother(alpha=0.6)
        self.indexSmoother = Smoother(alpha=0.6)


    def Map(self, landmark):
       
        x_normalized = landmark["x"]
        y_normalized = landmark["y"]


        #----cursor ai generated code----  
        x_expanded = (x_normalized - 0.1) / 0.8  
        y_expanded = (y_normalized - 0.1) / 0.8  
        x_expanded = max(0.0, min(1.0, x_expanded))
        y_expanded = max(0.0, min(1.0, y_expanded))
        #--------------------------------
        
        x = int(x_expanded * self.ScreenWidth)
        y = int(y_expanded * self.ScreenHeight)

        x = max(0, min(self.ScreenWidth - 1, x))
        y = max(0, min(self.ScreenHeight - 1, y))

        return x, y

    def MapMidpoint(self, landmark1, landmark2):

        midpoint = {
            "x": (landmark1["x"] + landmark2["x"]) / 2,
            "y": (landmark1["y"] + landmark2["y"]) / 2
        }

        return self.Map(midpoint)

    def getSmoothedThumbScreen(self, thumbLandmark):
        screenX, screenY = self.Map(thumbLandmark)
        return self.thumbSmoother.Apply(screenX, screenY)

    def getSmoothedIndexScreen(self, indexLandmark):
        screenX, screenY = self.Map(indexLandmark)
        return self.indexSmoother.Apply(screenX, screenY)
