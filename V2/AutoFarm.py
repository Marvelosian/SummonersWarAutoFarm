import pyautogui, cv2, msvcrt, random
import pygetwindow as gw
from time import sleep
from swicons.swiconsoy import *

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


searches=["Noxplayer","Bluestacks"]
# region=(0,0, 300, 400) explanation :(a 4-integer tuple of (left, top, width, height))
# print (Appwindow.size)
#print (Appwindow.topleft)
def getregion(appwindow):
    appwindow.topleft
    appwindow.size
    region = appwindow.topleft,appwindow.size
    return region
#Apptitles= gw.getAllTitles()
#search function with window name

def searchwindow(name):
    #search titles
    if gw.getWindowsWithTitle(name)[0]
        Appwindow = gw.getWindowsWithTitle(name)[0]



def autosearchwindow(searchwindows):
    #windows to search
    for i in range(len(searchwindows)):


def click(name):
    region = getregion()
    png=""
    btn=pyautogui.locateOnScreen(pngname, grayscale=True, confidence=.7,region)
    if (btn):
        pyautogui.click((btn.left + random_left(btn.width))
        ,(btn.top + random_top(btn.height)))
    btn=none
