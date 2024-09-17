# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QToolButton, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setEnabled(True)
        Widget.resize(370, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(370, 720))
        Widget.setMaximumSize(QSize(370, 720))
        font = QFont()
        font.setPointSize(11)
        Widget.setFont(font)
        Widget.setLayoutDirection(Qt.RightToLeft)
        Widget.setAutoFillBackground(False)
        Widget.setStyleSheet(u"QWidget{\n"
"background-color: #2a2a27;\n"
"}")
        Widget.setInputMethodHints(Qt.ImhNone)
        self.division = QPushButton(Widget)
        self.division.setObjectName(u"division")
        self.division.setGeometry(QRect(300, 350, 50, 35))
        font1 = QFont()
        font1.setBold(True)
        self.division.setFont(font1)
        self.division.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 20px; \n"
"    border-bottom-right-radius: 20px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size: 22px;\n"
"	padding-bottom: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"\n"
"")
        self.addition = QPushButton(Widget)
        self.addition.setObjectName(u"addition")
        self.addition.setGeometry(QRect(300, 530, 50, 35))
        self.addition.setFont(font1)
        self.addition.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 20px; \n"
"    border-bottom-right-radius: 20px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size: 22px;\n"
"	padding-bottom: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"")
        self.clearwork = QPushButton(Widget)
        self.clearwork.setObjectName(u"clearwork")
        self.clearwork.setGeometry(QRect(20, 600, 50, 35))
        self.clearwork.setFont(font1)
        self.clearwork.setStyleSheet(u"QPushButton {\n"
"	\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 20px; \n"
"    border-bottom-right-radius: 20px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size: 13px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"\n"
"")
        self.equalto = QPushButton(Widget)
        self.equalto.setObjectName(u"equalto")
        self.equalto.setGeometry(QRect(300, 590, 50, 35))
        self.equalto.setFont(font1)
        self.equalto.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 20px; \n"
"    border-bottom-right-radius: 20px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size: 22px;\n"
"	padding-bottom: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"\n"
"")
        self.subtraction = QPushButton(Widget)
        self.subtraction.setObjectName(u"subtraction")
        self.subtraction.setGeometry(QRect(300, 470, 50, 35))
        self.subtraction.setFont(font1)
        self.subtraction.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 20px; \n"
"    border-bottom-right-radius: 20px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size: 22px;\n"
"	padding-bottom: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"")
        self.multiplication = QPushButton(Widget)
        self.multiplication.setObjectName(u"multiplication")
        self.multiplication.setGeometry(QRect(300, 410, 50, 35))
        self.multiplication.setFont(font1)
        self.multiplication.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 20px; \n"
"    border-bottom-right-radius: 20px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size: 22px;\n"
"	padding-bottom: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"\n"
"")
        self.recall = QPushButton(Widget)
        self.recall.setObjectName(u"recall")
        self.recall.setGeometry(QRect(20, 550, 50, 25))
        self.recall.setFont(font1)
        self.recall.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"")
        self.store = QPushButton(Widget)
        self.store.setObjectName(u"store")
        self.store.setGeometry(QRect(20, 500, 50, 25))
        self.store.setFont(font1)
        self.store.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size: 13px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"\n"
"")
        self.log = QPushButton(Widget)
        self.log.setObjectName(u"log")
        self.log.setGeometry(QRect(20, 450, 50, 25))
        self.log.setFont(font1)
        self.log.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"\n"
"")
        self.inverse = QPushButton(Widget)
        self.inverse.setObjectName(u"inverse")
        self.inverse.setGeometry(QRect(20, 400, 50, 25))
        self.inverse.setFont(font1)
        self.inverse.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"\n"
"")
        self.power = QPushButton(Widget)
        self.power.setObjectName(u"power")
        self.power.setGeometry(QRect(230, 400, 50, 25))
        font2 = QFont()
        font2.setBold(True)
        font2.setKerning(True)
        self.power.setFont(font2)
        self.power.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size: 15px;	\n"
"	padding-bottom: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"\n"
"")
        self.reciprocal = QPushButton(Widget)
        self.reciprocal.setObjectName(u"reciprocal")
        self.reciprocal.setGeometry(QRect(230, 350, 50, 25))
        self.reciprocal.setFont(font1)
        self.reciprocal.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size: 16px;	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"\n"
