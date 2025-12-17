import cv2


class PhoneBackend:
    def __init__(self, config):
        Url = config.get("Url")
        Width = config.get("Width", 1280)
        Height = config.get("Height", 720)

        if Url is None:
            raise ValueError("Phone camera requires url")

        self.Capture = cv2.VideoCapture(Url)
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
