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
    QPalette, QPixmap, QRadialGradient, QTransform, QAction)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy, QSystemTrayIcon, #QAction,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget, QMenu, QMessageBox, QLineEdit)
import os
import json
from custom.classes.widgets.button_slot import ButtonSlot
from custom.classes.util.hotkey_util import HotkeyRecorder

class Ui_MainWindow(object):
    CONFIG_FILE = "button_config.json"

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
        icon.addFile(u"CompanionApp/icons/buttons.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.editor_button.setIcon(icon)
        self.editor_button.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.editor_button)

        self.vertical_spacer1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.vertical_spacer1)

        self.settings_button = QPushButton(self.menu_tab)
        self.settings_button.setObjectName(u"settings_button")
        icon1 = QIcon()
        icon1.addFile(u"CompanionApp/icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        self.button_slot_container.setMinimumSize(QSize(600, 400))
        self.button_slot_container.setMaximumSize(QSize(500, 400))
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

        self.setup_tray_icon(MainWindow)
        self.connect_button_count_selector(MainWindow)
        self.setup_side_panel(MainWindow)
        self.button_slots = []
        self.load_configuration(MainWindow)

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

    def setup_tray_icon(self, MainWindow):
        """
        Adds a system Tray icon and context menu for the icon.
        """
        icon_path = "CompanionApp/icons/placeholder.png"

        if not os.path.exists(icon_path):
            print(f"Icon file not found at path: {icon_path}")
        else:
            print(f"Icon file found at path: {icon_path}")

        self.tray_icon = QSystemTrayIcon(MainWindow)
        self.tray_icon.setIcon(QIcon(icon_path))

        self.tray_menu = QMenu(MainWindow)
        restore_action = QAction("Restore", MainWindow)
        restore_action.triggered.connect(MainWindow.restore_window)
        quit_action = QAction("Quit", MainWindow)
        quit_action.triggered.connect(MainWindow.quit_application)

        self.tray_menu.addAction(restore_action)
        self.tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.show()

    def connect_button_count_selector(self, MainWindow):
        self.button_count_selector = self.button_count_selector
        self.button_count_selector.currentIndexChanged.connect(MainWindow.update_button_slots)

    def setup_side_panel(self, MainWindow):
        """
        Sets up the side panel UI using a QStackedWidget.
        """

        self.side_panel = QStackedWidget(MainWindow)
        self.side_panel.setFixedWidth(200)
        self.side_panel.setStyleSheet("background-color: #1A1A1A;")
        self.side_panel.setVisible(False)

        layout = self.centralwidget.layout()
        layout.addWidget(self.side_panel)

        self.button_config_panels = {}

    def update_button_slots(self, MainWindow):
        """
        Updates the number of ButtonSlot widgets based on user selection.
        """

        # delete existing slots.
        layout = self.button_slot_container.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Add new button slots and save
        self.add_button_slots(layout, MainWindow)

    def add_button_slots(self, layout, MainWindow):
        """
        Adds ButtonSlot widgets to button container and creates corresponding configuration panels.
        """

        num_buttons = int(self.button_count_selector.currentText())
        self.button_slots = []

        rows = int(num_buttons**0.5) + (1 if num_buttons % int(num_buttons**0.5) else 0)
        cols = (num_buttons + rows - 1) // rows

        for i in range(num_buttons):
            button = ButtonSlot(MainWindow)
            button.label = f"Button {i + 1}"

            r, c = divmod(i, cols)
            layout.addWidget(button, r, c)

            button.clicked.connect(lambda b=button: MainWindow.show_side_panel(b))
            button.clicked.connect(lambda b=button: MainWindow.on_button_clicked(b))
            self.button_slots.append(button)

            config_panel = QWidget()
            config_layout = QVBoxLayout(config_panel)
            config_label = QLabel(f"Configure {button.label}")
            config_layout.addWidget(config_label)

            label_edit = QLineEdit()
            label_edit.setPlaceholderText("Enter button name")
            label_edit.setText(button.label)
            label_edit.editingFinished.connect(lambda b=button, le=label_edit: MainWindow.save_configuration(b, le))
            #save_button = QPushButton("Save")
            #save_button.clicked.connect(lambda checked, b=button, le=label_edit: MainWindow.save_configuration(b, le))

            hotkey_label = QLabel("Hotkey:")
            hotkey_edit = QLineEdit()
            hotkey_edit.setPlaceholderText("None")
            hotkey_edit.setReadOnly(True)
            record_button = QPushButton("Record Hotkey")
            record_button.clicked.connect(lambda checked, b=button, he=hotkey_edit: MainWindow.record_hotkey(b, he))

            config_layout.addWidget(label_edit)
            #config_layout.addWidget(save_button)
            config_layout.addWidget(hotkey_label)
            config_layout.addWidget(hotkey_edit)
            config_layout.addWidget(record_button)

            self.side_panel.addWidget(config_panel)
            self.button_config_panels[button] = config_panel
            spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
            config_layout.addItem(spacer)

    def load_configuration(self, MainWindow):
        """
        Loads button configuration from a JSON file, if it exists.
        """

        if os.path.exists(self.CONFIG_FILE):
            with open(self.CONFIG_FILE, 'r') as config_file:
                self.config_data = json.load(config_file)

            num_buttons = len(self.config_data.get("buttons", []))
            self.button_count_selector.setCurrentText(str(num_buttons))
            MainWindow.update_button_slots()

            # Apply saved labels to the buttons
            for idx, button_config in enumerate(self.config_data["buttons"]):
                if idx < len(self.button_slots):
                    self.button_slots[idx].label = button_config["label"]
                    self.button_slots[idx].hotkey = button_config["hotkey"]

                    config_panel = self.button_config_panels.get(self.button_slots[idx])
                    if config_panel:
                        line_edits = config_panel.findChildren(QLineEdit)
                        if len(line_edits) >= 2:
                            line_edits[0].setText(button_config["label"])

                            hotkey_str = '+'.join(button_config.get("hotkey", []))
                            line_edits[1].setText(hotkey_str)
        else:
            MainWindow.update_button_slots()