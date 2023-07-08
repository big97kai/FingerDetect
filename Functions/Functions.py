'''
    @FileName:Functions.py
    @Author:yikai yang
    @Date:2023/4/14
    @Desc:Null
'''
from Functions.Compare import Compare
from Functions.DealArray import DealArray
from Functions.DealSingle import DealSingle
from Functions.DetectImage import DetectImage
from Functions.DetectVideo import DetectVideo
from Functions.DrawAlready import DrawAlready
from Functions.DrawHeat import DrawHeat
from Functions.DrawListTacle import DrawListTacle
from Functions.DrawTacle import DrawTacle
from Functions.Drawings import Drawings


class Functions():

    def __init__(self):
        self.detectVideo = DetectVideo()
        self.dealFile = DealSingle()
        self.drawAlready = DrawAlready()
        self.drawHeat = DrawHeat()
        self.drawTacle = DrawTacle()
        self.drawTacleList = DrawListTacle()
        self.drawings = Drawings()
        self.compare = Compare()

        self.currentPage = 0

        self.currentFinger = -1
        self.needToChooseFinger = False
        self.fingerList = [False, False, False, False, False,
                           False, False, False, False, False]
        self.Rois = [(-1, -1, -1, -1), (-1, -1, -1, -1), (-1, -1, -1, -1), (-1, -1, -1, -1), (-1, -1, -1, -1),
                     (-1, -1, -1, -1), (-1, -1, -1, -1), (-1, -1, -1, -1), (-1, -1, -1, -1), (-1, -1, -1, -1)]

        self.routeList = []

        self.frameSize = None
        self.originalFrameSize = None

        self.modelIndex = 0

        self.state = 0

        self.isArray = False

        self.hasUsedModel = [False, False]

        self.prePath = '\out\\'

        self.tacleList = [-1, -1]

        self.alreadyDone = []

    def setTacle(self, index, img):
        self.tacleList[index] = img

    def setHasUsedModel(self, index):
        self.hasUsedModel[index] = True

    def testAllModel(self):
        for hasUsed in self.hasUsedModel:

            if not hasUsed:
                return False

        return True

    def testFingerList(self):

        for boolean in self.fingerList:

            if boolean:
                return True

        return False

    def setRoi(self, index, roi):
        self.Rois[index] = roi

    def setOriginalFrameSize(self, frameSize):
        self.originalFrameSize = frameSize

    def setFrameSize(self, frameSize):
        self.frameSize = frameSize

    def setIsArray(self, boolean):
        self.isArray = boolean
        if self.isArray:
            self.dealFile = DealArray()
        else:
            self.dealFile = DealSingle()

    def setModelIndex(self, index):
        self.modelIndex = index

    def setSaveFilePath(self, file):
        self.prePath = file

    def setNeedToChooseFinger(self, boolean):
        self.needToChooseFinger = boolean

    def changeState(self):

        if self.state == 0:
            if self.dealFile.currentFile or self.isArray:
                self.state = 1
            return

        if self.state == 1:
            if self.routeList is not []:
                self.state = 2
            return

        if self.state == 2:
            if self.drawings.hotMapPic is not []:
                self.state = 3

    def setCurrentPage(self, pageIndex):
        self.currentPage = pageIndex

    def setFingerList(self, index, isBool):
        self.fingerList[index] = isBool

    def addCurrentFinger(self):
        self.currentFinger += 1

    def setInitialFinger(self):
        self.currentFinger = 0

    def addRoute(self, route):
        self.routeList.append(route)

    def clearAll(self):
        self.frameSize = None
        self.needToChooseFinger = False

        self.fingerList = [False, False, False, False, False,
                           False, False, False, False, False]

        self.routeList = []
        self.currentFinger = 0

    def testTwoModelFingerList(self):

        for fingerIndex in range(len(self.fingerList)):

            if self.fingerList[fingerIndex] != self.alreadyDone[fingerIndex]:

                return False

        return True