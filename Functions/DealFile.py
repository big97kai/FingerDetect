'''
    @FileName:DealFile.py
    @Author:yikai yang
    @Date:2023/5/28
    @Desc:Null
'''
class DealFile:
    def __init__(self):
        self.currentIndex = 0
        self.currentFile = ""
        self.fileName = ""

    def setCurrentFile(self, currentFile):
        self.currentFile = currentFile

    def clearFile(self):
        self.currentFile = ""

    def setFileName(self, fileName):
        self.fileName = fileName

    def addIndex(self):
        self.currentIndex += 1

    def resetIndex(self):
        self.currentIndex = 0