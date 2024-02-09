# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from show_random_text import random_sentence
from audio_record import voice_recorder
from enroll import split_audio
import create_model
import check


class Ui_MainWindow(object):

    def openWindowRegist(self, MainWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RegistWindow()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def openWindowVerif(self, MainWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_VerifWindow()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(893, 555)
        MainWindow.setStyleSheet(
            " background-color:qlineargradient(spread:pad, x1:0.267045, y1:0.591, x2:0.943, y2:0.0856818, stop:0.0965909 rgba(0, 162, 169, 248), stop:1 rgba(110, 194, 99, 228))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 50, 551, 171))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("border:none")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 280, 161, 71))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    font: 18pt \"Century Gothic\";\n"
                                      "    background-color: #85eb63;\n"
                                      "border-radius: 13px;\n"
                                      "border-solid\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #76c45c;\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    color:#8d948f;\n"
                                      "    background-color: #7ed660\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(lambda: self.openWindowRegist(MainWindow))

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 280, 181, 71))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    font: 18pt \"Century Gothic\";\n"
                                        "    background-color: #85eb63;\n"
                                        "border-radius: 13px;\n"
                                        "border-solid\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: #76c45c;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    color:#8d948f;\n"
                                        "    background-color: #7ed660\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(lambda: self.openWindowVerif(MainWindow))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 893, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Choose Screen"))
        self.label.setText(_translate("MainWindow", "Select \"Registration\", to register,\n"
                                                    "                              if you are here for the first time.\n"
                                                    "\n"
                                                    "      Or choose \"Verification\", to go through \n"
                                                    "                                     verification."))
        self.pushButton.setText(_translate("MainWindow", "Registration"))
        self.pushButton_2.setText(_translate("MainWindow", "Verification"))


class Ui_RegistWindow(object):

    def openMainWindow(self, RegistWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        RegistWindow.hide()
        self.window.show()

    def start_record(self, RegistWindow):
        voice_recorder("target.wav", 70)
        split_audio('target.wav', 'raw_data_wav/')
        self.label_2.setText('   Recording \nCompleted')
        return None

    def train_model(self, RegistWindow):
        voices = create_model.wav_reader('raw_data_wav/')
        create_model.create_model(voices, 'model/_', 10)
        self.label_2.setText('Registration \nCompleted')
        return None

    def setupUi(self, RegistWindow):
        RegistWindow.setObjectName("RegistWindow")
        RegistWindow.resize(891, 552)
        RegistWindow.setStyleSheet(
            " background-color:qlineargradient(spread:pad, x1:0.267045, y1:0.591, x2:0.943, y2:0.0856818, stop:0.0965909 rgba(0, 162, 169, 248), stop:1 rgba(110, 194, 99, 228))")
        self.centralwidget = QtWidgets.QWidget(RegistWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 120, 821, 301))
        self.textBrowser.setStyleSheet("background-color: white;\n"
                                       "border: 1px solid;\n"
                                       "border-radius: 9px")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 430, 271, 71))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    font: 18pt \"Century Gothic\";\n"
                                      "    background-color: #85eb63;\n"
                                      "border-radius: 13px;\n"
                                      "border-solid\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #76c45c;\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    color:#8d948f;\n"
                                      "    background-color: #7ed660\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(lambda: self.start_record(RegistWindow))

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    font: 10pt \"Century Gothic\";\n"
                                        "    background-color: #85eb63;\n"
                                        "border-radius: 13px;\n"
                                        "border-solid\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: #76c45c;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    color:#8d948f;\n"
                                        "    background-color: #7ed660\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(lambda: self.openMainWindow(RegistWindow))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 40, 731, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("border:none;\n"
                                 "")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(710, 430, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setStyleSheet("border:none;\n"
                                   "")
        self.label_2.setScaledContents(False)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 430, 271, 71))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
                                        "    font: 18pt \"Century Gothic\";\n"
                                        "    background-color: #85eb63;\n"
                                        "border-radius: 13px;\n"
                                        "border-solid\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: #76c45c;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    color:#8d948f;\n"
                                        "    background-color: #7ed660\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.train_model(RegistWindow))
        RegistWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegistWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 22))
        self.menubar.setObjectName("menubar")
        RegistWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RegistWindow)
        self.statusbar.setObjectName("statusbar")
        RegistWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegistWindow)
        QtCore.QMetaObject.connectSlotsByName(RegistWindow)

    def retranslateUi(self, RegistWindow):
        _translate = QtCore.QCoreApplication.translate
        RegistWindow.setWindowTitle(_translate("RegistWindow", "Registration"))
        self.textBrowser.setHtml(_translate("RegistWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:14pt; color:#202122; background-color:#ffffff;\"></span></p></body></html>"))
        self.textBrowser.append(random_sentence('rand_sent.txt', 15))
        self.pushButton.setText(_translate("RegistWindow", "Start Recording"))
        self.pushButton_2.setText(_translate("RegistWindow", "Back"))
        self.label.setText(_translate("RegistWindow",
                                      "<html><head/><body><p align=\"center\">Click &quot;Start recording&quot; then introduce yourself and read the text below</p><p align=\"center\">Next click &quot;Register&quot;</p></body></html>"))
        self.label_2.setText(_translate("RegistWindow",
                                        "<html><head/><body><p align=\"center\">Expectation</p><p align=\"center\">Entries</p></body></html>"))
        self.pushButton_3.setText(_translate("RegistWindow", "Register"))


