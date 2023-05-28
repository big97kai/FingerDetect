'''
    @FileName:Drawings.py
    @Author:yikai yang
    @Date:2023/5/27
    @Desc:Null
'''
class Drawings():
    def __init__(self):
        self.saveAlready = False
        self.saveHot = False
        self.saveHotRoute = False
        self.saveTacleFixation = False

        self.alreadyPic = None
        self.hotMapPic = None
        self.hotMapRoutePic = None
        self.tacleFixation = None

    def setSaveAlready(self, boolean):
        self.saveAlready = boolean

    def setSaveHot(self, boolean):
        self.saveHot = boolean

    def setSaveHotRoute(self, boolean):
        self.saveHotRoute = boolean

    def setSaveTacleRixation(self, boolean):
        self.tacleFixation = boolean

    def setAlready(self, pic):
        self.alreadyPic = pic

    def setHot(self, pic):
        self.hotMapPic = pic

    def setHotRoute(self, pic):
        self.hotMapRoutePic = pic

    def setTacleRixation(self, pic):
        self.tacleFixation = pic