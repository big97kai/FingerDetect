'''
    @FileName:DrawTacle.py
    @Author:yikai yang
    @Date:2023/5/15
    @Desc:Null
'''
import cv2
import numpy as np

from Functions.DrawImg import DrawImg


class DrawTacle(DrawImg):
    def __init__(self):
        super(DrawTacle, self).__init__()
        self.imgList = []

    def addImgList(self, img):
        self.imgList.append(img)

    def clearImg(self):
        self.imgList.clear()

    def getTacleImg(self):
        # Combine heatmaps

        if self.imgList == []:
            return []

        h = self.frameSize[1]
        w = self.frameSize[0]
        # x = np.arange(w)
        # y = np.arange(h)
        # X, Y = np.meshgrid(x, y)
        #pos = np.dstack((X, Y))
        zombies = np.ones((int(h), int(w)), np.float64)
        composite_heatmap = np.zeros_like(self.imgList[0])

        for heatmap in self.imgList:
            composite_heatmap += heatmap

        gray_image = cv2.cvtColor(composite_heatmap, cv2.COLOR_BGR2GRAY)
        # Apply a threshold to identify the heavy color areas
        # Iterate over the contours
        _, thresholded = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            # Calculate the bounding box for the contour
            x, y, w, h = cv2.boundingRect(contour)

            # Calculate the center point of the bounding box
            center_x = x + int(w / 2)
            center_y = y + int(h / 2)

            # Draw a circle at the center point on the thresholded image
            cv2.circle(zombies, (center_x, center_y), radius=5, color=(0, 0, 0), thickness=-1)

        return zombies
