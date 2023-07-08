"""
    @FileName:ColourDetect.py
    @Author:yikai yang
    @Date:2023/2/23
    @Desc:Null
"""
import cv2
import cv2 as cv
import numpy as np


class ColourDetect():

    def __init__(self):

        self.roi = []
        self.roisHist = []
        self.frame = None
        self.currentIndex = 0
        self.term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 50, 1)

    def setCurrentIndex(self, currentIndex):
        self.currentIndex = currentIndex

    def setFrame(self, frame):
        self.frame = frame

    def setRoi(self, roi):

        self.roi.append(roi)

    def setInitial(self, roi_frame):

        mask = cv2.inRange(roi_frame, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
        self.roisHist.append(cv2.calcHist([roi_frame], [0], mask, [180], [0, 180]))
        cv2.normalize(self.roisHist[-1], self.roisHist[-1], 0, 255, cv2.NORM_MINMAX)

    def colourDetectSimple(self):

        x, y, width, height = self.roi[self.currentIndex]
        hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        # Calculate the back projection based on the histogram
        back_proj = cv2.calcBackProject([hsv], [0], self.roisHist[self.currentIndex], [0, 180], 1)

        # Apply CamShift to track the object
        ret, self.roi[self.currentIndex] = cv2.meanShift(back_proj, (x, y, width, height), self.term_criteria)

        if self.roi[self.currentIndex] is not None:
            # Get the center of the track_window
            center_x = int(self.roi[self.currentIndex][0] + self.roi[self.currentIndex][2] / 2)
            center_y = int(self.roi[self.currentIndex][1] + self.roi[self.currentIndex][3] / 2)

            return self.roi[self.currentIndex]
        else:

            print("Track window is None")
            return -1, -1, -1, -1
