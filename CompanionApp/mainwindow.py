# This Python file uses the following encoding: utf-8
import sys
import os
import json
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import QPropertyAnimation, Qt
from custom_widgets.button_slot import ButtonSlot
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QSystemTrayIcon,
    QMenu, QMessageBox, QWidget, QVBoxLayout,
    QLabel, QLineEdit, QPushButton, QComboBox
    )

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

CONFIG_FILE = "button_config.json"

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setup_tray_icon()
        self.connect_button_count_selector()

        self.button_slots = []
        self.load_configuration()
        self.setup_side_panel()

    def setup_tray_icon(self):
        """
        Adds a system Tray icon and context menu for the icon.
        """

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("icons\placeholder.svg"))

        self.tray_menu = QMenu(self)
        restore_action = QAction("Restore", self)
        restore_action.triggered.connect(self.restore_window)
        quit_action = QAction("Quit" ,self)
        quit_action.triggered.connect(self.quit_application)

        self.tray_menu.addAction(restore_action)
        self.tray_menu.addSeparator()
        self.tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(self.tray_menu)

        self.tray_icon.show()

    def connect_button_count_selector(self):
        self.button_count_selector = self.ui.button_count_selector
        self.button_count_selector.currentIndexChanged.connect(self.update_button_slots)

    def update_button_slots(self):
        """
        Updates the number of ButtonSlot widgets based on user selection.
        """

        # delete existing slots.
        layout = self.ui.button_slot_container.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Add new button slots and save
        self.add_button_slots(layout)

    def load_configuration(self):
        """
        Loads button configuration from a JSON file, if it exists.
        """

        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as config_file:
                self.config_data = json.load(config_file)

            num_buttons = len(self.config_data.get("buttons", []))
            self.button_count_selector.setCurrentText(str(num_buttons))
            self.update_button_slots()

            # Apply saved labels to the buttons
            for idx, button_config in enumerate(self.config_data["buttons"]):
                if idx < len(self.button_slots):
                    self.button_slots[idx].label = button_config["label"]
        else:
            # Default: Load based on combo box selection
            self.update_button_slots()

    def setup_side_panel(self):
        """
        Sets up side panel UI for customizing buttons.
        """

        self.side_panel = QWidget(self)
        self.side_panel.setFixedWidth(200)
        self.side_panel.setStyleSheet("background-color: #1A1A1A;")
        self.side_panel.setGeometry(self.width(), 0, 200, self.height())

        layout = QVBoxLayout(self.side_panel)
        layout.setAlignment(Qt.AlignTop)

        self.label_edit = QLineEdit()
        self.label_edit.setPlaceholderText("Enter button Name")
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.update_button_configuration)

        layout.addWidget(QLabel("Button Configuration"))
        layout.addWidget(self.label_edit)
        layout.addWidget(save_button)

        self.selected_button = None
        self.animation = QPropertyAnimation(self.side_panel, b"geometry")

    def update_button_configuration(self):
        """
        Saves changes made to this button slot.
        """

        if self.selected_button:
            new_label = self.label_edit.text()
            self.selected_button.label = new_label

            self.save_configuration()

    def add_button_slots(self, layout):
        """
        Adds ButtonSlot widgets to button container and loads config file.
        """

        num_buttons = int(self.button_count_selector.currentText())
        self.button_slots = []  # Reset the button slots list
        for i in range(num_buttons):
            button = ButtonSlot(self)
            button.label = f"Button {i + 1}"  # Default label
            layout.addWidget(button)
            button.clicked.connect(lambda b=button: self.show_side_panel(b))  # Connect signal
            self.button_slots.append(button)

    def save_configuration(self):
        """
        Saves the current configuration of the selected button slot.
        """

        self.config_data = {
            "buttons": [
                {"id": idx + 1, "label": button.label}
                for idx, button in enumerate(self.button_slots)
            ]
        }

        # write to config file
        with open(CONFIG_FILE, 'w') as config_file:
            json.dump(self.config_data, config_file, indent=4)

        print("saved")

    def show_side_panel(self, button_slot):
        """
        Displays the side panel for the selected button slot.
        """

        print('panel')
        self.side_panel.setGeometry(self.width(), 0, 200, self.height())
        self.selected_button = button_slot
        self.label_edit.setText(button_slot.label)
        self.animation.setDuration(300)
        self.animation.setStartValue(self.side_panel.geometry())
        self.animation.setEndValue(
            self.side_panel.geometry().translated(-self.side_panel.width(), 0)
            )
        self.animation.start()

    def closeEvent(self, event):
        """
        Overrides closeEvent to minimize app to system tray.
        """

        if self.tray_icon.isVisible():
            QMessageBox.information(self, "Minimize to System Tray",
            "The application will continue running in the system tray.")
            self.hide()
            event.ignore()

    def restore_window(self):
        """
        Restores the main window from system tray.
        """
        self.showNormal()

    def quit_application(self):
        """
        Closes the application and removes system tray icon.
        """

        self.save_configuration()
        self.tray_icon.hide()
        QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
