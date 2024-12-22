# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
"background-color: #121212;\n"
"}\n"
"\n"
"#main_body {\n"
"background-color: #1A1A1A;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: transparent;\n"
"border: none;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.menu_tab = QWidget(self.centralwidget)
        self.menu_tab.setObjectName(u"menu_tab")
        self.verticalLayout = QVBoxLayout(self.menu_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.editor_button = QPushButton(self.menu_tab)
        self.editor_button.setObjectName(u"editor_button")
        icon = QIcon()
        icon.addFile(u"icons/buttons.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.editor_button.setIcon(icon)
        self.editor_button.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.editor_button)

        self.vertical_spacer1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.vertical_spacer1)

        self.settings_button = QPushButton(self.menu_tab)
        self.settings_button.setObjectName(u"settings_button")
        icon1 = QIcon()
        icon1.addFile(u"icons/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_button.setIcon(icon1)
        self.settings_button.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.settings_button)


        self.horizontalLayout.addWidget(self.menu_tab)

        self.main_body = QStackedWidget(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.button_editor = QWidget()
        self.button_editor.setObjectName(u"button_editor")
        self.horizontalLayout_2 = QHBoxLayout(self.button_editor)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(self.button_editor)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.button_toolbar = QWidget(self.widget)
        self.button_toolbar.setObjectName(u"button_toolbar")
        self.button_toolbar.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.button_toolbar)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.button_toolbar)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.button_count_selector = QComboBox(self.button_toolbar)
        self.button_count_selector.addItem("")
        self.button_count_selector.addItem("")
        self.button_count_selector.addItem("")
        self.button_count_selector.addItem("")
        self.button_count_selector.addItem("")
        self.button_count_selector.addItem("")
        self.button_count_selector.addItem("")
        self.button_count_selector.addItem("")
        self.button_count_selector.addItem("")
        self.button_count_selector.addItem("")
        self.button_count_selector.setObjectName(u"button_count_selector")

        self.horizontalLayout_3.addWidget(self.button_count_selector)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.button_toolbar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.button_slot_container = QWidget(self.widget)
        self.button_slot_container.setObjectName(u"button_slot_container")
        self.button_slot_container.setMinimumSize(QSize(500, 300))
        self.button_slot_container.setMaximumSize(QSize(500, 300))
        self.gridLayout = QGridLayout(self.button_slot_container)
        self.gridLayout.setObjectName(u"gridLayout")

        self.verticalLayout_2.addWidget(self.button_slot_container)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.widget)

        self.main_body.addWidget(self.button_editor)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.main_body.addWidget(self.settings)

        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.editor_button.setText("")
        self.settings_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Number of Buttons:", None))
        self.button_count_selector.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.button_count_selector.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.button_count_selector.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.button_count_selector.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.button_count_selector.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.button_count_selector.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.button_count_selector.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.button_count_selector.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.button_count_selector.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.button_count_selector.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))

    # retranslateUi