"")
        self.squareroot = QPushButton(Widget)
        self.squareroot.setObjectName(u"squareroot")
        self.squareroot.setGeometry(QRect(90, 350, 50, 25))
        self.squareroot.setFont(font1)
        self.squareroot.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size: 16px;	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"\n"
"")
        self.percent = QPushButton(Widget)
        self.percent.setObjectName(u"percent")
        self.percent.setGeometry(QRect(20, 350, 50, 25))
        self.percent.setFont(font1)
        self.percent.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size: 16px;	\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"\n"
"")
        self.square = QPushButton(Widget)
        self.square.setObjectName(u"square")
        self.square.setGeometry(QRect(160, 350, 50, 25))
        self.square.setFont(font1)
        self.square.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size: 16px;	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"\n"
"")
        self.parenthesisleft = QPushButton(Widget)
        self.parenthesisleft.setObjectName(u"parenthesisleft")
        self.parenthesisleft.setGeometry(QRect(90, 400, 50, 25))
        self.parenthesisleft.setFont(font1)
        self.parenthesisleft.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size: 18px;	\n"
"	padding-bottom: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"\n"
"")
        self.parenthesisright = QPushButton(Widget)
        self.parenthesisright.setObjectName(u"parenthesisright")
        self.parenthesisright.setGeometry(QRect(160, 400, 50, 25))
        self.parenthesisright.setFont(font1)
        self.parenthesisright.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size: 18px;	\n"
"	padding-bottom: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"\n"
"")
        self.presentvalue = QPushButton(Widget)
        self.presentvalue.setObjectName(u"presentvalue")
        self.presentvalue.setGeometry(QRect(160, 300, 50, 25))
        self.presentvalue.setFont(font1)
        self.presentvalue.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #EFECEC;\n"
"    color: black;\n"
"	font-size: 14px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#c1bbbb;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #a8a2a2;\n"
"}")
        self.period = QPushButton(Widget)
        self.period.setObjectName(u"period")
        self.period.setGeometry(QRect(20, 300, 50, 25))
        self.period.setFont(font1)
        self.period.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #EFECEC;\n"
"    color: black;\n"
"	font-size: 14px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#c1bbbb;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #a8a2a2;\n"
"}\n"
"")
        self.payment = QPushButton(Widget)
        self.payment.setObjectName(u"payment")
        self.payment.setGeometry(QRect(230, 300, 50, 25))
        self.payment.setFont(font1)
        self.payment.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #EFECEC;\n"
"    color: black;\n"
"	font-size: 14px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#c1bbbb;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #a8a2a2;\n"
"}")
        self.interestrate = QPushButton(Widget)
        self.interestrate.setObjectName(u"interestrate")
        self.interestrate.setGeometry(QRect(90, 300, 50, 25))
        self.interestrate.setFont(font1)
        self.interestrate.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #EFECEC;\n"
"    color: black;\n"
"	font-size: 14px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#c1bbbb;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #a8a2a2;\n"
"}")
        self.futurevalue = QPushButton(Widget)
        self.futurevalue.setObjectName(u"futurevalue")
        self.futurevalue.setGeometry(QRect(300, 300, 50, 25))
        self.futurevalue.setFont(font1)
        self.futurevalue.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #EFECEC;\n"
"    color: black;\n"
"	font-size: 14px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#c1bbbb;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #a8a2a2;\n"
"}")
        self.cashflow = QPushButton(Widget)
        self.cashflow.setObjectName(u"cashflow")
        self.cashflow.setGeometry(QRect(90, 250, 50, 25))
        self.cashflow.setFont(font1)
        self.cashflow.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size:14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"\n"
"")
        self.backspace = QPushButton(Widget)
        self.backspace.setObjectName(u"backspace")
        self.backspace.setGeometry(QRect(300, 250, 50, 25))
        self.backspace.setFont(font1)
        self.backspace.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size:20px;\n"
"	padding-bottom:4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"\n"
"")
        self.internalratereturn = QPushButton(Widget)
        self.internalratereturn.setObjectName(u"internalratereturn")
        self.internalratereturn.setGeometry(QRect(230, 250, 50, 25))
        self.internalratereturn.setFont(font1)
        self.internalratereturn.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size:14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"\n"
