import mediapipe as mp
import cv2
import math
from gestures.definitions import calculateDistance, calculateAngle
from vision.landmarks import THUMB_TIP, INDEX_TIP
from smoothing.filters import Smoother


class HandTracker:
    def __init__(self, maxHands=1, detectionConfidence=0.7, trackingConfidence=0.7):
        self.MPHands = mp.solutions.hands
        self.Hands = self.MPHands.Hands(
            static_image_mode=False,
            max_num_hands=maxHands,
            min_detection_confidence=detectionConfidence,
            min_tracking_confidence=trackingConfidence
        )
        self.Drawer = mp.solutions.drawing_utils

        # Smoothing for thumb and index positions
        self.thumbSmoother = Smoother(alpha=0.6)
        self.indexSmoother = Smoother(alpha=0.6)

        # Conversion factor: pixels to cm (rough estimate for webcam at arm's length)
        # This can be calibrated based on actual measurements
        self.pixels_to_cm = 0.026  # ~26 pixels = 1 cm at typical webcam distance

    def Process(self, frame, draw=False, drawThumbIndexLine=True):
        rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.Hands.process(rgbFrame)

        handsData = [] # all hand points
        if result.multi_hand_landmarks:
            for handLandmarks in result.multi_hand_landmarks:
                landmarks = []
                for lm in handLandmarks.landmark:
                    landmarks.append({
                        "x": lm.x,
                        "y": lm.y,
                        "z": lm.z
                    })
                handsData.append(landmarks)
                if draw:
                    self.Drawer.draw_landmarks(frame,handLandmarks, self.MPHands.HAND_CONNECTIONS)

                # Always draw thumb-index line with distance and angle
                if drawThumbIndexLine and len(landmarks) > max(THUMB_TIP, INDEX_TIP):
                    self._drawThumbIndexVisualization(frame, landmarks)

        return handsData

    def _drawThumbIndexVisualization(self, frame, landmarks):

        thumb = landmarks[THUMB_TIP]
        index = landmarks[INDEX_TIP]

       
        frameHeight, frameWidth = frame.shape[:2]

        thumbX = int(thumb["x"] * frameWidth)
        thumbY= int(thumb["y"] * frameHeight)
        indexX= int(index["x"] * frameWidth)
        indexY = int(index["y"] * frameHeight)

        smoothThumbX, smoothThumbY= self.thumbSmoother.Apply(thumbX, thumbY)
        smoothIndexX, smoothIndexY = self.indexSmoother.Apply(indexX, indexY)

        cv2.line(frame, (int(smoothThumbX), int(smoothThumbY)),
                (int(smoothIndexX), int(smoothIndexY)), (255, 0, 255), 3)

            
        cv2.circle(frame, (int(smoothThumbX), int(smoothThumbY)), 8, (0, 255, 255), -1) 
        cv2.circle(frame, (int(smoothIndexX), int(smoothIndexY)), 8, (255, 255, 0), -1)  

        pixelDistance = math.sqrt((smoothThumbX - smoothIndexX)**2 + (smoothThumbY - smoothIndexY)**2)
        cmDistance = pixelDistance * self.pixels_to_cm
        angle = calculateAngle(landmarks)
        midX= int((smoothThumbX + smoothIndexX) / 2)
        midY= int((smoothThumbY + smoothIndexY) / 2)

        cv2.rectangle(frame, (midX - 60, midY - 40), (midX + 60, midY + 10), (0, 0, 0), -1)
        cv2.putText(frame, f"{cmDistance:.1f}cm", (midX - 50, midY - 20),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.putText(frame, f"{angle:.1f}°", (midX - 50, midY - 5),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
