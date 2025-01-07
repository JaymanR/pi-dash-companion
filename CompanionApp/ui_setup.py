# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
    QAction,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSystemTrayIcon,  # QAction,
    QSpacerItem,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
    QMenu,
    QMessageBox,
    QLineEdit,
)
import os
import json
from custom.classes.widgets.button_slot import ButtonSlot
from custom.classes.util.hotkey_util import HotkeyRecorder


class Ui_MainWindow(object):
    CONFIG_FILE = "button_config.json"

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(
            "#centralwidget {\n"
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
            "}"
        )
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu_tab = QWidget(self.centralwidget)
        self.menu_tab.setObjectName("menu_tab")
        self.verticalLayout = QVBoxLayout(self.menu_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.editor_button = QPushButton(self.menu_tab)
        self.editor_button.setObjectName("editor_button")
        icon = QIcon()
        icon.addFile(
            "CompanionApp/icons/buttons.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.editor_button.setIcon(icon)
        self.editor_button.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.editor_button)

        self.vertical_spacer1 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout.addItem(self.vertical_spacer1)

        self.settings_button = QPushButton(self.menu_tab)
        self.settings_button.setObjectName("settings_button")
        icon1 = QIcon()
        icon1.addFile(
            "CompanionApp/icons/settings.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.settings_button.setIcon(icon1)
        self.settings_button.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.settings_button)

        self.horizontalLayout.addWidget(self.menu_tab)

        self.main_body = QStackedWidget(self.centralwidget)
        self.main_body.setObjectName("main_body")
        self.button_editor = QWidget()
        self.button_editor.setObjectName("button_editor")
        self.horizontalLayout_2 = QHBoxLayout(self.button_editor)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QWidget(self.button_editor)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_toolbar = QWidget(self.widget)
        self.button_toolbar.setObjectName("button_toolbar")
        self.button_toolbar.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.button_toolbar)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QLabel(self.button_toolbar)
        self.label.setObjectName("label")

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout_2.addWidget(self.button_toolbar)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.button_slot_container = QWidget(self.widget)
        self.button_slot_container.setObjectName("button_slot_container")
        self.button_slot_container.setMinimumSize(QSize(600, 400))
        self.button_slot_container.setMaximumSize(QSize(500, 400))
        self.gridLayout = QGridLayout(self.button_slot_container)
        self.gridLayout.setObjectName("gridLayout")

        self.verticalLayout_2.addWidget(self.button_slot_container)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2.addWidget(self.widget)

        self.main_body.addWidget(self.button_editor)
        self.settings = QWidget()
        self.settings.setObjectName("settings")
        self.main_body.addWidget(self.settings)

        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.setup_tray_icon(MainWindow)
        self.setup_side_panel(MainWindow)
        self.setup_button_slots(MainWindow)
        self.button_slots = []

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.editor_button.setText("")
        self.settings_button.setText("")

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

    def setup_button_slots(self, MainWindow):
        """
        Populates button slots into the button container.
        """
        num_buttons = 6  # Number of buttons to create
        self.button_slots = []

        for i in range(num_buttons):
            button = ButtonSlot(MainWindow)
            button.label = f"Button {i + 1}"
            button.clicked.connect(lambda b=button: MainWindow.show_side_panel(b))
            button.clicked.connect(lambda b=button: MainWindow.on_button_clicked(b))
            self.gridLayout.addWidget(button, i // 3, i % 3)  # Adjust layout as needed
            self.button_slots.append(button)

            # Create and configure side panel for each button
            config_panel = QWidget()
            config_layout = QVBoxLayout(config_panel)
            config_label = QLabel(f"Configure {button.label}")
            config_layout.addWidget(config_label)

            label_edit = QLineEdit()
            label_edit.setPlaceholderText("Enter button name")
            label_edit.setText(button.label)
            label_edit.editingFinished.connect(
                lambda b=button, le=label_edit: self.update_button_label(b, le)
            )
            config_layout.addWidget(label_edit)

            hotkey_edit = QLineEdit()
            hotkey_edit.setPlaceholderText("Press a key")
            hotkey_edit.setReadOnly(True)
            hotkey_edit.mousePressEvent = lambda event, b=button, he=hotkey_edit: MainWindow.record_hotkey(b, he)
            config_layout.addWidget(hotkey_edit)

            test_button = QPushButton("Test Hotkey")
            test_button.clicked.connect(lambda _, b=button: MainWindow.execute_hotkey(b))
            config_layout.addWidget(test_button)

            self.side_panel.addWidget(config_panel)
            self.button_config_panels[button] = config_panel

    def update_button_label(self, button, line_edit):
        """
        Updates the button label with the text from the line edit.
        """
        button.label = line_edit.text()
        button.update()

    def add_button_slots(self, layout, MainWindow):
        """
        Adds ButtonSlot widgets to button container and creates corresponding configuration panels.
        """

        num_buttons = 6
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
            label_edit.editingFinished.connect(
                lambda b=button, le=label_edit: None  # Remove save_configuration connection
            )

            config_layout.addWidget(label_edit)

            self.side_panel.addWidget(config_panel)
            self.button_config_panels[button] = config_panel
            spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
            config_layout.addItem(spacer)
