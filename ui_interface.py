# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import QSS_Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(797, 471)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget, #playerBtn, #mainBodyContent{\n"
"	background-color: #1b1b27;\n"
"}\n"
"#header, #mainBody{\n"
"	background-color: #27263c;\n"
"}\n"
"\n"
"#files{\n"
"	border:1px solid #cc5bce;\n"
"	border-radius: 12px;\n"
"	text-align:center;\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align:left;\n"
"	padding:5px 8px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#playerBtn{\n"
"	font-weight:bold;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftFrame = QFrame(self.header)
        self.leftFrame.setObjectName(u"leftFrame")
        self.leftFrame.setFrameShape(QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.leftFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 9, -1, -1)
        self.leftMenuBtn = QPushButton(self.leftFrame)
        self.leftMenuBtn.setObjectName(u"leftMenuBtn")
        self.leftMenuBtn.setEnabled(False)
        self.leftMenuBtn.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon()
        icon.addFile(u":/icons/Icons/align-center.png", QSize(), QIcon.Normal, QIcon.Off)
        self.leftMenuBtn.setIcon(icon)
        self.leftMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.leftMenuBtn, 0, Qt.AlignLeft)

        self.label = QLabel(self.leftFrame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe Script"])
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.label, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.leftFrame, 0, Qt.AlignLeft)

        self.volumeFrame = QFrame(self.header)
        self.volumeFrame.setObjectName(u"volumeFrame")
        self.volumeFrame.setFrameShape(QFrame.StyledPanel)
        self.volumeFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.volumeFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.openBtn = QPushButton(self.volumeFrame)
        self.openBtn.setObjectName(u"openBtn")

        self.horizontalLayout_5.addWidget(self.openBtn)

        self.playBtn = QPushButton(self.volumeFrame)
        self.playBtn.setObjectName(u"playBtn")

        self.horizontalLayout_5.addWidget(self.playBtn)

        self.previousBtn = QPushButton(self.volumeFrame)
        self.previousBtn.setObjectName(u"previousBtn")

        self.horizontalLayout_5.addWidget(self.previousBtn)

        self.pauseBtn = QPushButton(self.volumeFrame)
        self.pauseBtn.setObjectName(u"pauseBtn")

        self.horizontalLayout_5.addWidget(self.pauseBtn)

        self.nextBtn = QPushButton(self.volumeFrame)
        self.nextBtn.setObjectName(u"nextBtn")

        self.horizontalLayout_5.addWidget(self.nextBtn)

        self.stopBtn = QPushButton(self.volumeFrame)
        self.stopBtn.setObjectName(u"stopBtn")

        self.horizontalLayout_5.addWidget(self.stopBtn)


        self.horizontalLayout.addWidget(self.volumeFrame)

        self.rightFrame = QFrame(self.header)
        self.rightFrame.setObjectName(u"rightFrame")
        self.rightFrame.setFrameShape(QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.rightFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.begin = QPushButton(self.rightFrame)
        self.begin.setObjectName(u"begin")
        self.begin.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/instagram.png", QSize(), QIcon.Normal, QIcon.Off)
        self.begin.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.begin)

        self.reset = QPushButton(self.rightFrame)
        self.reset.setObjectName(u"reset")
        self.reset.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/corner-up-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reset.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.reset)

        self.file = QPushButton(self.rightFrame)
        self.file.setObjectName(u"file")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/file-text.png", QSize(), QIcon.Normal, QIcon.Off)
        self.file.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.file)

        self.input = QPushButton(self.rightFrame)
        self.input.setObjectName(u"input")
        self.input.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/file-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.input.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.input)

        self.files = QPushButton(self.rightFrame)
        self.files.setObjectName(u"files")
        self.files.setEnabled(False)
        self.files.setMinimumSize(QSize(38, 38))
        self.files.setMaximumSize(QSize(38, 38))
        self.files.setCursor(QCursor(Qt.ArrowCursor))
        self.files.setIcon(icon3)
        self.files.setIconSize(QSize(32, 32))
        self.files.setCheckable(False)
        self.files.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.files)


        self.horizontalLayout.addWidget(self.rightFrame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.mainBody.setMinimumSize(QSize(797, 409))
        self.horizontalLayout_2 = QHBoxLayout(self.mainBody)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.leftMenu = QWidget(self.mainBody)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(200, 0))
        self.verticalLayout_3 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.leftMenu)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(182, 381))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(8, 0, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.playerBtn = QPushButton(self.frame)
        self.playerBtn.setObjectName(u"playerBtn")
        self.playerBtn.setCursor(QCursor(Qt.OpenHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/play-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playerBtn.setIcon(icon5)

        self.verticalLayout_5.addWidget(self.playerBtn)

        self.alreadyMapBtn = QPushButton(self.frame)
        self.alreadyMapBtn.setObjectName(u"alreadyMapBtn")
        self.alreadyMapBtn.setEnabled(False)
        self.alreadyMapBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/map.png", QSize(), QIcon.Normal, QIcon.Off)
        self.alreadyMapBtn.setIcon(icon6)

        self.verticalLayout_5.addWidget(self.alreadyMapBtn)

        self.hotMapBtn = QPushButton(self.frame)
        self.hotMapBtn.setObjectName(u"hotMapBtn")
        self.hotMapBtn.setEnabled(False)
        self.hotMapBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/arrow-down-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hotMapBtn.setIcon(icon7)

        self.verticalLayout_5.addWidget(self.hotMapBtn)

        self.hotMapRouteBtn = QPushButton(self.frame)
        self.hotMapRouteBtn.setObjectName(u"hotMapRouteBtn")
        self.hotMapRouteBtn.setEnabled(False)
        self.hotMapRouteBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/Icons/crop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hotMapRouteBtn.setIcon(icon8)

        self.verticalLayout_5.addWidget(self.hotMapRouteBtn)


        self.verticalLayout_4.addWidget(self.frame)

        self.tacicleFixationBtn = QPushButton(self.widget)
        self.tacicleFixationBtn.setObjectName(u"tacicleFixationBtn")
        self.tacicleFixationBtn.setEnabled(False)
        icon9 = QIcon()
        icon9.addFile(u":/icons/Icons/airplay.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tacicleFixationBtn.setIcon(icon9)

        self.verticalLayout_4.addWidget(self.tacicleFixationBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.modelCompareBtn = QPushButton(self.frame_2)
        self.modelCompareBtn.setObjectName(u"modelCompareBtn")
        self.modelCompareBtn.setEnabled(False)
        self.modelCompareBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/command.png", QSize(), QIcon.Normal, QIcon.Off)
        self.modelCompareBtn.setIcon(icon10)

        self.verticalLayout_6.addWidget(self.modelCompareBtn)

        self.modelSettingBtn = QPushButton(self.frame_2)
        self.modelSettingBtn.setObjectName(u"modelSettingBtn")
        self.modelSettingBtn.setEnabled(False)
        self.modelSettingBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/Icons/more-horizontal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.modelSettingBtn.setIcon(icon11)

        self.verticalLayout_6.addWidget(self.modelSettingBtn)

        self.handSettingBtn = QPushButton(self.frame_2)
        self.handSettingBtn.setObjectName(u"handSettingBtn")
        self.handSettingBtn.setEnabled(False)
        self.handSettingBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/Icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.handSettingBtn.setIcon(icon12)

        self.verticalLayout_6.addWidget(self.handSettingBtn)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_2.addWidget(self.leftMenu)

        self.mainBodyContent = QWidget(self.mainBody)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        self.verticalLayout_2 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mainPages = QStackedWidget(self.mainBodyContent)
        self.mainPages.setObjectName(u"mainPages")
        font1 = QFont()
        font1.setPointSize(12)
        self.mainPages.setFont(font1)
        self.playerPage = QWidget()
        self.playerPage.setObjectName(u"playerPage")
        self.gridLayout = QGridLayout(self.playerPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.playerFrame = QFrame(self.playerPage)
        self.playerFrame.setObjectName(u"playerFrame")
        self.playerFrame.setFrameShape(QFrame.StyledPanel)
        self.playerFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.playerFrame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.playerFrame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMinimumSize(QSize(0, 30))
        self.frame_5.setBaseSize(QSize(0, 40))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.already = QPushButton(self.frame_5)
        self.already.setObjectName(u"already")

        self.horizontalLayout_6.addWidget(self.already)

        self.hot = QPushButton(self.frame_5)
        self.hot.setObjectName(u"hot")

        self.horizontalLayout_6.addWidget(self.hot)

        self.hotRoute = QPushButton(self.frame_5)
        self.hotRoute.setObjectName(u"hotRoute")
        self.hotRoute.setBaseSize(QSize(100, 20))

        self.horizontalLayout_6.addWidget(self.hotRoute)

        self.tacle = QPushButton(self.frame_5)
        self.tacle.setObjectName(u"tacle")

        self.horizontalLayout_6.addWidget(self.tacle)

        self.compare = QPushButton(self.frame_5)
        self.compare.setObjectName(u"compare")

        self.horizontalLayout_6.addWidget(self.compare)


        self.verticalLayout_13.addWidget(self.frame_5)

        self.player = QVideoWidget(self.playerFrame)
        self.player.setObjectName(u"player")
        sizePolicy.setHeightForWidth(self.player.sizePolicy().hasHeightForWidth())
        self.player.setSizePolicy(sizePolicy)

        self.verticalLayout_13.addWidget(self.player)


        self.gridLayout.addWidget(self.playerFrame, 0, 0, 1, 1)

        self.mainPages.addWidget(self.playerPage)
        self.alreadyMapPage = QWidget()
        self.alreadyMapPage.setObjectName(u"alreadyMapPage")
        self.verticalLayout_10 = QVBoxLayout(self.alreadyMapPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.alreadyMap = QLabel(self.alreadyMapPage)
        self.alreadyMap.setObjectName(u"alreadyMap")

        self.verticalLayout_10.addWidget(self.alreadyMap)

        self.mainPages.addWidget(self.alreadyMapPage)
        self.hotMapPage = QWidget()
        self.hotMapPage.setObjectName(u"hotMapPage")
        self.verticalLayout_11 = QVBoxLayout(self.hotMapPage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.hotMap = QLabel(self.hotMapPage)
        self.hotMap.setObjectName(u"hotMap")

        self.verticalLayout_11.addWidget(self.hotMap)

        self.mainPages.addWidget(self.hotMapPage)
        self.hotMapRoutePage = QWidget()
        self.hotMapRoutePage.setObjectName(u"hotMapRoutePage")
        self.verticalLayout_12 = QVBoxLayout(self.hotMapRoutePage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.hotMapRoute = QLabel(self.hotMapRoutePage)
        self.hotMapRoute.setObjectName(u"hotMapRoute")

        self.verticalLayout_12.addWidget(self.hotMapRoute)

        self.mainPages.addWidget(self.hotMapRoutePage)
        self.modelComparePage = QWidget()
        self.modelComparePage.setObjectName(u"modelComparePage")
        self.frame_9 = QFrame(self.modelComparePage)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(50, 100, 168, 66))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.chartTime = QWidget(self.frame_10)
        self.chartTime.setObjectName(u"chartTime")

        self.verticalLayout_16.addWidget(self.chartTime)

        self.tacleForColour = QLabel(self.frame_10)
        self.tacleForColour.setObjectName(u"tacleForColour")

        self.verticalLayout_16.addWidget(self.tacleForColour)


        self.horizontalLayout_9.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_11)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.chartCorrect = QWidget(self.frame_11)
        self.chartCorrect.setObjectName(u"chartCorrect")

        self.verticalLayout_17.addWidget(self.chartCorrect)

        self.tacleForMedia = QLabel(self.frame_11)
        self.tacleForMedia.setObjectName(u"tacleForMedia")

        self.verticalLayout_17.addWidget(self.tacleForMedia)


        self.horizontalLayout_9.addWidget(self.frame_11)

        self.mainPages.addWidget(self.modelComparePage)
        self.tacicleFixationPage = QWidget()
        self.tacicleFixationPage.setObjectName(u"tacicleFixationPage")
        self.frame_8 = QFrame(self.tacicleFixationPage)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(130, 140, 120, 80))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.tacleMap = QLabel(self.frame_8)
        self.tacleMap.setObjectName(u"tacleMap")
        self.tacleMap.setGeometry(QRect(50, 40, 54, 12))
        self.mainPages.addWidget(self.tacicleFixationPage)
        self.handSettingPage = QWidget()
        self.handSettingPage.setObjectName(u"handSettingPage")
        self.verticalLayout_9 = QVBoxLayout(self.handSettingPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.fingerFrame = QFrame(self.handSettingPage)
        self.fingerFrame.setObjectName(u"fingerFrame")
        self.fingerFrame.setFrameShape(QFrame.StyledPanel)
        self.fingerFrame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.fingerFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.left_1 = QCheckBox(self.fingerFrame)
        self.fingerGroup = QButtonGroup(MainWindow)
        self.fingerGroup.setObjectName(u"fingerGroup")
        self.fingerGroup.setExclusive(False)
        self.fingerGroup.addButton(self.left_1)
        self.left_1.setObjectName(u"left_1")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.left_1)

        self.left_2 = QCheckBox(self.fingerFrame)
        self.fingerGroup.addButton(self.left_2)
        self.left_2.setObjectName(u"left_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.left_2)

        self.left_3 = QCheckBox(self.fingerFrame)
        self.fingerGroup.addButton(self.left_3)
        self.left_3.setObjectName(u"left_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.left_3)

        self.left_4 = QCheckBox(self.fingerFrame)
        self.fingerGroup.addButton(self.left_4)
        self.left_4.setObjectName(u"left_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.left_4)

        self.left_5 = QCheckBox(self.fingerFrame)
        self.fingerGroup.addButton(self.left_5)
        self.left_5.setObjectName(u"left_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.left_5)

        self.right_1 = QCheckBox(self.fingerFrame)
        self.fingerGroup.addButton(self.right_1)
        self.right_1.setObjectName(u"right_1")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.right_1)

        self.right_2 = QCheckBox(self.fingerFrame)
        self.fingerGroup.addButton(self.right_2)
        self.right_2.setObjectName(u"right_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.right_2)

        self.right_3 = QCheckBox(self.fingerFrame)
        self.fingerGroup.addButton(self.right_3)
        self.right_3.setObjectName(u"right_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.right_3)

        self.right_4 = QCheckBox(self.fingerFrame)
        self.fingerGroup.addButton(self.right_4)
        self.right_4.setObjectName(u"right_4")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.right_4)

        self.right_5 = QCheckBox(self.fingerFrame)
        self.fingerGroup.addButton(self.right_5)
        self.right_5.setObjectName(u"right_5")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.right_5)


        self.verticalLayout_9.addWidget(self.fingerFrame)

        self.frame_12 = QFrame(self.handSettingPage)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_12)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.saveAreadyBtn = QCheckBox(self.frame_12)
        self.saveAreadyBtn.setObjectName(u"saveAreadyBtn")

        self.gridLayout_2.addWidget(self.saveAreadyBtn, 0, 0, 1, 1)

        self.saveTacleFixationBtn = QCheckBox(self.frame_12)
        self.saveTacleFixationBtn.setObjectName(u"saveTacleFixationBtn")

        self.gridLayout_2.addWidget(self.saveTacleFixationBtn, 1, 1, 1, 1)

        self.saveHotRouteBtn = QCheckBox(self.frame_12)
        self.saveHotRouteBtn.setObjectName(u"saveHotRouteBtn")

        self.gridLayout_2.addWidget(self.saveHotRouteBtn, 1, 0, 1, 1)

        self.saveHotBtn = QCheckBox(self.frame_12)
        self.saveHotBtn.setObjectName(u"saveHotBtn")

        self.gridLayout_2.addWidget(self.saveHotBtn, 0, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_12)

        self.mainPages.addWidget(self.handSettingPage)
        self.modelSettingPage = QWidget()
        self.modelSettingPage.setObjectName(u"modelSettingPage")
        self.verticalLayout_14 = QVBoxLayout(self.modelSettingPage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_6 = QFrame(self.modelSettingPage)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.colorDetect = QRadioButton(self.frame_6)
        self.modleGroup = QButtonGroup(MainWindow)
        self.modleGroup.setObjectName(u"modleGroup")
        self.modleGroup.addButton(self.colorDetect)
        self.colorDetect.setObjectName(u"colorDetect")

        self.horizontalLayout_7.addWidget(self.colorDetect)

        self.mediaPipe = QRadioButton(self.frame_6)
        self.modleGroup.addButton(self.mediaPipe)
        self.mediaPipe.setObjectName(u"mediaPipe")

        self.horizontalLayout_7.addWidget(self.mediaPipe)


        self.verticalLayout_14.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.modelSettingPage)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 30))
        self.frame_7.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.nextFingerBtn = QPushButton(self.frame_7)
        self.nextFingerBtn.setObjectName(u"nextFingerBtn")
        self.nextFingerBtn.setEnabled(False)
        self.nextFingerBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/Icons/chevrons-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nextFingerBtn.setIcon(icon13)

        self.horizontalLayout_8.addWidget(self.nextFingerBtn)

        self.skipBtn = QPushButton(self.frame_7)
        self.skipBtn.setObjectName(u"skipBtn")
        self.skipBtn.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.skipBtn.sizePolicy().hasHeightForWidth())
        self.skipBtn.setSizePolicy(sizePolicy2)
        self.skipBtn.setMinimumSize(QSize(0, 30))
        self.skipBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/icons/Icons/checkbox_unchecked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.skipBtn.setIcon(icon14)

        self.horizontalLayout_8.addWidget(self.skipBtn)

        self.fingerLabel = QLabel(self.frame_7)
        self.fingerLabel.setObjectName(u"fingerLabel")

        self.horizontalLayout_8.addWidget(self.fingerLabel)


        self.verticalLayout_14.addWidget(self.frame_7, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.modelSettingPage)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_4)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frontMap = QLabel(self.frame_4)
        self.frontMap.setObjectName(u"frontMap")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frontMap.sizePolicy().hasHeightForWidth())
        self.frontMap.setSizePolicy(sizePolicy3)
        self.frontMap.setCursor(QCursor(Qt.CrossCursor))
        self.frontMap.setMouseTracking(True)

        self.verticalLayout_18.addWidget(self.frontMap)


        self.verticalLayout_14.addWidget(self.frame_4)

        self.mainPages.addWidget(self.modelSettingPage)

        self.verticalLayout_2.addWidget(self.mainPages)


        self.horizontalLayout_2.addWidget(self.mainBodyContent)

        self.rightMenu = QWidget(self.mainBody)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setMinimumSize(QSize(200, 0))
        self.rightMenu.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_2 = QWidget(self.rightMenu)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_3 = QFrame(self.widget_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.listWidget = QListWidget(self.frame_3)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_15.addWidget(self.listWidget)


        self.verticalLayout_8.addWidget(self.frame_3)


        self.verticalLayout_7.addWidget(self.widget_2)


        self.horizontalLayout_2.addWidget(self.rightMenu)


        self.verticalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.files.setDefault(False)
        self.mainPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.leftMenuBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"ViDetect", None))
        self.openBtn.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.playBtn.setText("")
        self.previousBtn.setText("")
        self.pauseBtn.setText("")
        self.nextBtn.setText("")
        self.stopBtn.setText("")
        self.begin.setText("")
        self.reset.setText("")
        self.file.setText("")
        self.input.setText("")
        self.files.setText("")
        self.playerBtn.setText(QCoreApplication.translate("MainWindow", u"Player", None))
        self.alreadyMapBtn.setText(QCoreApplication.translate("MainWindow", u"AlreadyMap", None))
        self.hotMapBtn.setText(QCoreApplication.translate("MainWindow", u"HotMap", None))
        self.hotMapRouteBtn.setText(QCoreApplication.translate("MainWindow", u"HotMapRoute", None))
        self.tacicleFixationBtn.setText(QCoreApplication.translate("MainWindow", u"TacicleFixation", None))
        self.modelCompareBtn.setText(QCoreApplication.translate("MainWindow", u"ModelCompare", None))
        self.modelSettingBtn.setText(QCoreApplication.translate("MainWindow", u"ModelSetting", None))
        self.handSettingBtn.setText(QCoreApplication.translate("MainWindow", u"HandSetting", None))
        self.already.setText(QCoreApplication.translate("MainWindow", u"Already", None))
        self.hot.setText(QCoreApplication.translate("MainWindow", u"Hot", None))
        self.hotRoute.setText(QCoreApplication.translate("MainWindow", u"HorRoute", None))
        self.tacle.setText(QCoreApplication.translate("MainWindow", u"Tacle", None))
        self.compare.setText(QCoreApplication.translate("MainWindow", u"Compare", None))
        self.alreadyMap.setText("")
        self.hotMap.setText("")
        self.hotMapRoute.setText("")
        self.tacleForColour.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tacleForMedia.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tacleMap.setText("")
        self.left_1.setText(QCoreApplication.translate("MainWindow", u"left_1", None))
        self.left_2.setText(QCoreApplication.translate("MainWindow", u"left_2", None))
        self.left_3.setText(QCoreApplication.translate("MainWindow", u"left_3", None))
        self.left_4.setText(QCoreApplication.translate("MainWindow", u"left_4", None))
        self.left_5.setText(QCoreApplication.translate("MainWindow", u"left_5", None))
        self.right_1.setText(QCoreApplication.translate("MainWindow", u"right_1", None))
        self.right_2.setText(QCoreApplication.translate("MainWindow", u"right_2", None))
        self.right_3.setText(QCoreApplication.translate("MainWindow", u"right_3", None))
        self.right_4.setText(QCoreApplication.translate("MainWindow", u"right_4", None))
        self.right_5.setText(QCoreApplication.translate("MainWindow", u"right_5", None))
        self.saveAreadyBtn.setText(QCoreApplication.translate("MainWindow", u"SaveAreadyMap", None))
        self.saveTacleFixationBtn.setText(QCoreApplication.translate("MainWindow", u"saveTacleFixation", None))
        self.saveHotRouteBtn.setText(QCoreApplication.translate("MainWindow", u"SaveHotRoute", None))
        self.saveHotBtn.setText(QCoreApplication.translate("MainWindow", u"SaveHotMap", None))
        self.colorDetect.setText(QCoreApplication.translate("MainWindow", u"ColorDetect", None))
        self.mediaPipe.setText(QCoreApplication.translate("MainWindow", u"MediaPipe", None))
        self.nextFingerBtn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.skipBtn.setText(QCoreApplication.translate("MainWindow", u"Skip", None))
        self.fingerLabel.setText(QCoreApplication.translate("MainWindow", u"Click the finger under the image!", None))
        self.frontMap.setText("")
    # retranslateUi

