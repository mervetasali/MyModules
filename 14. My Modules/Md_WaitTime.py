#Waits for the time defined by the user before exiting

import time # Imports time library to use sleep command

def waitBeforeQuit(waitTime):
    for currentTime in range(waitTime,0,-1):
        print(f"The programme will be ended in {currentTime} seconds.. ", end="\r")
        time.sleep(1)