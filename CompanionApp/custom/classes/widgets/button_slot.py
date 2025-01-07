# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPainterPath, QColor, QPen
from PySide6.QtCore import Signal

S_BORDER_SIZE = 4
S_BORDER_RADIUS = 10
S_DEFAULT_BORDER_COLOR = QColor(69, 69, 69)  # #454545
S_BACKGROUND_COLOR = QColor(18, 18, 18)  # #121212
S_HIGHLIGHT_COLOR = QColor(255, 255, 255)  # #FFFFFF

class ButtonSlot(QWidget):
    clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.label = ""

        self._is_selected = False
        self._is_hovered = False

        self.setMaximumSize(80, 80)
        self.setMouseTracking(True)
        self.hotkey = None  # Add a hotkey attribute

    def is_selected(self):
        """
        Checks if button is selected.

        Returns:
            bool: True if the button is selected, False otherwise.
        """
        return self._is_selected

    def set_selected(self, state):
        """
        Sets the selection state of the button and updates its appearance.

        Args:
            state (bool): True to select the button, False to deselect it.
        """
        self._is_selected = state
        self.update()  # Ensure the button appearance is updated

    def set_hotkey(self, hotkey):
        """
        Sets the hotkey for the button slot.

        Args:
            hotkey (str): The hotkey to set.
        """
        self.hotkey = hotkey

    def get_hotkey(self):
        """
        Gets the hotkey for the button slot.

        Returns:
            str: The hotkey assigned to the button slot.
        """
        return self.hotkey

    def paintEvent(self, event):
        """
        Handles widget painting.

        Args:
            event (QPaintEvent): The paint event object.
        """

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        border_color = S_HIGHLIGHT_COLOR if self._is_hovered or self._is_selected else S_DEFAULT_BORDER_COLOR

        rect = self.rect().adjusted(S_BORDER_SIZE / 2, S_BORDER_SIZE / 2, -S_BORDER_SIZE / 2, -S_BORDER_SIZE / 2)

        path = QPainterPath()
        path.addRoundedRect(rect, S_BORDER_RADIUS, S_BORDER_RADIUS)

        pen = QPen(border_color, S_BORDER_SIZE)
        painter.setPen(pen)
        painter.fillPath(path, S_BACKGROUND_COLOR)
        painter.drawPath(path)

    def enterEvent(self, event):
        """
        Handles mouse enter event for the widget.

        Args:
            event (QEnterEvent): The enter event object.
        """

        self._is_hovered = True
        self.update()

    def leaveEvent(self, event):
        """
        Handles mouse leave event for the widget.

        Args:
            event (QEvent): The leave event object.
        """

        self._is_hovered = False
        self.update()

    def mousePressEvent(self, event):
        """
        Handles mouse press event for the widget.

        Args:
            event (QMouseEvent): The mouse event object.
        """

        super().mousePressEvent(event)
        self.clicked.emit()
        print(f'emitted button {self.label} selected.')
