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
RADIOS_ROUTE = 10
DISTANCETHRESHOLD = 5

class DrawHeat(DrawImg):
    def __init__(self):
        super(DrawHeat, self).__init__()

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

