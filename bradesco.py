from pywinauto.application import Application
import time
import os
from pywinauto import mouse
from pywinauto import keyboard

# Run a target application
app = Application().start("C:\Program Files (x86)\AppBrad\AplicativoBradesco.exe")

time.sleep(35)



mouse.move(coords=(1380, 195))

time.sleep(2)

mouse.click(coords=(1360, 260))

time.sleep(2)

mouse.click(coords=(448, 121))

time.sleep(45)

mouse.click(coords=(83, 343))

time.sleep(30)

mouse.click(coords=(413, 322))

time.sleep(35)

keyboard.SendKeys('e')

keyboard.SendKeys('l')

keyboard.SendKeys('o')

keyboard.SendKeys('y')

time.sleep(1)

mouse.click(coords=(398, 350))

keyboard.SendKeys('e')

keyboard.SendKeys('l')

keyboard.SendKeys('o')

keyboard.SendKeys('y')

time.sleep(1)

mouse.click(coords=(706, 522))