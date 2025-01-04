# This Python file uses the following encoding: utf-8
import sys
from custom.classes.util.hotkey_util import HotkeyRecorder
#from custom.classes.widgets.button_slot import ButtonSlot
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def restore_window(self):
        """
        Restores the main window from system tray.
        """
        self.showNormal()

    def quit_application(self):
        """
        Closes the application and removes system tray icon.
        """
        self.ui.save_configuration(self)
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
            self.ui.side_panel.setCurrentWidget(config_panel)  # Switch to the correct panel
            self.ui.side_panel.setVisible(True)

    def on_button_clicked(self, button):
        """
        Handles button click event to highlight the clicked button.
        """
        for btn in self.ui.button_slots:
            btn.set_selected(False)

        button.set_selected(True)
        self.selected_button = button

        self.show_side_panel(button)

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
        self.ui.save_configuration(self)

    def closeEvent(self, event):
        """
        Overrides closeEvent to minimize app to system tray.
        """
        if self.ui.tray_icon.isVisible():
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