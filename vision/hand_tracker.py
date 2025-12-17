import mediapipe as mp
import cv2


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

    def Process(self, frame, draw=False):
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

        return handsData
