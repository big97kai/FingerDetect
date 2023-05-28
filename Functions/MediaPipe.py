'''
    @FileName:MediaPipe.py
    @Author:yikai yang
    @Date:2023/2/13
    @Desc:Null
'''

import mediapipe as mp

"""
    This is mediapiepe model to detect hands
    
    :argument null
    :return null
"""


class MediaPipe():
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=False,
                                         max_num_hands=2,
                                         min_detection_confidence=0.05,
                                         min_tracking_confidence=0.2)