"")
        self.second = QPushButton(Widget)
        self.second.setObjectName(u"second")
        self.second.setGeometry(QRect(20, 250, 50, 25))
        self.second.setFont(font1)
        self.second.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #f7ef4c;\n"
"    color: black;\n"
"	font-size:14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:#ddd640;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #beb836;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.netpresentvalue = QPushButton(Widget)
        self.netpresentvalue.setObjectName(u"netpresentvalue")
        self.netpresentvalue.setGeometry(QRect(160, 250, 50, 25))
        self.netpresentvalue.setFont(font1)
        self.netpresentvalue.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size:14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"\n"
"")
        self.down = QPushButton(Widget)
        self.down.setObjectName(u"down")
        self.down.setGeometry(QRect(230, 200, 50, 25))
        self.down.setFont(font1)
        self.down.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size: 20px;\n"
"	padding-bottom:4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"\n"
"")
        self.up = QPushButton(Widget)
        self.up.setObjectName(u"up")
        self.up.setGeometry(QRect(160, 200, 50, 25))
        self.up.setFont(font1)
        self.up.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size: 20px;\n"
"	padding-bottom:4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"\n"
"")
        self.enter = QPushButton(Widget)
        self.enter.setObjectName(u"enter")
        self.enter.setGeometry(QRect(90, 200, 50, 25))
        self.enter.setFont(font1)
        self.enter.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size:14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"")
        self.compute = QPushButton(Widget)
        self.compute.setObjectName(u"compute")
        self.compute.setGeometry(QRect(20, 200, 50, 25))
        self.compute.setFont(font1)
        self.compute.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size:14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"")
        self.switchon = QPushButton(Widget)
        self.switchon.setObjectName(u"switchon")
        self.switchon.setGeometry(QRect(300, 200, 50, 25))
        self.switchon.setFont(font1)
        self.switchon.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 15px; \n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: #474646;\n"
"    color: white;\n"
"	font-size: 13px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#615f5f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #706f6f;\n"
"}\n"
"")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 20, 171, 20))
        font3 = QFont()
        font3.setFamilies([u"Sitka Display"])
        font3.setPointSize(15)
        font3.setBold(True)
        self.label.setFont(font3)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(14, 180, 63, 20))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(84, 180, 63, 20))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(154, 180, 63, 20))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(224, 180, 63, 20))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(14, 280, 63, 20))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(Widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(84, 280, 63, 20))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(Widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(154, 280, 63, 20))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(Widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(224, 280, 63, 20))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(Widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(294, 280, 63, 20))
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(Widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(14, 330, 63, 20))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(Widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(294, 330, 63, 20))
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(Widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(14, 380, 63, 20))
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(Widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(84, 380, 63, 20))
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}\n"
"")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(Widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(154, 380, 63, 20))
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_16 = QLabel(Widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(224, 380, 63, 20))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(True)
        self.label_16.setFont(font4)
        self.label_16.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_16.setScaledContents(False)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_17 = QLabel(Widget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(294, 390, 63, 20))
        self.label_17.setFont(font1)
        self.label_17.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 14px;\n"
