'''
    @FileName:Model.py
    @Author:yikai yang
    @Date:2023/5/26
    @Desc:Null
'''
import cv2
from matplotlib.pyplot import hsv

from Functions.ColourDetect import ColourDetect
from Functions.MediaPipe import MediaPipe


class Model():
    def __init__(self):
        self.model = None
        self.modelIndex = 0
        self.firstFrame = None
        self.trackerSize = 0

    def setFirstFrame(self, firstFrame):

        self.firstFrame = cv2.cvtColor(firstFrame, cv2.COLOR_BGR2HSV)

    def setModelIndex(self, index):
        self.modelIndex = index
        if index == 0:
            self.model = MediaPipe()
        else:
            self.model = ColourDetect()

    def setRoiInist(self, Rois):
        len = 1
        for roi in Rois:
            if roi[0] != -1:
                self.model.setRoi(roi)
                x, y, width, height = roi
                roi_frame = self.firstFrame[y:y + height, x:x+width]
                self.model.setInitial(roi_frame)
                cv2.imwrite(str(len) + ".jpg", roi_frame)
                len += 1
