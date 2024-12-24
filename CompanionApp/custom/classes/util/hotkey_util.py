# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
from PySide6.QtCore import Signal, QThread
from pynput import keyboard

class HotkeyRecorder(QThread):
    hotkey_recorded = Signal(str, list)

    def __init__(self):
        super().__init__()
        self.current_hotkey = set()

    def on_press(self, key):
        """
        Handles key press
        """

        try:
            self.current_hotkey.add(key.char)
        except AttributeError:
            self.current_hotkey.add(str(key))

    def on_release(self, key):
        """
        Handles Key Releases. Stops recording when all keys released.
        """

        try:
            if len(self.current_hotkey) > 0:
                display_str = '+'.join(
                    sorted([self.key_to_string(k)
                        for k in self.current_hotkey
                        ])
                    )
                hotkey_str = '+'.join(sorted(self.current_hotkey))
                self.hotkey_recorded.emit(display_str, list(self.current_hotkey))
                print(f"recorded: {hotkey_str}")
                self.current_hotkey.clear()
        except Exception as e:
            print(f"Error on release while recording: {e}")
        finally:
            return False

    def key_to_string(self, key):
        """
        Converts pynput key object to a more user-friendly string format.
        """

        key_map = {
                keyboard.Key.ctrl_l: "Ctrl_L",
                keyboard.Key.ctrl_r: "Ctrl_R",
                keyboard.Key.shift: "Shift",
                keyboard.Key.shift_l: "Shift_L",
                keyboard.Key.shift_r: "Shift_R",
                keyboard.Key.alt: "Alt",
                keyboard.Key.alt_l: "Alt_L",
                keyboard.Key.alt_r: "Alt_R",
                keyboard.Key.enter: "Enter",
                keyboard.Key.space: "Space",
                keyboard.Key.backspace: "Backspace",
                keyboard.Key.tab: "Tab",
                keyboard.Key.esc: "Esc",
                keyboard.Key.delete: "Delete",
                keyboard.Key.up: "Up",
                keyboard.Key.down: "Down",
                keyboard.Key.left: "Left",
                keyboard.Key.right: "Right",
            }

        control_char_map = {
                '\x01': 'A', '\x02': 'B', '\x03': 'C', '\x04': 'D',
                '\x05': 'E', '\x06': 'F', '\x07': 'G', '\x08': 'H',
                '\x09': 'I', '\x0A': 'J', '\x0B': 'K', '\x0C': 'L',
                '\x0D': 'M', '\x0E': 'N', '\x0F': 'O', '\x10': 'P',
                '\x11': 'Q', '\x12': 'R', '\x13': 'S', '\x14': 'T',
                '\x15': 'U', '\x16': 'V', '\x17': 'W', '\x18': 'X',
                '\x19': 'Y', '\x1A': 'Z'
            }


        if key in key_map:
            return key_map[key]
        elif hasattr(key, "char") and key.char:
            # Check if the key is a control character
            if key.char in control_char_map:
                return control_char_map[key.char]
            elif key.char.isprintable():
                return key.char.upper()
            else:
                return repr(key.char)
        else:
            return str(key).replace("Key.", "")

    def run(self):
        """
        Starts recording hotkey.
        """
        print("recording...")
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

class HotkeyExecutor:
    def __init__(self):
        self.controller = keyboard.Controller()

    def execute_hotkey(self, hotkey):
        """
        Executes given hotkey.
        """

        try:
            for key in hotkey:
                self.controller.press(key)

            for key in hotkey:
                self.controller.release(key)

            print(f"executed hotkey: {hotkey}")
        except Exception as e:
            print(f"Error executing hotkey {hotkey}: {e}")