"}")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(Widget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(294, 450, 63, 20))
        self.label_18.setFont(font1)
        self.label_18.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_19 = QLabel(Widget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(294, 510, 63, 20))
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_20 = QLabel(Widget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(294, 570, 63, 20))
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_21 = QLabel(Widget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(14, 580, 61, 21))
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_21.setAlignment(Qt.AlignCenter)
        self.label_22 = QLabel(Widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(84, 608, 61, 16))
        self.label_22.setFont(font1)
        self.label_22.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_22.setAlignment(Qt.AlignCenter)
        self.label_23 = QLabel(Widget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(154, 608, 61, 16))
        self.label_23.setFont(font1)
        self.label_23.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_23.setAlignment(Qt.AlignCenter)
        self.label_24 = QLabel(Widget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(224, 608, 61, 16))
        self.label_24.setFont(font1)
        self.label_24.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_25 = QLabel(Widget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(84, 548, 61, 16))
        self.label_25.setFont(font1)
        self.label_25.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_25.setAlignment(Qt.AlignCenter)
        self.label_26 = QLabel(Widget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(154, 548, 61, 16))
        self.label_26.setFont(font1)
        self.label_26.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_27 = QLabel(Widget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(224, 548, 61, 16))
        self.label_27.setFont(font1)
        self.label_27.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_27.setAlignment(Qt.AlignCenter)
        self.label_28 = QLabel(Widget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(84, 490, 61, 16))
        self.label_28.setFont(font1)
        self.label_28.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_28.setAlignment(Qt.AlignCenter)
        self.label_29 = QLabel(Widget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(154, 490, 61, 16))
        self.label_29.setFont(font1)
        self.label_29.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_29.setAlignment(Qt.AlignCenter)
        self.label_30 = QLabel(Widget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(224, 490, 61, 16))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy1)
        self.label_30.setFont(font1)
        self.label_30.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_30.setAlignment(Qt.AlignCenter)
        self.label_31 = QLabel(Widget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(84, 432, 61, 16))
        self.label_31.setFont(font1)
        self.label_31.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_31.setAlignment(Qt.AlignCenter)
        self.label_32 = QLabel(Widget)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(154, 432, 61, 16))
        self.label_32.setFont(font1)
        self.label_32.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_32.setAlignment(Qt.AlignCenter)
        self.label_33 = QLabel(Widget)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(224, 432, 61, 16))
        self.label_33.setFont(font1)
        self.label_33.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_33.setAlignment(Qt.AlignCenter)
        self.label_34 = QLabel(Widget)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(14, 480, 61, 16))
        self.label_34.setFont(font1)
        self.label_34.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_34.setAlignment(Qt.AlignCenter)
        self.label_35 = QLabel(Widget)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(70, 690, 231, 20))
        font5 = QFont()
        font5.setBold(True)
        font5.setItalic(True)
        self.label_35.setFont(font5)
        self.label_35.setStyleSheet(u"QLabel {\n"
"font-size: 10px;\n"
"}")
        self.label_35.setAlignment(Qt.AlignCenter)
        self.label_36 = QLabel(Widget)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(60, 140, 241, 20))
        self.label_36.setFont(font1)
        self.label_36.setStyleSheet(u"QLabel {\n"
"font-size: 15px;\n"
"}")
        self.label_36.setTextFormat(Qt.PlainText)
        self.label_36.setScaledContents(False)
        self.label_36.setAlignment(Qt.AlignCenter)
        self.label_37 = QLabel(Widget)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(14, 430, 63, 20))
        self.label_37.setFont(font1)
        self.label_37.setStyleSheet(u"QLabel {\n"
"color: #F1EC86;\n"
"font-size: 12px;\n"
"}")
        self.label_37.setAlignment(Qt.AlignCenter)
        self.number3 = QPushButton(Widget)
        self.number3.setObjectName(u"number3")
        self.number3.setGeometry(QRect(230, 566, 51, 41))
        self.number3.setFont(font1)
        self.number3.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 20px; \n"
"    border-bottom-right-radius: 20px;\n"
"    background-color: #979494;\n"
"    color: white;\n"
"    padding: 5px;\n"
"	font-size: 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#8a8888;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #6e6d6d;\n"
"}\n"
"")
        self.number0 = QPushButton(Widget)
        self.number0.setObjectName(u"number0")
        self.number0.setGeometry(QRect(90, 624, 51, 41))
        self.number0.setFont(font1)
        self.number0.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 20px; \n"
"    border-bottom-right-radius: 20px;\n"
"    background-color: #979494;\n"
"    color: white;\n"
"    padding: 5px;\n"
"	font-size: 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#8a8888;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #6e6d6d;\n"
"}\n"
"")
        self.number9 = QPushButton(Widget)
        self.number9.setObjectName(u"number9")
        self.number9.setGeometry(QRect(230, 450, 51, 41))
        self.number9.setFont(font1)
        self.number9.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 20px; \n"
