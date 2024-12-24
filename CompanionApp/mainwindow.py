# This Python file uses the following encoding: utf-8
import sys
import os
import json
from PySide6.QtGui import QIcon, QAction
from custom.classes.widgets.button_slot import ButtonSlot
from custom.classes.util.hotkey_util import HotkeyRecorder
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QSystemTrayIcon,
    QMenu, QMessageBox, QWidget, QVBoxLayout,
    QLabel, QLineEdit, QPushButton, QStackedWidget,
    QSpacerItem, QSizePolicy
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
        self.setup_side_panel()

        self.button_slots = []
        self.load_configuration()

    def setup_tray_icon(self):
        """
        Adds a system Tray icon and context menu for the icon.
        """

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("icons/placeholder.svg"))

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

    def connect_button_count_selector(self):
        self.button_count_selector = self.ui.button_count_selector
        self.button_count_selector.currentIndexChanged.connect(self.update_button_slots)

    def setup_side_panel(self):
        """
        Sets up the side panel UI using a QStackedWidget.
        """

        self.side_panel = QStackedWidget(self)
        self.side_panel.setFixedWidth(200)
        self.side_panel.setStyleSheet("background-color: #1A1A1A;")
        self.side_panel.setVisible(False)

        layout = self.ui.centralwidget.layout()
        layout.addWidget(self.side_panel)

        self.button_config_panels = {}

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

    def add_button_slots(self, layout):
        """
        Adds ButtonSlot widgets to button container and creates corresponding configuration panels.
        """

        num_buttons = int(self.button_count_selector.currentText())
        self.button_slots = []

        rows = int(num_buttons**0.5) + (1 if num_buttons % int(num_buttons**0.5) else 0)
        cols = (num_buttons + rows - 1) // rows

        for i in range(num_buttons):
            button = ButtonSlot(self)
            button.label = f"Button {i + 1}"

            r, c = divmod(i, cols)
            layout.addWidget(button, r, c)

            button.clicked.connect(lambda b=button: self.show_side_panel(b))
            button.clicked.connect(lambda b=button: self.on_button_clicked(b))
            self.button_slots.append(button)

            config_panel = QWidget()
            config_layout = QVBoxLayout(config_panel)
            config_label = QLabel(f"Configure {button.label}")
            config_layout.addWidget(config_label)

            label_edit = QLineEdit()
            label_edit.setPlaceholderText("Enter button name")
            label_edit.setText(button.label)
            label_edit.editingFinished.connect(lambda b=button, le=label_edit: self.save_configuration(b, le))
            #save_button = QPushButton("Save")
            #save_button.clicked.connect(lambda checked, b=button, le=label_edit: self.save_configuration(b, le))

            hotkey_label = QLabel("Hotkey:")
            hotkey_edit = QLineEdit()
            hotkey_edit.setPlaceholderText("None")
            hotkey_edit.setReadOnly(True)
            record_button = QPushButton("Record Hotkey")
            record_button.clicked.connect(lambda checked, b=button, he=hotkey_edit: self.record_hotkey(b, he))

            config_layout.addWidget(label_edit)
            #config_layout.addWidget(save_button)
            config_layout.addWidget(hotkey_label)
            config_layout.addWidget(hotkey_edit)
            config_layout.addWidget(record_button)

            self.side_panel.addWidget(config_panel)
            self.button_config_panels[button] = config_panel
            spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
            config_layout.addItem(spacer)

    def record_hotkey(self, button_slot, hotkey_edit):
        """
        Records a hotkey and stores it in the given slot.
        """

        self.hotkey_recorder = HotkeyRecorder()
        self.hotkey_recorder.hotkey_recorded.connect(
            lambda display_str, hotkey: self.update_hotkey_edit(button_slot, display_str, hotkey, hotkey_edit)
            )
        hotkey_edit.setText("Recording...")
        self.hotkey_recorder.run()

    def update_hotkey_edit(self, button_slot, display_str, hotkey, hotkey_edit):
        """
        Updates hotkey_edit with its recorded hotkey text.
        """

        hotkey_edit.setText(display_str)
        print(f"recorded hotkey: {hotkey}")

        button_slot.hotkey = hotkey
        self.save_configuration()

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
                    self.button_slots[idx].hotkey = button_config["hotkey"]

                    config_panel = self.button_config_panels.get(self.button_slots[idx])
                    if config_panel:
                        line_edits = config_panel.findChildren(QLineEdit)
                        if len(line_edits) >= 2:
                            line_edits[0].setText(button_config["label"])

                            hotkey_str = '+'.join(button_config.get("hotkey", []))
                            line_edits[1].setText(hotkey_str)
        else:
            self.update_button_slots()

    def update_button_configuration(self):
        """
        Saves changes made to this button slot.
        """

        if self.selected_button:
            new_label = self.label_edit.text()
            self.selected_button.label = new_label

            self.save_configuration()

    def save_configuration(self, button_slot=None, label_edit=None):
        """
        Saves the current configuration of the selected button slot.
        """

        print("saving...")
        if button_slot and label_edit:
            #print("saving label...")
            new_label = label_edit.text()
            button_slot.label = new_label

        #print("writing..")
        self.config_data = {
            "buttons": [
                {"id": idx + 1, "label": button.label, "hotkey": getattr(button, "hotkey", '')}
                for idx, button in enumerate(self.button_slots)
            ]
        }

        # write to config file
        with open(CONFIG_FILE, 'w') as config_file:
            json.dump(self.config_data, config_file, indent=4)

        print("saved.\n")

    def show_side_panel(self, button_slot):
        """
        Displays the side panel for the selected button slot.
        """
        print(f"Opening side panel for {button_slot.label}")

        config_panel = self.button_config_panels.get(button_slot)
        if config_panel:
            self.side_panel.setCurrentWidget(config_panel)  # Switch to the correct panel
            self.side_panel.setVisible(True)

    def on_button_clicked(self, button):
        """
        Handles button click event to highlight the clicked button.
        """

        for btn in self.button_slots:
            btn.set_selected(False)

        button.set_selected(True)
        self.selected_button = button

        self.show_side_panel(button)

    def closeEvent(self, event):
        """
        Overrides closeEvent to minimize app to system tray.
        """

        if self.tray_icon.isVisible():
            QMessageBox.information(self, "Minimize to System Tray",
            "The application will continue running in the system tray.")
            self.hide()
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
