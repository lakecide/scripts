#import pyautogui as pg
import time
time.sleep(10)

txt = open('animal.txt', 'r')
a = "Jumoke is a"
for words in txt:
    print(f"{a} {words}")
    
    #pg.write(a+' '+words)
    #pg.press('Enter')