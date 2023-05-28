'''
    @FileName:DrawAlready.py
    @Author:yikai yang
    @Date:2023/5/26
    @Desc:Null
'''
import numpy as np

from Functions.DrawImg import DrawImg


class DrawAlready(DrawImg):
    def __init__(self):
        super(DrawAlready, self).__init__()

    def drawAlready(self):
        """
            draw already pass area

            :argument left hand data, right hand data, which finger to draw, frame
            :return img
        """
        img_blank = np.zeros((int(self.frameSize[1]), int(self.frameSize[0]), 3), np.uint8)
        img_blank[:] = [255, 255, 255]
        before_point = None
        for i in range(len(self.drawList)):
            if self.drawList[i]:
                img_blank, before_point = self.drawRoute(img_blank, before_point, self.route, i)

        return img_blank
