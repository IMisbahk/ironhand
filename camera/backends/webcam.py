import cv2

class WebcamBackend:
    def __init__(self, config):
        Index = config.get("index", 0)
        Width = config.get("width", 1280)
        Height = config.get("height", 720)

        self.Capture = cv2.VideoCapture(Index)
        self.Capture.set(cv2.CAP_PROP_FRAME_WIDTH, Width)
        self.Capture.set(cv2.CAP_PROP_FRAME_HEIGHT, Height)

    def read(self):
        Success, Frame = self.Capture.read()
        if not Success:
            return None
        Frame = cv2.flip(Frame, 1)
        return Frame

    def release(self):
        self.Capture.release()
