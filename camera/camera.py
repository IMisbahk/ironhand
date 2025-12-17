from camera.backends.webcam import WebcamBackend
from camera.backends.phone import PhoneBackend


class Camera:
    def __init__(self, source=0, config=None):
        self.Source = source
        self.Config = config or {}

        if source == 0:
            self.Backend = WebcamBackend(self.Config)
        elif source == 1:
            self.Backend = PhoneBackend(self.Config)
        else:
            raise ValueError("ur camera source isnt supported")

    def Read(self):
        return self.Backend.read()

    def Release(self):
        self.Backend.release()
