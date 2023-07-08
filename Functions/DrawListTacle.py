'''
    @FileName:DrawListTacle.py
    @Author:yikai yang
    @Date:2023/6/8
    @Desc:Null
'''
import cv2
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from Functions.DrawImg import DrawImg

DISTANCCE = 10
WINDOWSSIZE = 20  # Number of positions to consider in each window
THRESHOLD = 2.5

CIRCLE_RADIUS = 10
CIRCLE_COLOR = (0, 0, 255)  # Red color in BGR format
CIRCLE_THICKNESS = 2
COLOUR_ROUTE = 5
RADIOS_ROUTE = 5

class DrawListTacle(DrawImg):

    def __init__(self):
        super(DrawListTacle, self).__init__()
        self.imgList = [[], [], [], [], [],
                        [], [], [], [], []]

    def check_position_stability(self, image, fingerIndex):
        points = self.imgList[fingerIndex]
        points_array = np.array(points)

        # Scale the data for better clustering performance
        scaler = StandardScaler()
        points_scaled = scaler.fit_transform(points_array)

        # Perform DBSCAN clustering
        dbscan = DBSCAN(eps=1, min_samples=2)  # Adjust the parameters as needed
        dbscan.fit(points_scaled)

        # Get the cluster labels assigned to each point
        cluster_labels = dbscan.labels_

        # Get the number of clusters (excluding noise points)
        num_clusters = len(set(cluster_labels)) - (1 if -1 in cluster_labels else 0)

        # Calculate the cluster centers
        cluster_centers = []
        for i in range(num_clusters):
            cluster_points = points_array[cluster_labels == i]
            cluster_center = np.mean(cluster_points, axis=0)
            cluster_centers.append(cluster_center)
            cv2.circle(image, (int(cluster_center[0]), int(cluster_center[1])), CIRCLE_RADIUS, CIRCLE_COLOR)



    def addPointToList(self, fingerIndex, position):

        self.imgList[fingerIndex].append(position)

    def checkIfNear(self):
        print(self.imgList)
        h = self.frameSize[1]
        w = self.frameSize[0]
        zombies = np.ones((int(h), int(w), 3), dtype=np.uint8) * 255

        for fingerIndex in range(len(self.imgList)):

            if self.drawList[fingerIndex]:
                self.check_position_stability(zombies, fingerIndex)

        cv2.imwrite("listTacle.jpg", zombies)
        self.imgList = [[], [], [], [], [],
                        [], [], [], [], []]
        return zombies.astype(np.uint8)