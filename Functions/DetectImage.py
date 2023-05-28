"""
    @FileName:DetectImage.py
    @Author:yikai yang
    @Date:2023/1/12
    @Desc:Null
"""

import cv2
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap, Normalize
from scipy.stats import multivariate_normal
import queue

COLOUR_ROUTE = (255, 0, 0)
RADIOS_ROUTE = 10


class DetectImage():

    def __init__(self, draw_list, frame_size, route):

        self.draw_list = draw_list
        self.frame_size = frame_size
        self.route = route
        self.queueList = [queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue(),
                          queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue()]

    def __init__(self):

        self.draw_list = []
        self.frame_size = ()
        self.route = []

    def set_draw_list(self, draw_list):

        self.draw_list = draw_list

    def set_frame_size(self, frame_size):

        self.frame_size = frame_size

    def set_route(self, route):

        self.route = route

    def draw_route(self, img, before_point, route_list, permission):
        """
            draw route from a finger

            :argument img to draw, before point, route list, which finger
            :return img
        """
        for single_position in route_list:
            if not single_position:

                continue
            else:
                single_position = single_position[permission]
                if before_point is None:
                    before_point = single_position
                else:
                    cv2.line(img, (before_point[1], before_point[2]), (single_position[1], single_position[2]),
                             COLOUR_ROUTE, RADIOS_ROUTE)
                    before_point = single_position

        return img, before_point

    def draw_already(self):
        """
            draw already pass area

            :argument left hand data, right hand data, which finger to draw, frame
            :return img
        """
        img_blank = np.zeros((int(self.frame_size[1]), int(self.frame_size[0]), 3), np.uint8)
        img_blank[:] = [255, 255, 255]
        before_point = None
        for i in range(len(self.draw_list)):
            if self.draw_list[i]:
                img_blank, before_point = self.draw_route(img_blank, before_point, self.route, i)

        return img_blank

    def calcutate_normal(self, img, rout_list, pos, finger):
        """
            generate normal distribution

            :argument left hand data, right hand data, which finger to draw, frame
            :return img
        """
        for single_position in rout_list:

            if not single_position:

                continue
            else:
                single_position = single_position[finger]

                rv = multivariate_normal([single_position[1], single_position[2]], [[50, 0], [0, 50]])
                Z = rv.pdf(pos)
                img += Z

        return img

    def hot_draw(self):
        """
            generate heat map

            :argument left hand data, right hand data, frame, which finger to draw
            :return img
        """
        # Generate mockup data
        h = self.frame_size[1]
        w = self.frame_size[0]
        x = np.arange(w)
        y = np.arange(h)
        X, Y = np.meshgrid(x, y)

        pos = np.dstack((X, Y))
        zombies = np.zeros((int(h), int(w)), np.float64)

        for i in range(len(self.draw_list)):
            if self.draw_list[i]:
                zombies = self.calcutate_normal(zombies, self.route, pos, i)

        zombies /= np.max(zombies)
        # Generate custom colormap with alpha channel,
        # cf. https://stackoverflow.com/a/37334212/11089932
        cmap = cm.autumn_r
        c_cmap = cmap(np.arange(cmap.N))
        c_cmap[:, -1] = np.linspace(0, 1, cmap.N)
        c_cmap = ListedColormap(c_cmap)

        # Generate heatmap, cf. https://stackoverflow.com/a/31546410/11089932
        norm = Normalize(vmin=zombies.min(), vmax=zombies.max())
        heatmap = c_cmap(norm(zombies))
        heatmap = cv2.cvtColor(np.uint8(heatmap * 255), cv2.COLOR_RGBA2BGRA)
        return heatmap

    def judge_in_zoom(self, contours, x, y):
        """
            generate in heat zone and out heat zone time

            :argument wheather in the zone, finger data, coord zone, time stamp, time start into the zone list, time out into the zone list
            :return time start into the zone list, time out into the zone list
        """

        for contour in contours:
            result = cv2.pointPolygonTest(contour, (x, y), False)
            if result >= 0:
                M = cv2.moments(contour)

                # Calculate the centroid coordinates
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                return cx, cy

        return -1, -1

    def calculate_hot(self, image):
        """
            generate in heat zone and out heat zone time list

            :argument image, left finger data, right finger data, which finger to draw
            :return time start into the zone list, time out into the zone list
        """
        heatmap = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Convert the image to grayscale
        gray_heatmap = cv2.cvtColor(heatmap, cv2.COLOR_RGB2GRAY)

        # Apply a threshold to identify the heavy color areas
        _, thresholded = cv2.threshold(gray_heatmap, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Find the contours of the thresholded areas
        contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        isInZoom = [False, False, False, False, False, False, False, False, False, False]

        for i in range(len(self.draw_list)):

            if self.draw_list[i] and not isInZoom[i]:
                x, y = self.judge_in_zoom(contours, x, y)
                if x != -1:
                    self.queueList[i].put((x, y))

        for i in range(len(self.draw_list)):

            if self.draw_list[i]:
                self.draw_route_hot(self.queueList[i], contours)

        return contours

    def draw_route_hot(self, queue, img):

        """
            generate route of heat map

            :argument heap
            :return img
        """
        last_one = queue.get()

        while queue.size() != 0:
            this_one = queue.get()

            cv2.line(img, (last_one[0], last_one[1]), (this_one[0], this_one[1]),
                     COLOUR_ROUTE, RADIOS_ROUTE)
            last_one = this_one

        return img
