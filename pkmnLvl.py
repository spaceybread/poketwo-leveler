import pyautogui
import time


input('Primed')
time.sleep(5)
while True:
    pyautogui.write("level this bunny")
    time.sleep(0.1)
    pyautogui.hotkey('enter')
    time.sleep(1)