"    border-bottom-right-radius: 20px;\n"
"    background-color: #979494;\n"
"    color: white;\n"
"    padding: 5px;\n"
"	font-size: 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#8a8888;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #6e6d6d;\n"
"}\n"
"")
        self.number9.setAutoRepeat(False)
        self.number1 = QPushButton(Widget)
        self.number1.setObjectName(u"number1")
        self.number1.setGeometry(QRect(90, 566, 51, 41))
        self.number1.setFont(font1)
        self.number1.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 20px; \n"
"    border-bottom-right-radius: 20px;\n"
"    background-color: #979494;\n"
"    color: white;\n"
"    padding: 5px;\n"
"	font-size: 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#8a8888;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #6e6d6d;\n"
"}\n"
"")
        self.number8 = QPushButton(Widget)
        self.number8.setObjectName(u"number8")
        self.number8.setGeometry(QRect(160, 450, 51, 41))
        self.number8.setFont(font1)
        self.number8.setMouseTracking(True)
        self.number8.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 20px; \n"
"    border-bottom-right-radius: 20px;\n"
"    background-color: #979494;\n"
"    color: white;\n"
"    padding: 5px;\n"
"	font-size: 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#8a8888;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #6e6d6d;\n"
"}")
        self.negative = QPushButton(Widget)
        self.negative.setObjectName(u"negative")
        self.negative.setGeometry(QRect(230, 624, 51, 41))
        self.negative.setFont(font1)
        self.negative.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 20px; \n"
"    border-bottom-right-radius: 20px;\n"
"    background-color: #979494;\n"
"    color: white;\n"
"    padding: 5px;\n"
"	font-size: 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#8a8888;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #6e6d6d;\n"
"}\n"
"")
        self.number7 = QPushButton(Widget)
        self.number7.setObjectName(u"number7")
        self.number7.setGeometry(QRect(90, 450, 51, 41))
        self.number7.setFont(font1)
        self.number7.setMouseTracking(True)
        self.number7.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 20px; \n"
"    border-bottom-right-radius: 20px;\n"
"    background-color: #979494;\n"
"    color: white;\n"
"    padding: 5px;\n"
"	font-size: 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#8a8888;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #6e6d6d;\n"
"}")
        self.number5 = QPushButton(Widget)
        self.number5.setObjectName(u"number5")
        self.number5.setGeometry(QRect(160, 508, 51, 41))
        self.number5.setFont(font1)
        self.number5.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 20px; \n"
"    border-bottom-right-radius: 20px;\n"
"    background-color: #979494;\n"
"    color: white;\n"
"    padding: 5px;\n"
"	font-size: 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#8a8888;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #6e6d6d;\n"
"}\n"
"")
        self.decimal = QPushButton(Widget)
        self.decimal.setObjectName(u"decimal")
        self.decimal.setGeometry(QRect(160, 624, 51, 41))
        self.decimal.setFont(font1)
        self.decimal.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 20px; \n"
"    border-bottom-right-radius: 20px;\n"
"    background-color: #979494;\n"
"    color: white;\n"
"    padding: 5px;\n"
"	font-size: 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#8a8888;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #6e6d6d;\n"
"}\n"
"")
        self.number6 = QPushButton(Widget)
        self.number6.setObjectName(u"number6")
        self.number6.setGeometry(QRect(230, 508, 51, 41))
        self.number6.setFont(font1)
        self.number6.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 20px; \n"
"    border-bottom-right-radius: 20px;\n"
"    background-color: #979494;\n"
"    color: white;\n"
"    padding: 5px;\n"
"	font-size: 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#8a8888;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #6e6d6d;\n"
"}\n"
"")
        self.number2 = QPushButton(Widget)
        self.number2.setObjectName(u"number2")
        self.number2.setGeometry(QRect(160, 566, 51, 41))
        self.number2.setFont(font1)
        self.number2.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 20px; \n"
"    border-bottom-right-radius: 20px;\n"
"    background-color: #979494;\n"
"    color: white;\n"
"    padding: 5px;\n"
"	font-size: 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#8a8888;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #6e6d6d;\n"
"}\n"
"")
        self.number4 = QPushButton(Widget)
        self.number4.setObjectName(u"number4")
        self.number4.setGeometry(QRect(90, 508, 51, 41))
        self.number4.setFont(font1)
        self.number4.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-top-left-radius: 10px;    \n"
