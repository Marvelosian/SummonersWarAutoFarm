import pyautogui
import pygetwindow as gw


Apptitles= gw.getAllTitles()
Appwindow = gw.getWindowsWithTitle('NoxPlayer')[0]
print (Appwindow.size)
print (Appwindow.topleft)
print (Appwindow.bottomright)
print(Apptitles)
