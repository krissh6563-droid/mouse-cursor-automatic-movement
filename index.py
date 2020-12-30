import pyautogui
import time
print(pyautogui.size())

#time duration in which cursor move 
time_duration =  time.time() + 30
while time.time()<time_duration:
    pyautogui.moveTo(500,300,duration=2)
    pyautogui.moveTo(300,500,duration=2)
    