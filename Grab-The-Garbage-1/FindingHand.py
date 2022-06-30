import mediapipe as mp
import cv2
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
from variables import *


class FindHands:
    def __init__(self):
        self.hand_tracking = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.Fistclosed= False
        self.FistMid_x = 0
        self.FistMid_y = 0
        self.Final = None

    def cv2Hands(self, img):
        rows, cols, _ = img.shape
        img =  cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)
        img.flags.writeable = False
        self.Final =  self.hand_tracking.process(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        self.Fistclosed= False

        if self.Final.multi_hand_landmarks:
            for hand_landmarks in self.Final.multi_hand_landmarks:
                x, y = hand_landmarks.landmark[9].x, hand_landmarks.landmark[9].y

                self.FistMid_x = int(x * SWIDTH)
                self.FistMid_y= int(y * SHEIGHT)
               
                x1, y1 = hand_landmarks.landmark[12].x, hand_landmarks.landmark[12].y

                if y1 > y:
                    self.Fistclosed= True

                mp_drawing.draw_landmarks(
                    img,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
        return img
    def get_Fist_center(self):
        return (self.FistMid_x, self.FistMid_y)


    def display_Fist(self):
        cv2.imshow("image", self.image)
        cv2.waitKey(1)

    def is_Fist_closed(self):
        pass