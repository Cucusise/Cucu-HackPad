import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros


keyboard = KMKKeyboard()


macros = Macros()
keyboard.modules.append(macros)


PINS = [board.D1, board.D2, board.D3, board.D4]


keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)


keyboard.keymap = [
    [KC.A, KC.F5, KC.F10, KC.F11]
]

if __name__ == '__main__':
    keyboard.go()