"    border-top-right-radius: 10px;   \n"
"    border-bottom-left-radius: 20px; \n"
"    border-bottom-right-radius: 20px;\n"
"    background-color: #979494;\n"
"    color: white;\n"
"    padding: 5px;\n"
"	font-size: 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#8a8888;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #6e6d6d;\n"
"}\n"
"")
        self.toolButton = QToolButton(Widget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(10, 10, 31, 27))
        self.toolButton.setStyleSheet(u"QToolButton{\n"
"background-color: #474646;\n"
"font-size: 13px\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"background-color:#615f5f;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"background-color: #706f6f;\n"
"}\n"
"")
        self.toolButton.setPopupMode(QToolButton.InstantPopup)
        self.toolButton.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.screennumber = QLineEdit(Widget)
        self.screennumber.setObjectName(u"screennumber")
        self.screennumber.setGeometry(QRect(110, 69, 241, 51))
        font6 = QFont()
        font6.setFamilies([u"Digital-7 Mono"])
        font6.setBold(False)
        self.screennumber.setFont(font6)
        self.screennumber.setLayoutDirection(Qt.RightToLeft)
        self.screennumber.setStyleSheet(u"QLineEdit {  \n"
"	border-right: 2px solid #f3f3e8;\n"
"	border-bottom: 2px solid #f3f3e8;\n"
"	border-bottom-right-radius:8px;          \n"
"    background-color: #7e8c74;     \n"
"    padding-left: 5px;\n"
"    color: #333333; \n"
"	font-size: 42px;          \n"
"}")
        self.screennumber.setMaxLength(12)
        self.screennumber.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.screenletter = QLineEdit(Widget)
        self.screenletter.setObjectName(u"screenletter")
        self.screenletter.setGeometry(QRect(20, 69, 91, 51))
        self.screenletter.setFont(font6)
        self.screenletter.setStyleSheet(u"QLineEdit {\n"
"	border-bottom: 2px solid #f3f3e8;\n"
"	border-left: 2px solid #f3f3e8;\n"
"    border-bottom-left-radius: 8px;            \n"
"    background-color: #7e8c74;     \n"
"    padding-right: 8px;                       \n"
"    color: #333333; \n"
"	font-size: 40px;             \n"
"}")
        self.screensetting = QLineEdit(Widget)
        self.screensetting.setObjectName(u"screensetting")
        self.screensetting.setGeometry(QRect(20, 54, 331, 16))
        self.screensetting.setFont(font6)
        self.screensetting.setStyleSheet(u"QLineEdit {  \n"
"	border-top: 2px solid #f3f3e8;\n"
"	border-left: 2px solid #f3f3e8;\n"
"	border-right: 2px solid #f3f3e8;\n"
"    border-top-right-radius: 8px;            \n"
"	border-top-left-radius: 8px;\n"
"    background-color: #7e8c74;     \n"
"                        \n"
"    color: #333333; \n"
"	font-size: 13px;         \n"
"}")

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"TIBAplusFinancialCalculator", None))
        self.division.setText(QCoreApplication.translate("Widget", u"\u00f7", None))
