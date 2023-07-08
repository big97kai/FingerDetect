'''
    @FileName:DealArray.py
    @Author:yikai yang
    @Date:2023/5/15
    @Desc:Null
'''
import os

from PySide6.QtWidgets import QFileDialog
from Functions.DealFile import DealFile

class DealArray(DealFile):

    def __init__(self):
        super(DealArray, self).__init__()
        self.filesPath = []
        self.filesName = []

    def addCurrentIndex(self):

        if self.currentIndex != len(self.filesPath)-1:
            self.currentIndex += 1
        else:
            self.currentIndex = 0

    def addFile(self, file):
        self.filesPath.append(file)

    def addFileName(self, fileName):
        self.filesName.append(fileName)

    def deleteFile(self, file):
        self.filesPath.remove(file)

    def isVideoFile(self, file_path):
        video_extensions = ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm']
        extension = os.path.splitext(file_path)[1].lower()
        return extension in video_extensions

    def clearFile(self):
        self.currentFile = ""
        self.filesPath.clear()
        self.filesName.clear()

    def getFileLocations(self, directory):

        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path) and self.isVideoFile(file_path):

                list = self.changeFile(file_path)
                self.filesPath.append(list)
            else:
                self.clearFile()
                return []

        return self.filesPath

    def changeFile(self, file):

        list = file.split("\\")
        return list[0] + "/" + list[1]
