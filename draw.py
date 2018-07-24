#!Python3
#This program automaticly draw a shape
#Place mouse cursor on paint and run the program

import pyautogui

pyautogui.click()
distance = 300
while distance > 0:
    print(distance,0)
    pyautogui.dragRel(distance, 0, duration=0.1)
    distance = distance - 25
    print(0,distance)
    pyautogui.dragRel(0,distance,duration=0.1)
    print(-distance,0)
    pyautogui.dragRel(-distance,0,duration=0.1)
    distance = distance-25
    print(0,-distance)
    pyautogui.dragRel(0,-distance,duration=0.1)
    