class Ui_VerifWindow(object):

    def openMainWindow(self, VerifWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        VerifWindow.hide()
        self.window.show()

    def check_permission(self, VerifWindow):
        voice_recorder('audio_to_check/target2check.wav', 7)
        val = check.check_access('audio_to_check/target2check.wav', 'model/')
        if val:
            self.label_2.setText("Access is allowed!")
        else:
            self.label_2.setText("Access is denied!")


    def setupUi(self, VerifWindow):
        VerifWindow.setObjectName("VerifWindow")
        VerifWindow.resize(890, 552)
        VerifWindow.setStyleSheet(
            " background-color:qlineargradient(spread:pad, x1:0.267045, y1:0.591, x2:0.943, y2:0.0856818, stop:0.0965909 rgba(0, 162, 169, 248), stop:1 rgba(110, 194, 99, 228))")
        self.centralwidget = QtWidgets.QWidget(VerifWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    font: 10pt \"Century Gothic\";\n"
                                        "    background-color: #85eb63;\n"
                                        "border-radius: 13px;\n"
                                        "border-solid\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: #76c45c;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    color:#8d948f;\n"
                                        "    background-color: #7ed660\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(lambda: self.openMainWindow(VerifWindow))

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 400, 271, 71))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    font: 18pt \"Century Gothic\";\n"
                                      "    background-color: #85eb63;\n"
                                      "border-radius: 13px;\n"
                                      "border-solid\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #76c45c;\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    color:#8d948f;\n"
                                      "    background-color: #7ed660\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(lambda: self.check_permission(VerifWindow))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 881, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("border:none;\n"
                                 "")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 110, 821, 95))
        self.textBrowser.setStyleSheet("background-color: white;\n"
                                       "border: 1px solid;\n"
                                       "border-radius: 9px")
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 220, 371, 111))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
                                   "    font: 28pt \"Century Gothic\";\n"
                                   "}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        VerifWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VerifWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 890, 22))
        self.menubar.setObjectName("menubar")
        VerifWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VerifWindow)
        self.statusbar.setObjectName("statusbar")
        VerifWindow.setStatusBar(self.statusbar)

        self.retranslateUi(VerifWindow)
        QtCore.QMetaObject.connectSlotsByName(VerifWindow)

    def retranslateUi(self, VerifWindow):
        _translate = QtCore.QCoreApplication.translate
        VerifWindow.setWindowTitle(_translate("VerifWindow", "Verification"))
        self.pushButton_2.setText(_translate("VerifWindow", "Back"))
        self.pushButton.setText(_translate("VerifWindow", "Check access"))
        self.label.setText(_translate("VerifWindow",
                                      "Click \"Check access\" then read the text below to pass verification\n"
                                      "                                Your access status will be shown below"))
        self.textBrowser.setHtml(_translate("VerifWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:14pt; color:#202122; background-color:#ffffff;\"></span></p></body></html>"))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.append(random_sentence('rand_sent.txt',2))
