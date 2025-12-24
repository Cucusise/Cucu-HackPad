import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_displayio_ssd1306 import SSD1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros


displayio.release_displays()

i2c = busio.I2C(board.D5, board.D4)

display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

display = SSD1306(
    display_bus,
    width=128,
    height=64,
)

splash = displayio.Group()
display.root_group = splash

text = "Hi Cucu!"
text_area = label.Label(
    terminalio.FONT,
    text=text,
    color=0xFFFFFF,
    x=20,
    y=32,
)

splash.append(text_area)


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
