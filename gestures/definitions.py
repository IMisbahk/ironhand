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



#gemini 
def calculate_angle(a, b, width, height):
    """
    Calculates the angle of the line connecting a and b relative to the vertical axis.
    """
    dx = (b['x'] - a['x']) * width
    dy = (b['y'] - a['y']) * height
    
    # atan2(dx, dy) gives 0 for (0, 1) i.e. vertical down, and 90 for (1, 0) i.e. horizontal right
    angle_rad = math.atan2(dx, dy)
    angle_deg = math.degrees(angle_rad)
    
    return abs(angle_deg)


