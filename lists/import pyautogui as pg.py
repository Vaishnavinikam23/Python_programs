import pyautogui as pg
import time
time.sleep(10)
txt = open("emoji.txt,"'r')
a= "Hey Vinu"
for i in txt:
    pg.write(a+''+i)
    pg.press("Enter")
    