#if QT_CONFIG(shortcut)
        self.division.setShortcut(QCoreApplication.translate("Widget", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.addition.setText(QCoreApplication.translate("Widget", u"+", None))
#if QT_CONFIG(shortcut)
        self.addition.setShortcut(QCoreApplication.translate("Widget", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.clearwork.setText(QCoreApplication.translate("Widget", u"CE|C", None))
#if QT_CONFIG(shortcut)
        self.clearwork.setShortcut(QCoreApplication.translate("Widget", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.equalto.setText(QCoreApplication.translate("Widget", u"=", None))
#if QT_CONFIG(shortcut)
        self.equalto.setShortcut(QCoreApplication.translate("Widget", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.subtraction.setText(QCoreApplication.translate("Widget", u"-", None))
#if QT_CONFIG(shortcut)
        self.subtraction.setShortcut(QCoreApplication.translate("Widget", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.multiplication.setText(QCoreApplication.translate("Widget", u"\u00d7", None))
#if QT_CONFIG(shortcut)
        self.multiplication.setShortcut(QCoreApplication.translate("Widget", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.recall.setText(QCoreApplication.translate("Widget", u"RCL", None))
        self.store.setText(QCoreApplication.translate("Widget", u"STO", None))
        self.log.setText(QCoreApplication.translate("Widget", u"LN", None))
        self.inverse.setText(QCoreApplication.translate("Widget", u"INV", None))
        self.power.setText(QCoreApplication.translate("Widget", u"y\u1d61", None))
#if QT_CONFIG(shortcut)
        self.power.setShortcut(QCoreApplication.translate("Widget", u"^", None))
#endif // QT_CONFIG(shortcut)
        self.reciprocal.setText(QCoreApplication.translate("Widget", u"1/x", None))
        self.squareroot.setText(QCoreApplication.translate("Widget", u"\u221ax", None))
        self.percent.setText(QCoreApplication.translate("Widget", u"%", None))
        self.square.setText(QCoreApplication.translate("Widget", u"x\u00b2", None))
        self.parenthesisleft.setText(QCoreApplication.translate("Widget", u"(", None))
#if QT_CONFIG(shortcut)
        self.parenthesisleft.setShortcut(QCoreApplication.translate("Widget", u"(", None))
#endif // QT_CONFIG(shortcut)
        self.parenthesisright.setText(QCoreApplication.translate("Widget", u")", None))
#if QT_CONFIG(shortcut)
        self.parenthesisright.setShortcut(QCoreApplication.translate("Widget", u")", None))
#endif // QT_CONFIG(shortcut)
        self.presentvalue.setText(QCoreApplication.translate("Widget", u"PV", None))
        self.period.setText(QCoreApplication.translate("Widget", u"N", None))
        self.payment.setText(QCoreApplication.translate("Widget", u"PMT", None))
        self.interestrate.setText(QCoreApplication.translate("Widget", u"I/Y", None))
        self.futurevalue.setText(QCoreApplication.translate("Widget", u"FV", None))
        self.cashflow.setText(QCoreApplication.translate("Widget", u"CF", None))
        self.backspace.setText(QCoreApplication.translate("Widget", u"\u2192", None))
#if QT_CONFIG(shortcut)
        self.backspace.setShortcut(QCoreApplication.translate("Widget", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.internalratereturn.setText(QCoreApplication.translate("Widget", u"IRR", None))
        self.second.setText(QCoreApplication.translate("Widget", u"2ND", None))
#if QT_CONFIG(shortcut)
        self.second.setShortcut(QCoreApplication.translate("Widget", u"F2", None))
#endif // QT_CONFIG(shortcut)
        self.netpresentvalue.setText(QCoreApplication.translate("Widget", u"NPV", None))
        self.down.setText(QCoreApplication.translate("Widget", u"\u2193", None))
#if QT_CONFIG(shortcut)
        self.down.setShortcut(QCoreApplication.translate("Widget", u"Down", None))
#endif // QT_CONFIG(shortcut)
        self.up.setText(QCoreApplication.translate("Widget", u"\u2191", None))
#if QT_CONFIG(shortcut)
        self.up.setShortcut(QCoreApplication.translate("Widget", u"Down", None))
#endif // QT_CONFIG(shortcut)
        self.enter.setText(QCoreApplication.translate("Widget", u"ENTER", None))
        self.compute.setText(QCoreApplication.translate("Widget", u"CPT", None))
        self.switchon.setText(QCoreApplication.translate("Widget", u"ON|OFF", None))
        self.label.setText(QCoreApplication.translate("Widget", u"TI BA II Plus", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"QUIT", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"SET", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"DEL", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"INS", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"xP/Y", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"P/Y", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"AMORT", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"BGN", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"CLR TVM", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"K", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"RAND", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"HYP", None))
        self.label_14.setText(QCoreApplication.translate("Widget", u"SIN", None))
        self.label_15.setText(QCoreApplication.translate("Widget", u"COS", None))
        self.label_16.setText(QCoreApplication.translate("Widget", u"TAN", None))
        self.label_17.setText(QCoreApplication.translate("Widget", u"x!", None))
        self.label_18.setText(QCoreApplication.translate("Widget", u"nPr", None))
        self.label_19.setText(QCoreApplication.translate("Widget", u"nCr", None))
        self.label_20.setText(QCoreApplication.translate("Widget", u"ANS", None))
        self.label_21.setText(QCoreApplication.translate("Widget", u"CLR WORK", None))
        self.label_22.setText(QCoreApplication.translate("Widget", u"MEM", None))
        self.label_23.setText(QCoreApplication.translate("Widget", u"FORMAT", None))
        self.label_24.setText(QCoreApplication.translate("Widget", u"RESET", None))
        self.label_25.setText(QCoreApplication.translate("Widget", u"DATE", None))
        self.label_26.setText(QCoreApplication.translate("Widget", u"ICONV", None))
        self.label_27.setText(QCoreApplication.translate("Widget", u"PROFIT", None))
        self.label_28.setText(QCoreApplication.translate("Widget", u"DEPR", None))
        self.label_29.setText(QCoreApplication.translate("Widget", u"\u25ff %", None))
        self.label_30.setText(QCoreApplication.translate("Widget", u"BRKEVEN", None))
        self.label_31.setText(QCoreApplication.translate("Widget", u"DATA", None))
        self.label_32.setText(QCoreApplication.translate("Widget", u"STAT", None))
        self.label_33.setText(QCoreApplication.translate("Widget", u"BOND", None))
        self.label_34.setText(QCoreApplication.translate("Widget", u"ROUND", None))
        self.label_35.setText(QCoreApplication.translate("Widget", u"Developed by Dhruva Sahani", None))
        self.label_36.setText(QCoreApplication.translate("Widget", u"B U S I N E S S   A N A L Y S T", None))
        self.label_37.setText(QCoreApplication.translate("Widget", u"e\u02e3", None))
        self.number3.setText(QCoreApplication.translate("Widget", u"3", None))
#if QT_CONFIG(shortcut)
        self.number3.setShortcut(QCoreApplication.translate("Widget", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.number0.setText(QCoreApplication.translate("Widget", u"0", None))
#if QT_CONFIG(shortcut)
        self.number0.setShortcut(QCoreApplication.translate("Widget", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.number9.setText(QCoreApplication.translate("Widget", u"9", None))
#if QT_CONFIG(shortcut)
        self.number9.setShortcut(QCoreApplication.translate("Widget", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.number1.setText(QCoreApplication.translate("Widget", u"1", None))
#if QT_CONFIG(shortcut)
        self.number1.setShortcut(QCoreApplication.translate("Widget", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.number8.setText(QCoreApplication.translate("Widget", u"8", None))
#if QT_CONFIG(shortcut)
        self.number8.setShortcut(QCoreApplication.translate("Widget", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.negative.setText(QCoreApplication.translate("Widget", u"+|-", None))
        self.number7.setText(QCoreApplication.translate("Widget", u"7", None))
#if QT_CONFIG(shortcut)
        self.number7.setShortcut(QCoreApplication.translate("Widget", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.number5.setText(QCoreApplication.translate("Widget", u"5", None))
#if QT_CONFIG(shortcut)
        self.number5.setShortcut(QCoreApplication.translate("Widget", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.decimal.setText(QCoreApplication.translate("Widget", u".", None))
#if QT_CONFIG(shortcut)
        self.decimal.setShortcut(QCoreApplication.translate("Widget", u".", None))
#endif // QT_CONFIG(shortcut)
        self.number6.setText(QCoreApplication.translate("Widget", u"6", None))
#if QT_CONFIG(shortcut)
        self.number6.setShortcut(QCoreApplication.translate("Widget", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.number2.setText(QCoreApplication.translate("Widget", u"2", None))
#if QT_CONFIG(shortcut)
        self.number2.setShortcut(QCoreApplication.translate("Widget", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.number4.setText(QCoreApplication.translate("Widget", u"4", None))
#if QT_CONFIG(shortcut)
        self.number4.setShortcut(QCoreApplication.translate("Widget", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.toolButton.setText(QCoreApplication.translate("Widget", u"\u2630", None))
        self.screennumber.setText(QCoreApplication.translate("Widget", u"1234567890.-", None))
        self.screenletter.setText(QCoreApplication.translate("Widget", u"asd=", None))
        self.screensetting.setText(QCoreApplication.translate("Widget", u"12345678901234567890123456789012345678901234567890", None))
    # retranslateUi

