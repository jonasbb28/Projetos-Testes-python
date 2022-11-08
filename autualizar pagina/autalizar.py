import pyautogui
from time import sleep

while True:
    pyautogui.click(610,778,duration=0.5)
    for i in range(8):
        pyautogui.click(87,48,duration=0.5)
        sleep(2)
    pyautogui.click(610,778,duration=0.5)
    sleep(1200) 