'''
    @FileName:DrawTacle.py
    @Author:yikai yang
    @Date:2023/5/15
    @Desc:Null
'''
import math
import queue

import cv2
import numpy as np

from Functions.DrawImg import DrawImg

DISTANCCE = 10
WINDOWSSIZE = 20  # Number of positions to consider in each window
THRESHOLD = 5

CIRCLE_RADIUS = 10
CIRCLE_COLOR = (0, 0, 255)  # Red color in BGR format
CIRCLE_THICKNESS = 2
COLOUR_ROUTE = 5
RADIOS_ROUTE = 5

class DrawTacle(DrawImg):
    def __init__(self):
        super(DrawTacle, self).__init__()
        self.queueList = [queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue(),
                          queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue()]

        self.lastOne = None

    def calculate_distance(self, tuple1, tuple2):

        if len(tuple1) != len(tuple2):
            raise ValueError("Tuples must have the same length.")

        squared_diff_sum = sum((p - q) ** 2 for p, q in zip(tuple1, tuple2))

        return squared_diff_sum

    def check_position_stability(self, positions, threshold):
        list_of_position = []
        for i in range(len(positions) - 1):
            first_position = (positions[i+1][1], positions[i+1][2])
            second_position = (positions[i][1], positions[i][2])
            list_of_position.append(first_position)
            difference = abs(self.calculate_distance(first_position, second_position))
            if difference > threshold:
                return -1, -1

        sum_1 = 0
        sum_2 = 0
        for item in list_of_position:

            sum_1 += item[0]
            sum_2 += item[1]

        return sum_1 / len(list_of_position), sum_2 / len(list_of_position)

    def getTacleImg(self):
        # Combine heatmaps

        if self.route == []:
            return []

        h = self.frameSize[1]
        w = self.frameSize[0]

        flipped_list = list(zip(*self.route))
        zombies = np.ones((int(h), int(w), 3), dtype=np.uint8) * 255

        for fingerIndex in range(len(flipped_list)):

            if self.drawList[fingerIndex]:
                self.lastOne = None
                i = 0
                while i < len(flipped_list[fingerIndex]) - WINDOWSSIZE + 1:
                    window_positions = flipped_list[fingerIndex][i:i + WINDOWSSIZE]
                    # Check stability within the window
                    is_stable = self.check_position_stability(window_positions, THRESHOLD)
                    if is_stable != (-1, -1):

                        if self.lastOne is None:

                            self.lastOne = is_stable
                            self.queueList[fingerIndex].put(is_stable)

                            cv2.circle(zombies, (int(is_stable[0]), int(is_stable[1])), CIRCLE_RADIUS, CIRCLE_COLOR,
                                       thickness=CIRCLE_THICKNESS)
                        else:
                            diff = self.calculate_distance(self.lastOne, is_stable)
                            if diff > 10 * THRESHOLD:
                                self.lastOne = is_stable
                                self.queueList[fingerIndex].put(is_stable)

                                cv2.circle(zombies, (int(is_stable[0]), int(is_stable[1])), CIRCLE_RADIUS, CIRCLE_COLOR,
                                           thickness=CIRCLE_THICKNESS)

                        i += WINDOWSSIZE
                    else:
                        i += 1

        return zombies.astype(np.uint8)

    def drawHeatRoute(self):
        h = self.frameSize[1]
        w = self.frameSize[0]

        zombies = np.ones((int(h), int(w), 3), dtype=np.uint8)* 255

        for fingerIndex in range(len(self.drawList)):

            if self.drawList[fingerIndex] and not self.queueList[fingerIndex].empty():

                self.drawActuralRoute(self.queueList[fingerIndex], zombies)

        cv2.imwrite("tacleRoute.jpg", zombies)
        return zombies.astype(np.uint8)

    def drawActuralRoute(self, queue, img):

        """
            generate route of heat map

            :argument heap
            :return img
        """

        last_one = queue.get()

        cv2.circle(img, (int(last_one[0]), int(last_one[1])), CIRCLE_RADIUS, CIRCLE_COLOR,
                   thickness=CIRCLE_THICKNESS)
        while not queue.empty():
            this_one = queue.get()

            cv2.line(img, (int(last_one[0]), int(last_one[1])), (int(this_one[0]), int(this_one[1])),
                     COLOUR_ROUTE, RADIOS_ROUTE)
            cv2.circle(img, (int(this_one[0]), int(this_one[1])), CIRCLE_RADIUS, CIRCLE_COLOR,
                       thickness=CIRCLE_THICKNESS)
            last_one = this_one

        return img.astype(np.uint8)

