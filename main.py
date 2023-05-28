########################################################################
## QT GUI BY SPINN TV(YOUTUBE)
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
########################################################################
# IMPORT GUI FILE
import cv2
from PIL import Image, ImageQt

from Functions.Functions import Functions
from ui_interface import *

from PySide6.QtCore import Slot, QStandardPaths, QUrl, QDir
from PySide6.QtGui import QPixmap, QKeySequence, QIcon, QPen
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer, QMediaFormat
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QDialog, QStyle, QSlider, QListWidgetItem

########################################################################

messages = [
            "Click for left_1 finger .",
            "Click for left_2 finger.",
            "Click for left_3 finger.",
            "Click for left_4 finger.",
            "Click for left_5 finger.",
            "Click for right_1 finger.",
            "Click for right_2 finger.",
            "Click for right_3 finger.",
            "Click for right_4 finger.",
            "Click for right_5 finger.",
        ]

########################################################################


# INITIALIZE APP SETTINGS

########################################################################

AVI = "video/x-msvideo"  # AVI
MP4 = 'video/mp4'

def get_supported_mime_types():
    """
        :argument null
        :return list of all support video type

        get all support video type
    """
    result = []
    for f in QMediaFormat().supportedFileFormats(QMediaFormat.Decode):
        mime_type = QMediaFormat(f).mimeType()
        result.append(mime_type.name())
    return result


