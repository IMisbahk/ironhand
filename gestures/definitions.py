import math
from vision.landmarks import *

def distance(a, b):
    return math.sqrt((a['x'] - b['x']) ** 2 + (a['y'] - b['y']) ** 2)

def pinch(landmarks, threshold=.07):
    thumb = landmarks[THUMB_TIP]
    index = landmarks[INDEX_TIP]
    return distance(thumb, index) < threshold

def extended(tip, base):
    return tip["y"] < base["y"]

def grabbing(landmarks):
    folded = 0

    if not extended(landmarks[INDEX_TIP], landmarks[WRIST]):
        folded += 1
    if not extended(landmarks[MIDDLE_TIP], landmarks[WRIST]):
        folded += 1
    if not extended(landmarks[RING_TIP], landmarks[WRIST]):
        folded += 1
    if not extended(landmarks[PINKY_TIP], landmarks[WRIST]):
        folded += 1

    return folded >= 3


def calculateDistance(landmarks):
    thumb = landmarks[THUMB_TIP]
    index = landmarks[INDEX_TIP]
    return math.sqrt((thumb["x"] - index["x"])**2 + (thumb["y"] - index["y"])**2)

def calculateAngle(landmarks):
    thumb = landmarks[THUMB_TIP]
    index = landmarks[INDEX_TIP]
    dx = index["x"] - thumb["x"]
    dy = index["y"] - thumb["y"]
    return math.degrees(math.atan2(dy, dx))
