'''
    @FileName:DrawHeat.py
    @Author:yikai yang
    @Date:2023/5/26
    @Desc:Null
'''
from Functions.DrawImg import DrawImg
import cv2
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap, Normalize
from scipy.stats import multivariate_normal
import queue

COLOUR_ROUTE = (255, 0, 0)
RADIOS_ROUTE = 30
DISTANCETHRESHOLD = 10

class DrawHeat(DrawImg):
    def __init__(self):
        super(DrawHeat, self).__init__()
        self.queueList = [queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue(),
                          queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue()]

    def calcutateNormal(self, img, finger, width, height):
        """
            generate normal distribution

            :argument left hand data, right hand data, which finger to draw, frame
            :return img
        """
        for single_position in self.route:

            if not single_position:

                continue
            else:
                single_position = single_position[finger]
                #
                # rv = multivariate_normal([single_position[1], single_position[2]], [[50, 0], [0, 50]])
                # Z = rv.pdf(pos)
                # img += Z
                radius = 15

                x = single_position[1]
                y = single_position[2]
                x_min = max(0, x - radius)
                x_max = min(width - 1, x + radius)
                y_min = max(0, y - radius)
                y_max = min(height - 1, y + radius)

                img[y_min:y_max, x_min:x_max] -= 10

        return img

    def hotDraw(self):
        """
            generate heat map

            :argument left hand data, right hand data, frame, which finger to draw
            :return img
        """
        # Generate mockup data
        h = self.frameSize[1]
        w = self.frameSize[0]
        # x = np.arange(w)
        # y = np.arange(h)
        # X, Y = np.meshgrid(x, y)
        #pos = np.dstack((X, Y))
        zombies = np.ones((int(h), int(w)), np.float64)

        for i in range(len(self.drawList)):
            if self.drawList[i]:
                zombies = self.calcutateNormal(zombies, i, w, h)

        zombies -= np.min(zombies)

        zombies /= np.max(zombies)
        #
        # heatmap_image = np.uint8(zombies)

        # # Generate custom colormap with alpha channel,
        # # cf. https://stackoverflow.com/a/37334212/11089932
        cmap = cm.gray
        c_cmap = cmap(np.arange(cmap.N))
        c_cmap[:, -1] = np.linspace(0, 1, cmap.N)
        c_cmap = ListedColormap(c_cmap)
        #
        # # Generate heatmap, cf. https://stackoverflow.com/a/31546410/11089932
        norm = Normalize(vmin=zombies.min(), vmax=zombies.max())
        heatmap = c_cmap(norm(zombies))
        heatmap = cv2.cvtColor(np.uint8(heatmap * 255), cv2.COLOR_RGB2BGR)
        #

        return heatmap

    def isPositionNearThresholded(self, thresholded, x, y, i):

        if thresholded[y, x] == 0:
            self.queueList[i].put((x, y))

        # Check nearby pixels within the distance threshold
        y_min = max(0, y - DISTANCETHRESHOLD)
        y_max = min(thresholded.shape[0] - 1, y + DISTANCETHRESHOLD)
        x_min = max(0, x - DISTANCETHRESHOLD)
        x_max = min(thresholded.shape[1] - 1, x + DISTANCETHRESHOLD)
        nearby_pixels = thresholded[y_min:y_max, x_min:x_max]
        if np.any(nearby_pixels == 0):
            self.queueList[i].put((x, y))

    def calculateHot(self, image):
        """
            generate in heat zone and out heat zone time list

            :argument image, left finger data, right finger data, which finger to draw
            :return time start into the zone list, time out into the zone list
        """

        h = self.frameSize[1]
        w = self.frameSize[0]
        img_blank = np.zeros((int(h), int(w), 3), np.uint8)
        img_blank[:] = [255, 255, 255]

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Apply a threshold to identify the heavy color areas
        _, thresholded = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)

        cv2.imwrite("thresholded.jpg", thresholded)

        for i in range(len(self.drawList)):

            if self.drawList[i]:

                for coordinate in self.route:

                    coordinate = coordinate[i]
                    self.isPositionNearThresholded(thresholded, coordinate[1], coordinate[2], i)

        for i in range(len(self.drawList)):

            if self.drawList[i]:
                self.drawRouteHot(self.queueList[i], img_blank)

        return img_blank

    def drawRouteHot(self, queue, img):

        """
            generate route of heat map

            :argument heap
            :return img
        """
        last_one = queue.get()

        while not queue.empty():
            this_one = queue.get()

            cv2.line(img, (last_one[0], last_one[1]), (this_one[0], this_one[1]),
                     COLOUR_ROUTE, RADIOS_ROUTE)
            last_one = this_one

        return img
