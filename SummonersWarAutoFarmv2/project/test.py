import pyautogui, cv2, msvcrt, random
import pygetwindow as gw
from time import sleep
from swicons.swiconspy import *

#wait
def wait():
    sleep(round(random.uniform(.8, 3), 2))

#random
def random_left(width):
    objx = random.randint(0,width)
    return objx
def random_top(height):
    objy = random.randint(0,height)
    return objy
#test
# region=(0,0, 300, 400)
#explanation :(a 4-integer tuple of (left, top, width, height))
Appwindow = gw.getWindowsWithTitle('noxplayer')[0]
def getregion(appwindow):
    appwindow.left
    appwindow.top
    appwindow.width
    appwindow.height
    region = appwindow.left,appwindow.top,appwindow.width,appwindow.height
    return region
print (getregion(Appwindow))
