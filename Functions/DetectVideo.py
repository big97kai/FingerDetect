"""
    @FileName:DetectVideo.py
    @Author:yikai yang
    @Date:2022/12/31
    @Desc:Null
"""
import time

import cv2

from Functions.Model import Model

import numpy as np

RADIOS_DETECT = int(15 * 1)
RADIOS_ROUTE = 5
COLOUR_DETECT = (0, 0, 255)
COLOUR_ROUTE = (255, 255, 255)

OUTPUT_PATH = "out.avi"


class DetectVideo:

    def __init__(self, path="", drawList=None):
        self.path = path
        self.drawList = drawList
        self.model = Model()

    def setPath(self, path):
        self.path = path

    def setDrawList(self, drawList):
        self.drawList = drawList

    def generate_video(self):

        """
            use model to detect finger position and collect position location and generate route

            :argument frame, last frame finger position, finger list to detect
            :return img with route, current frame finger position
        """
        # Record the start time
        start_time = time.time()
        # standard code to output video
        cap = cv2.VideoCapture(self.path)
        print(self.path)
        # set frame width and height
        frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        frame_size = (frame_width, frame_height)
        if self.model.modelIndex == 0:
            self.drawList.reverse()
        # standard code to output video
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        fps = cap.get(cv2.CAP_PROP_FPS)
        out = cv2.VideoWriter(OUTPUT_PATH, fourcc, fps, (int(frame_size[0]), int(frame_size[1])), True)
        trajectory = []

        success_time = 0
        frame_time = 1
        # deal every frame

        while (cap.isOpened()):

            success, frame = cap.read()
            print(success)
            if not success:
                break

            # try:
            right, single_frame, last_list = self.process_frame_origin(frame, trajectory)
            frame_time += 1
            if right:
                success_time += 1
            trajectory.append(last_list)

            # except:
            #     print('error')
            #     pass

            if success:
                out.write(single_frame)


        cv2.destroyAllWindows()
        out.release()
        cap.release()
        # Record the end time
        end_time = time.time()

        # Calculate the running time
        running_time = end_time - start_time
        detect_rate = success_time / frame_time

        return OUTPUT_PATH, trajectory, frame_size, running_time, detect_rate

    def process_frame_origin(self, img, trajectory):
        """
            use model to do one single frame to generate route and mask

            :argument frame, last frame finger position, finger list to detect
            :return img with route, current frame finger position
        """

        # uese mediepipe to detect image
        h, w = img.shape[0], img.shape[1]
        point_list = []
        right = None
        if self.model.modelIndex == 1:

            self.model.model.setFrame(img)

            currentTracker = 0
            for finger_index in range(len(self.drawList)):

                if self.drawList[finger_index]:

                    self.model.model.setCurrentIndex(currentTracker)

                    track_window = self.model.model.colourDetectSimple()
                    x, y, width, height = track_window

                    # Draw a rectangle around the tracked object
                    cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)
                    x = int(track_window[0] + track_window[2] / 2)
                    y = int(track_window[1] + track_window[3] / 2)

                    if x != -1:
                        this_point = [finger_index, x, y]
                        right = True
                    else:
                        right = False
                        if len(trajectory) == 0:
                            currentTracker += 1
                            continue
                        else:
                            this_point = trajectory[len(trajectory) - 1][finger_index]

                    if trajectory is None:
                        point_list.append(this_point)
                        currentTracker += 1
                        continue

                    point_list.append(this_point)

                    img = self.draw_image(trajectory, this_point, finger_index, img)

                    currentTracker += 1
                else:
                    point_list.append([finger_index, -1, -1])
        else:
            img = cv2.flip(img, 1)
            img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = self.model.model.hands.process(img_RGB)
            # collect data and generate route
            if results.multi_hand_landmarks and len(results.multi_handedness) == 2:
                right = True
                for hand_landmarks in range(len(results.multi_hand_landmarks)):

                    for i in [4, 8, 12, 16, 20]:

                        finger_position = results.multi_hand_landmarks[hand_landmarks].landmark[i]

                        cx = int(finger_position.x * w)
                        cy = int(finger_position.y * h)

                        this_point = [int(i / 4 - 1), cx, cy]

                        if trajectory is None:
                            point_list.append(this_point)
                            continue

                        point_list.append(this_point)

                        if self.drawList[int(hand_landmarks * 5 + i / 4 - 1)]:
                            img = self.draw_image(trajectory, this_point, int(hand_landmarks * 5 + i / 4 - 1), img)
            else:
                right = False
            img = cv2.flip(img, 1)
        return right, img, point_list

    def draw_image(self, trajectory, this_point, finger_index, img):
        """
            draw detect point and route to img

            :argument img, last point location, this point location
            :return img
        """
        size = len(trajectory)
        if size == 1:
            img = cv2.line(img, (trajectory[0][finger_index][1], trajectory[0][finger_index][2]),
                           (this_point[1], this_point[2]), (0, 255, 0), RADIOS_ROUTE)
        else:
            for i in range(1, len(trajectory)):
                img = cv2.line(img, (trajectory[i - 1][finger_index][1], trajectory[i - 1][finger_index][2]),
                               (trajectory[i][finger_index][1], trajectory[i][finger_index][2]), (0, 255, 0),
                               RADIOS_ROUTE)

        return img
