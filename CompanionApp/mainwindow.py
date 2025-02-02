# This Python file uses the following encoding: utf-8
import sys
# from custom.classes.util.hotkey_util import HotkeyRecorder

# from custom.classes.widgets.button_slot import ButtonSlot
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_setup import Ui_MainWindow
from pynput import keyboard
from pynput.keyboard import Key, Controller


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.selected_button = None  # Initialize selected_button to None
        self.keyboard_controller = Controller()  # Initialize keyboard controller

    def restore_window(self):
        """
        Restores the main window from system tray.
        """
        self.showNormal()

    def quit_application(self):
        """
        Closes the application and removes system tray icon.
        """
        self.ui.tray_icon.hide()
        QApplication.quit()

    def update_button_slots(self):
        self.ui.update_button_slots(self)

    def show_side_panel(self, button_slot):
        """
        Displays the side panel for the selected button slot.
        """
        print(f"Opening side panel for {button_slot.label}")

        config_panel = self.ui.button_config_panels.get(button_slot)
        if config_panel:
            self.ui.side_panel.setCurrentWidget(
                config_panel
            )  # Switch to the correct panel
            self.ui.side_panel.setVisible(True)

    def on_button_clicked(self, button):
        """
        Handles button click event to highlight the clicked button.
        """

        if self.selected_button:
            self.selected_button.set_selected(False)  # Deselect the previously selected button

        button.set_selected(True)
        self.selected_button = button

        self.show_side_panel(button)

    def record_hotkey(self, button_slot, hotkey_edit):
        """
        Records a hotkey and stores it in the given slot.
        """
        self.pressed_keys = set()

        def on_press(key):
            self.pressed_keys.add(key)
            hotkey_edit.setText('+'.join([self.format_key(k) for k in self.pressed_keys]))

        def on_release(key):
            if key == keyboard.Key.esc:
                self.hotkey_listener.stop()
                return

            hotkey = '+'.join([self.format_key(k) for k in self.pressed_keys])
            button_slot.set_hotkey(hotkey)
            hotkey_edit.setText(hotkey)
            self.hotkey_listener.stop()

        self.hotkey_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        self.hotkey_listener.start()

    def format_key(self, key):
        """
        Formats the key for display and storage.
        """
        if isinstance(key, keyboard.Key):
            return key.name
        else:
            return key.char

    def execute_hotkey(self, button_slot):
        """
        Executes the hotkey assigned to the given button slot.
        """
        hotkey = button_slot.get_hotkey()
        if hotkey:
            keys = hotkey.split('+')
            modifiers = []
            regular_keys = []

            for key in keys:
                if len(key) == 1:
                    regular_keys.append(key)
                else:
                    try:
                        modifiers.append(getattr(Key, key))
                    except AttributeError:
                        regular_keys.append(key)

            # Press modifiers first
            for key in modifiers:
                self.keyboard_controller.press(key)

            # Press regular keys
            for key in regular_keys:
                self.keyboard_controller.press(key)

            # Release regular keys
            for key in regular_keys:
                self.keyboard_controller.release(key)

            # Release modifiers last
            for key in modifiers:
                self.keyboard_controller.release(key)

    def update_hotkey_edit(self, button_slot, display_str, hotkey, hotkey_edit):
        """
        Updates hotkey_edit with its recorded hotkey text.
        """
        pass  # Remove the implementation of update_hotkey_edit

    def closeEvent(self, event):
        """
        Overrides closeEvent to minimize app to system tray.
        """
        if self.ui.tray_icon.isVisible():
            QMessageBox.information(
                self,
                "Minimize to System Tray",
                "The application will continue running in the system tray.",
            )
            self.hide()
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
