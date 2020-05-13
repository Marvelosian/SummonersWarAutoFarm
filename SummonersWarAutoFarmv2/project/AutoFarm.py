import pyautogui, cv2, msvcrt, random
import pygetwindow as gw
from time import sleep
from swicons.swiconspy import *
import eel

#start interface
eel.init('web')
eel.start('index.html', size=(1000, 600))

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


searches = ["Noxplayer","Bluestacks"]
getwindowauto = 0
#this function uses returns the appwindow's region(numbers)
def getregion(appwindow):
    # region=(0,0, 300, 400) explanation :(a 4-integer tuple of (left, top, width, height))
    region = appwindow.left,appwindow.top,appwindow.width,appwindow.height
    return region

#search function with window name
def searchwindow(name):
    #search titles
    #Apptitles= gw.getAllTitles()
    if gw.getWindowsWithTitle(name)[0]:
        Appwindow = gw.getWindowsWithTitle(name)[0]

def autosearchwindow(searchwindows):
    #windows to search
    for i in range(len(searchwindows)):
        oof= ("not made")

def getwindow():
    oof=("not made")
    return  oof

def click(name):
    regionnum = getregion(getwindow())
    pngname=locate(name)
    btn=pyautogui.locateOnScreen(pngname, grayscale=True, confidence=.9,region=(regionnum))
    if (btn):
        pyautogui.click((btn.left + random_left(btn.width))
        ,(btn.top + random_top(btn.height)))
    btn=none

def locate(name):
    return png
