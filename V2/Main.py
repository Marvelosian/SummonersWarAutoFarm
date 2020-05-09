import pyautogui, cv2, msvcrt, random
from time import sleep
import pygetwindow as gw
from sw-icons/sw-icons-v import *

# region=(0,0, 300, 400) explanation :(a 4-integer tuple of (left, top, width, height))
# Random wait time between clicks

def wait():
    sleep(round(random.uniform(.8, 3), 2))

#v1

Screen=""
#Home,Battle,arena,toa,Cairos,RoW,Tartarus,World Boss

battle=""
#Arena,Garen,Siz,Kabir,Ragon,Telain,Hydeni,Tamor,Vrofagus,Faimon,Aiden,Ferun,Runar,Charuka,World Boss

#Should log stars,and stats

#What runes should not sell
Rune_stars=0
Wanted_Rune_stars=0
Substats=""
Wanted_Substats=""
#End of Rune selection


#end of v1


Runes = 0
Runs = 0

# Random clicking location
def random_left(width):
    objx = random.randint(0,width)
    return objx
def random_top(height):
    objy = random.randint(0,height)
    return objy


while 1:

    # Press 2 times the screen at Victory
    victory = pyautogui.locateOnScreen('img/victory.PNG', grayscale=True, confidence=.7)
    if(victory):
        wait()
        pyautogui.click((victory.left + random_left(victory.width))
        ,(victory.top + random_top(victory.height))
        , clicks=2, interval=1.5)
        print("Finished Run")
        wait()

    # Press Ok for runes,monster,events etc.
    btn_ok = pyautogui.locateOnScreen('img/ok.PNG', grayscale=True, confidence=.7)
    if(btn_ok):
        pyautogui.click((btn_ok.left + random_left(btn_ok.width))
        ,(btn_ok.top + random_top(btn_ok.height)))
        print("Got Something,Next update I will recognize what it is,sell runes below 6 stars,and log them")
    wait()

    # Press Replay
    btn_replay = pyautogui.locateOnScreen('img/replay.PNG', grayscale=True, confidence=.9)
    if(btn_replay):
        pyautogui.click((btn_replay.left + random_left(btn_replay.width))
        ,(btn_replay.top + random_top(btn_replay.height)))
        Runs=Runs+1
        print ("You have auto:",Runs,"Runs")
    wait()

    #No Energy??
    btn_notenoughenergy = pyautogui.locateOnScreen('img/notenoughenergy.PNG', grayscale=True, confidence=.9)
    if(btn_notenoughenergy):
        pyautogui.click((btn_notenoughenergy.left + random_left(btn_notenoughenergy.width))
        ,(btn_notenoughenergy.top + random_top(btn_notenoughenergy.height)))
        print("Not enough energy,opening gift box(EXPERIMENTAL)")
        wait()

        btn_maybeenergy = pyautogui.locateOnScreen('img/maybenergy.PNG', grayscale=True, confidence=.9)
        if(btn_maybeenergy):
            # removing random and calculating where to click,needs YOUR tweaking
            pyautogui.click((btn_maybeenergy.left +((btn_maybeenergy.width)-50))
            ,(btn_maybeenergy.top + (btn_maybeenergy.height)-50))
            print("I got the energy,exiting and retrying")
            wait()
            # Exit
            btn_exit = pyautogui.locateOnScreen('img/exit.PNG', grayscale=True, confidence=.9)
            if(btn_exit):
                pyautogui.click((btn_exit.left + random_left(btn_exit.width))
                ,(btn_exit.top + random_top(btn_exit.height)))
                print("Exit tab")
    wait()

    # End of Press Replay




    #Prepare function
    btn_prepare = pyautogui.locateOnScreen('img/prepare.PNG', grayscale=True, confidence=.7)
    if(btn_prepare):
        pyautogui.click((btn_prepare.left + random_left(btn_prepare.width))
        ,(btn_prepare.top + random_top(btn_prepare.height)))
        btn_startreplay = pyautogui.locateOnScreen('img/startreplay.PNG', grayscale=True, confidence=.7)
        wait()
        if(btn_startreplay):
            pyautogui.click((btn_startreplay.left + random_left(btn_startreplay.width))
            ,(btn_startreplay.top + random_top(btn_startreplay.height)))
    wait()
    #End of Prepare

    #captcha
    #Is there no captcha?
    wait()




    ## Reset the random position
    victory = None
    btn_ok = None
    btn_replay = None
    btn_notenoughenergy= None
    btn_maybeenergy= None
    btn_exit = None
    btn_prepare = None
    btn_startreplay = None

    # Quit the program
    if msvcrt.kbhit():
        if ord(msvcrt.getch()) == 59:
            break
