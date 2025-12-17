from gestures.definitions import pinch, grabbing, extended


class GestureEngine:
    def __init__(self):
        self.LastState = None

    def Interpret(self, landmarks):
        if landmarks is None:
            return None
        
        ispinch = pinch(landmarks)
        isgrab = grabbing(landmarks)
        isOpen = not isgrab

        state = {
            "pinch": ispinch,
            "grab": isgrab,
            "open": isOpen
        }

        self.LastState = state
        return state