########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.functions = Functions()

        self.setUpLeftBtn()
        self.setUpPlayer()
        self.setUpToolBar()
        self.setUpBtn()
        self.setUpRightMenu()
        self.setUpSaveBtn()
        self.functions.detectVideo.model.setModelIndex(0)

        self.ui.begin.clicked.connect(self.beginBtn)
        # 选择finger的设置
        self.ui.fingerGroup.buttonToggled.connect(self.choose_finger)
        self.ui.modleGroup.buttonToggled.connect(self.choose_modle)
        self.ui.mediaPipe.setChecked(True)
        self.ui.file.clicked.connect(self.save_file)

        self.ui.frontMap.setMouseTracking(True)
        self.ui.frontMap.mousePressEvent = self.mousePressEvent
        self.ui.frontMap.mouseMoveEvent = self.mouseMoveEvent
        self.ui.frontMap.mouseReleaseEvent = self.mouseReleaseEvent

        self.first_frame = None
        self.selection_start = None
        self.selection_end = None
        self.drawRect = False

        self.changeState()

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()

    def beginBtn(self):
        self.generate(self.functions.isArray)
        self.functions.changeState()
        self.changeState()

    def setUpSaveBtn(self):
        self.ui.saveAreadyBtn.toggled.connect(self.sAlreadyBtn)
        self.ui.saveHotBtn.toggled.connect(self.sHotBtn)
        self.ui.saveHotRouteBtn.toggled.connect(self.sHotRouteBtn)
        self.ui.saveTacleFixationBtn.toggled.connect(self.sTacleFixationBtn)

    def sAlreadyBtn(self):
        if self.ui.saveAreadyBtn.isChecked():
            self.functions.drawings.setSaveAlready(True)
        else:
            self.functions.drawings.setSaveAlready(False)

    def sHotBtn(self):
        if self.ui.saveHotBtn.isChecked():
            self.functions.drawings.setSaveHot(True)
        else:
            self.functions.drawings.setSaveHot(False)

    def sHotRouteBtn(self):
        if self.ui.saveHotRouteBtn.isChecked():
            self.functions.drawings.setSaveHorRoute(True)
        else:
            self.functions.drawings.setSaveHorRoute(False)

    def sTacleFixationBtn(self):
        if self.ui.saveTacleFixationBtn.isChecked():
            self.functions.drawings.setSaveTacleRixation(True)
        else:
            self.functions.drawings.setSaveTacleRixation(False)

    def changeState(self):

        if self.functions.state == 0:
            self.ui.alreadyMapBtn.setEnabled(False)
            self.ui.hotMapBtn.setEnabled(False)
            self.ui.hotMapRouteBtn.setEnabled(False)
            self.ui.handSettingBtn.setEnabled(False)
            self.ui.modelCompareBtn.setEnabled(False)
            self.ui.modelSettingBtn.setEnabled(False)
            self.ui.tacicleFixationBtn.setEnabled(False)
        elif self.functions.state == 1:
            self.ui.modelSettingBtn.setEnabled(True)
            self.ui.handSettingBtn.setEnabled(True)
            self.ui.alreadyMapBtn.setEnabled(False)
            self.ui.hotMapBtn.setEnabled(False)
            self.ui.hotMapRouteBtn.setEnabled(False)
            self.ui.modelCompareBtn.setEnabled(False)
            self.ui.tacicleFixationBtn.setEnabled(False)
        elif self.functions.state == 2:
            self.ui.already.setEnabled(True)
            self.ui.hot.setEnabled(True)
        elif self.functions.state == 3:
            self.ui.hotRoute.setEnabled(True)
            self.ui.tacle.setEnabled(True)

    def setUpToolBar(self):
        # tool bar的相关设置
        style = self.style()
        icon = QIcon.fromTheme("media-playback-start.png",
                               style.standardIcon(QStyle.SP_MediaPlay))
        self.ui.playBtn.setIcon(icon)
        self.ui.playBtn.clicked.connect(self._player.play)

        icon = QIcon.fromTheme("media-skip-backward-symbolic.svg",
                               style.standardIcon(QStyle.SP_MediaSkipBackward))
        self.ui.previousBtn.setIcon(icon)
        self.ui.previousBtn.clicked.connect(self.previous_clicked)

        icon = QIcon.fromTheme("media-playback-pause.png",
                               style.standardIcon(QStyle.SP_MediaPause))
        self.ui.pauseBtn.setIcon(icon)
        self.ui.pauseBtn.clicked.connect(self._player.pause)

        icon = QIcon.fromTheme("media-skip-forward-symbolic.svg",
                               style.standardIcon(QStyle.SP_MediaSkipForward))
        self.ui.nextBtn.setIcon(icon)
        self.ui.nextBtn.clicked.connect(self.next_clicked)

        icon = QIcon.fromTheme("media-playback-stop.png",
                               style.standardIcon(QStyle.SP_MediaStop))
        self.ui.stopBtn.setIcon(icon)
        self.ui.stopBtn.clicked.connect(self._ensure_stopped)

        self.ui.openBtn.clicked.connect(self.open)

        self.ui.nextFingerBtn.clicked.connect(self.next_finger)
        self.ui.skipBtn.clicked.connect(self.skip_finger)

    def setUpRightMenu(self):

        self.ui.input.clicked.connect(self.get_files)

    def setUpPlayer(self):
        # 设置视频播放的相关设置
        self._mime_types = []
        self.functions.dealFile.setCurrentFile("")
        self._playlist = []  # FIXME 6.3: Replace by QMediaPlaylist?
        self._playlist_index = -1
        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)
        self._player.errorOccurred.connect(self._player_error)
        self._player.playbackStateChanged.connect(self.update_buttons)
        self._player.setVideoOutput(self.ui.player)
        self.update_buttons(self._player.playbackState())

    def setUpBtn(self):

        self.ui.hot.clicked.connect(self.img_hot_map)
        self.ui.already.clicked.connect(self.img_already)
        self.ui.hotRoute.clicked.connect(self.img_hot_route)
        self.ui.tacle.clicked.connect(self.img_tackel)
        self.ui.compare.clicked.connect(self.img_compare)

    def setUpLeftBtn(self):

        self.ui.alreadyMapBtn.clicked.connect(self.change_page_already)

        self.ui.playerBtn.clicked.connect(self.change_page_first)

        self.ui.hotMapRouteBtn.clicked.connect(self.change_page_hot_route)

        self.ui.hotMapBtn.clicked.connect(self.change_page_hot)

        self.ui.handSettingBtn.clicked.connect(self.change_page_hand_setting)

        self.ui.tacicleFixationBtn.clicked.connect(self.change_page_tactile)

        self.ui.modelCompareBtn.clicked.connect(self.change_page_compare)

        self.ui.modelSettingBtn.clicked.connect(self.change_page_model_setting)

    def unchange_btn(self, name):

        if name == 0:
            self.ui.playerBtn.setStyleSheet("background-color: #27263c;")
        elif name == 1:
            self.ui.alreadyMapBtn.setStyleSheet("background-color: #27263c;")
        elif name == 2:
            self.ui.hotMapBtn.setStyleSheet("background-color: #27263c;")
        elif name == 3:
            self.ui.hotMapRouteBtn.setStyleSheet("background-color: #27263c;")
        elif name == 4:
            self.ui.tacicleFixationBtn.setStyleSheet("background-color: #27263c;")
        elif name == 5:
            self.ui.modelCompareBtn.setStyleSheet("background-color: #27263c;")
        elif name == 6:
            self.ui.handSettingBtn.setStyleSheet("background-color: #27263c;")
        elif name == 7:
            self.ui.modelSettingBtn.setStyleSheet("background-color: #27263c;")

    def change_page_already(self):
        self.unchange_btn(self.functions.currentPage)
        self.functions.setCurrentPage(1)
        self.ui.alreadyMapBtn.setStyleSheet("font-weight:bold; background-color: #1b1b27;")
        self.ui.mainPages.setCurrentIndex(self.functions.currentPage)

    def change_page_first(self):
        self.unchange_btn(self.functions.currentPage)
        self.functions.setCurrentPage(0)
        self.ui.playerBtn.setStyleSheet("font-weight:bold; background-color: #1b1b27;")
        self.ui.mainPages.setCurrentIndex(self.functions.currentPage)

    def change_page_hot(self):
        self.unchange_btn(self.functions.currentPage)
        self.functions.setCurrentPage(2)
        self.ui.hotMapBtn.setStyleSheet("font-weight:bold; background-color: #1b1b27;")
        self.ui.mainPages.setCurrentIndex(self.functions.currentPage)

    def change_page_hot_route(self):
        self.unchange_btn(self.functions.currentPage)
        self.functions.setCurrentPage(3)
        self.ui.hotMapRouteBtn.setStyleSheet("font-weight:bold; background-color: #1b1b27;")
        self.ui.mainPages.setCurrentIndex(self.functions.currentPage)

    def change_page_tactile(self):
        self.unchange_btn(self.functions.currentPage)
        self.functions.setCurrentPage(5)
        self.ui.modelCompareBtn.setStyleSheet("font-weight:bold; background-color: #1b1b27;")
        self.ui.mainPages.setCurrentIndex(self.functions.currentPage)

    def change_page_compare(self):
        self.unchange_btn(self.functions.currentPage)
        self.functions.setCurrentPage(4)
        self.ui.tacicleFixationBtn.setStyleSheet("font-weight:bold; background-color: #1b1b27;")
        self.ui.mainPages.setCurrentIndex(self.functions.currentPage)

    def change_page_model_setting(self):
        self.unchange_btn(self.functions.currentPage)
        self.functions.setCurrentPage(7)
        self.ui.modelSettingBtn.setStyleSheet("font-weight:bold; background-color: #1b1b27;")
        self.ui.mainPages.setCurrentIndex(self.functions.currentPage)

    def change_page_hand_setting(self):
        self.unchange_btn(self.functions.currentPage)
        self.functions.setCurrentPage(6)
        self.ui.handSettingBtn.setStyleSheet("font-weight:bold; background-color: #1b1b27;")
        self.ui.mainPages.setCurrentIndex(self.functions.currentPage)

    def get_files(self):

        self.functions.setIsArray(True)
        self._ensure_stopped()
        self.functions.dealFile.clearFile()
        files_dialog = QFileDialog(self)

        dir_path = files_dialog.getExistingDirectory(None, "Select Directory", "/path/to/default/directory")
        files_list = self.functions.dealFile.getFileLocations(dir_path)

        if not len(files_list) == 0:
            for file_location in files_list:
                file_name = os.path.basename(file_location)
                list_item = QListWidgetItem(file_name)
                self.ui.listWidget.addItem(list_item)
        else:
            self.show_status_message("no valid files")

    def next_finger(self):

        if self.functions.currentFinger <= 8:
            self.change_finger_label()
            self.functions.setFingerList(self.functions.currentFinger, True)
            self.functions.setNeedToChooseFinger(True)
        else:
            self.ui.nextFingerBtn.setEnabled(False)
            self.ui.skipBtn.setEnabled(False)
            self.ui.fingerLabel.setText("Finish choosing colour!")
            self.functions.detectVideo.model.setRoiInist(self.functions.Rois)

    def skip_finger(self):

        if self.functions.currentFinger <= 8:
            self.change_finger_label()
            self.functions.setFingerList(self.functions.currentFinger, False)
            self.functions.setNeedToChooseFinger(False)
        else:
            self.ui.nextFingerBtn.setEnabled(False)
            self.ui.skipBtn.setEnabled(False)
            self.ui.fingerLabel.setText("Finish choosing colour!")
            self.functions.detectVideo.model.setRoiInist(self.functions.Rois)

    def change_finger_label(self):
        if self.functions.currentFinger <= 8:
            self.functions.addCurrentFinger()
            self.ui.fingerLabel.setText(messages[self.functions.currentFinger])

    def choose_modle(self):
        """
            select prefer model by the player, default is MediaPipe
        """
        if self.ui.mediaPipe.isChecked():
            self.functions.detectVideo.model.setModelIndex(0)
            self.closeFrontFrame()
            self.ui.skipBtn.setEnabled(False)
            self.ui.nextFingerBtn.setEnabled(False)
        else:
            self.functions.detectVideo.model.setModelIndex(1)
            self.open_first_frame()
            self.ui.skipBtn.setEnabled(True)
            self.ui.nextFingerBtn.setEnabled(True)

    def closeFrontFrame(self):
        self.ui.frontMap.clear()

    def mousePressEvent(self, event):

        if self.functions.needToChooseFinger and event.button() == Qt.LeftButton:

            self.selection_start = self.getImagePos(event.pos())
            self.selection_end = None
            self.drawRect = True


    def mouseMoveEvent(self, event):
        if self.drawRect:
            self.selection_end = self.getImagePos(event.pos())
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.drawRect:
            self.drawRect = False
            self.update()
            x , y, w, h = self.getROI()

            ratio_x = self.functions.frameSize[0] / self.functions.originalFrameSize[0]
            ratio_y = self.functions.frameSize[1] / self.functions.originalFrameSize[1]
            x /= ratio_x
            y /= ratio_x
            w /= ratio_x
            h /= ratio_x

            self.functions.setRoi(self.functions.currentFinger, (int(x), int(y), int(w), int(h)))

            self.show_pic(self.first_frame, 3)

    def getROI(self):
        left = min(self.selection_start.x(), self.selection_end.x())
        top = min(self.selection_start.y(), self.selection_end.y())
        width = abs(self.selection_start.x() - self.selection_end.x())
        height = abs(self.selection_start.y() - self.selection_end.y())
        return left, top, width, height

    def getImagePos(self, pos):
        pixmap_rect = self.ui.frontMap.pixmap().rect()
        label_rect = self.ui.frontMap.rect()

        if pixmap_rect.width() == label_rect.width():
            image_pos = QPoint(pos.x(), pos.y() - (label_rect.height() - pixmap_rect.height()) / 2)
        else:
            image_pos = QPoint(pos.x() - (label_rect.width() - pixmap_rect.width()) / 2, pos.y())
        print(image_pos)
        return image_pos

    def paintEvent(self, event):

        super().paintEvent(event)
        if self.selection_start and self.selection_end:
            self.modified_pixmap = self.ui.frontMap.pixmap().copy()  # Create a copy of the original pixmap
            rect = self.getROI()
            painter = QPainter(self.modified_pixmap)
            painter.setPen(QPen(QColor(255, 0, 0, 100), 2))  # Set a transparent red color
            painter.setBrush(QColor(255, 0, 0, 50))
            painter.drawRect(rect[0], rect[1], rect[2],
                             rect[3])
            painter.end()

            self.ui.frontMap.setPixmap(self.modified_pixmap)


    def open_first_frame(self):

        video = cv2.VideoCapture(self.functions.dealFile.currentFile.toString())

        ret, frame = video.read()

        if ret:

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.first_frame = rgb_frame
            self.functions.setOriginalFrameSize((int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))))
            self.functions.detectVideo.model.setFirstFrame(frame)
            self.show_pic(rgb_frame, 3)

    def get_new_file_name(self, name):
        temp_name = self.functions.dealFile.fileName.split(".")
        new_name = ''
        new_name += temp_name[0] + '_' + name + ".png"

        return new_name
    @Slot()
    def img_already(self):

        self.functions.drawAlready.setDrawList(self.functions.fingerList)
        self.functions.drawAlready.setFrameSize(self.functions.frameSize)
        self.functions.drawAlready.setRoute(self.functions.routeList[self.functions.dealFile.currentIndex])
        self.functions.drawAlready.setFileName(self.get_new_file_name('already'))
        self.already_pic = self.functions.drawAlready.drawAlready()
        self.functions.drawings.setAlready(self.already_pic)
        self.show_pic(self.already_pic, 0)
        self.ui.alreadyMapBtn.setEnabled(True)

    def img_hot_map(self):
        """
            generate hot map and produce it into a new windows
        """
        self.functions.drawHeat.setDrawList(self.functions.fingerList)
        self.functions.drawHeat.setFrameSize(self.functions.frameSize)
        self.functions.drawHeat.setRoute(self.functions.routeList[self.functions.dealFile.currentIndex])
        self.functions.drawHeat.setFileName(self.get_new_file_name('heat'))
        self.heat_map = self.functions.drawHeat.hotDraw()
        self.functions.drawings.setHot(self.heat_map)
        self.show_pic(self.heat_map, 1)
        self.ui.hotMapBtn.setEnabled(True)

        self.functions.changeState()
        self.changeState()

    def img_hot_route(self):

        self.heat_route = self.functions.drawHeat.calculateHot(self.functions.drawings.hotMapPic)
        self.show_pic(self.heat_route, 2)
        self.ui.hotMapRouteBtn.setEnabled(True)

    def img_tackel(self):

        self.functions.drawTacle.setFrameSize(self.functions.frameSize)
        self.functions.drawHeat.setFileName(self.get_new_file_name('tacle'))
        self.functions.drawTacle.addImgList(self.functions.drawings.hotMapPic)
        self.tackle_pic = self.functions.drawTacle.getTacleImg()
        self.show_pic(self.tackle_pic, 4)
        self.ui.tacicleFixationBtn.setEnabled(True)

    def img_compare(self):
        pass

    def show_pic(self, map, name):

        qimg = None
        if name != 3:
            label_size = self.ui.alreadyMapPage.size()
            qimg = QPixmap.fromImage(ImageQt.ImageQt(Image.fromarray(map))).scaled(label_size, Qt.KeepAspectRatio)

        if name == 0:
            self.ui.alreadyMap.setPixmap(qimg)
        elif name == 1:
            self.ui.hotMap.setPixmap(qimg)
        elif name == 2:
            self.ui.hotMapRoute.setPixmap(qimg)
        elif name == 3:
            label_size = self.ui.frontMap.size()
            qimg = QPixmap.fromImage(ImageQt.ImageQt(Image.fromarray(map))).scaled(label_size, Qt.KeepAspectRatio)
            self.ui.frontMap.setPixmap(qimg)
            size = self.ui.frontMap.size()
            self.functions.setFrameSize((size.width(), size.height()))
        elif name == 4:
            self.ui.tacleMap.setPixmap(qimg)

    # 关闭
    def closeEvent(self, event):
        self._ensure_stopped()
        event.accept()

    @Slot()
    def choose_finger(self):

        # 好蠢 但没想到什么好的办法 exec 好像不行，self是一个实例变量
        if self.ui.left_1.isChecked():
            self.functions.setFingerList(0, True)
        else:
            self.functions.setFingerList(0, False)

        if self.ui.left_2.isChecked():
            self.functions.setFingerList(1, True)
        else:
            self.functions.setFingerList(1, False)

        if self.ui.left_3.isChecked():
            self.functions.setFingerList(2, True)
        else:
            self.functions.setFingerList(2, False)

        if self.ui.left_4.isChecked():
            self.functions.setFingerList(3, True)
        else:
            self.functions.setFingerList(3, False)

        if self.ui.left_5.isChecked():
            self.functions.setFingerList(4, True)
        else:
            self.functions.setFingerList(4, False)

        if self.ui.right_1.isChecked():
            self.functions.setFingerList(5, True)
        else:
            self.functions.setFingerList(5, False)

        if self.ui.right_2.isChecked():
            self.functions.setFingerList(6, True)
        else:
            self.functions.setFingerList(6, False)

        if self.ui.right_3.isChecked():
            self.functions.setFingerList(7, True)
        else:
            self.functions.setFingerList(7, False)

        if self.ui.right_4.isChecked():
            self.functions.setFingerList(8, True)
        else:
            self.functions.setFingerList(8, False)

        if self.ui.right_5.isChecked():
            self.functions.setFingerList(9, True)
        else:
            self.functions.setFingerList(9, False)

    @Slot()
    def open(self):
        """
            open new video and detect
        """

        self._ensure_stopped()
        self.functions.setIsArray(False)
        file_dialog = QFileDialog(self)

        is_windows = sys.platform == 'win32'
        if not self._mime_types:
            self._mime_types = get_supported_mime_types()
            if (is_windows and AVI not in self._mime_types):
                self._mime_types.append(AVI)
            elif MP4 not in self._mime_types:
                self._mime_types.append(MP4)

        file_dialog.setMimeTypeFilters(self._mime_types)

        default_mimetype = AVI if is_windows else MP4
        if default_mimetype in self._mime_types:
            file_dialog.selectMimeTypeFilter(default_mimetype)

        movies_location = QStandardPaths.writableLocation(QStandardPaths.MoviesLocation)
        file_dialog.setDirectory(movies_location)
        if file_dialog.exec() == QDialog.Accepted:
            url = file_dialog.selectedUrls()[0]

            self.functions.dealFile.setCurrentFile(url)
            self._playlist.append(url)
            self._playlist_index = len(self._playlist) - 1

        self.functions.changeState()
        self.changeState()

    @Slot()
    def _ensure_stopped(self):
        if self._player.playbackState() != QMediaPlayer.StoppedState:
            self._player.stop()

    @Slot()
    def previous_clicked(self):
        # Go to previous track if we are within the first 5 seconds of playback
        # Otherwise, seek to the beginning.
        if self._player.position() <= 5000 and self._playlist_index > 0:
            self._playlist_index -= 1
            self._playlist.previous()
            self._player.setSource(self._playlist[self._playlist_index])
        else:
            self._player.setPosition(0)

    def generate_new_path(self):
        path = self.functions.dealFile.currentFile.toString().split('/')
        new_path = ''
        name = ''
        for i in range(len(path)):

            if i <= 2:
                pass
            elif i != len(path) - 1:
                new_path += path[i] + '/'
            else:
                new_path += path[i]
                name = path[i]
        return new_path, name

    def generate_new_url(self):

        current_path = os.path.abspath(__file__)
        path = current_path.split('\\')
        current_path = ''
        for i in range(len(path)):
            if i != len(path) - 1:
                current_path += path[i] + '\\'

        return current_path

    def set_up_new_play(self, current_path):
        newQurl = QUrl.fromLocalFile(current_path)

        self._ensure_stopped()
        self.currentUrl = newQurl
        self._playlist.append(newQurl)
        self._playlist_index = len(self._playlist) - 1
        self._player.setSource(newQurl)
        self._player.play()

    @Slot()
    def generate(self, bath):

        if not bath:
            newPath, newName = self.generate_new_path()
            current_path = self.generate_new_url()
            self.functions.detectVideo.setPath(newPath)
            self.functions.detectVideo.setDrawList(self.functions.fingerList)
            new_url, route, frame_size = self.functions.detectVideo.generate_video()
            current_path += new_url

            self.functions.dealFile.setFileName(newName)
            self.functions.dealFile.setCurrentFile(current_path)
            self.functions.addRoute(route)
            self.functions.setFrameSize(frame_size)
            self.set_up_new_play(current_path)
        else:
            
            new_url, route, frame_size = self.functions.detectVideo.generate_video()
            self.functions.dealFile.setCurrentFile(new_url)
            self.functions.addRoute(route)
            self.functions.setFrameSize(frame_size)

    @Slot()
    def next_clicked(self):
        if self._playlist_index < len(self._playlist) - 1:
            self._playlist_index += 1
            self._player.setSource(self._playlist[self._playlist_index])

    @Slot("QMediaPlayer::PlaybackState")
    def update_buttons(self, state):
        media_count = len(self._playlist)
        self.ui.playBtn.setEnabled(media_count > 0
                                        and state != QMediaPlayer.PlayingState)
        self.ui.pauseBtn.setEnabled(state == QMediaPlayer.PlayingState)
        self.ui.stopBtn.setEnabled(state != QMediaPlayer.StoppedState)
        self.ui.previousBtn.setEnabled(self._player.position() > 0)
        self.ui.nextBtn.setEnabled(media_count > 1)

    def show_status_message(self, message):
        self.statusBar().showMessage(message, 5000)

    @Slot("QMediaPlayer::Error", str)
    def _player_error(self, error, error_string):
        print(error_string, file=sys.stderr)
        self.show_status_message(error_string)

    def save_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(
            None, "Save File", "", "All Files (*);;Text Files (*.txt)", options=options
        )
        if file_path:

            self.functions.setFilePath(file_path)

########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
########################################################################
## END===>
########################################################################
