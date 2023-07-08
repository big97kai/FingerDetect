'''
    @FileName:DrawImg.py
    @Author:yikai yang
    @Date:2023/5/26
    @Desc:Null
'''
import cv2

COLOUR_ROUTE = (255, 0, 0)
RADIOS_ROUTE = 2

class DrawImg:
    """
            the base class for all drawing image incling save files
    """

    def __init__(self, drawList=None, frameSize=None, route=None, fileName=None):
        self.fileName = fileName
        self.drawList = drawList
        self.frameSize = frameSize
        self.route = route

    def setNeedToSave(self, needToSave):
        self.needToSave = needToSave

    def setFileName(self, fileName):
        self.fileName = fileName

    def setDrawList(self, drawList):
        self.drawList = drawList

    def setRoute(self, route):
        self.route = route

    def setFrameSize(self, frameSize):
        self.frameSize = frameSize

    def saveImg(self, filePath, img):
        # Save the image to the specified file location

        filePath = filePath + '//' + self.fileName
        cv2.imwrite(filePath, img)

    def drawRoute(self, img, before_point, route_list, permission):
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
