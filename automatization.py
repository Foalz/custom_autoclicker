import keyboard
from pynput.mouse import Listener,Button,Controller
import pyautogui
import time
import random
import os
import logging
import datetime

logging.basicConfig(filename='./logfile.log', encoding='utf-8', level=logging.DEBUG)
mouse=Controller()

class Automatization:
    BTN_DICT = {
        "disconnect": "assets/Botones/disconnect.png",
        "logout": "assets/Botones/logout.png",
        "login_screen": "assets/Botones/username.png" 
    }
    

    def __init__(self, LOGIN_DATA):
        self.LOGIN_DATA = LOGIN_DATA

    
    def DateAndTime(self):
        """
            This method is made to make time registries to the logfile.log file.
            Because, the program works with time module, so if something fails, 
            developer can get an idea of what's wrong.
        """
        e = datetime.datetime.now() 
        dateString = f"[{e.day}/{e.month}/{e.year}]: {e.hour}:{e.minute}:{e.second}"
        return dateString

    def Click(self,  LOCATION):
        """
            Clicking screen method

            LOCATION: Stores pyautogui data of the detected image,
                      to be processed by pyautogui.center() method.

            mouse.position: Variable that stores the cursor position to be controlled by 
                            Controller library.
            pyautogui.center(LOCATION): Processes the LOCATION data to transform it to (X,Y)
                                        coordinates.
        """
        CLICK_TIME = ( random.randint(50, 130) ) / 100
        logging.info(f'From automatization.py (Click): {self.DateAndTime(), CLICK_TIME, "seconds"}')
        time.sleep(CLICK_TIME)
        logging.info(f'From automatization.py (Click): {self.DateAndTime(), "Coordinates: ",mouse.position}')
        mouse.position = pyautogui.center(LOCATION)
        randX, randY, op = random.randint(1, 10), random.randint(1,10), random.randint(-1, 1)
        (x, y) = mouse.position[0] + (randX * op), mouse.position[1] - (randX * op)
        mouse.position = (x, y) 
        logging.info(f'from automatization.py (Click) {self.DateAndTime()} RandX: {randX}\nRandY: {randY}\nOperation: {op}\nX:{x}\nY:{y}')
        print()
        logging.info(f'From automatization.py (Click): {self.DateAndTime(), "Coordinates: ",mouse.position}')
        time.sleep(.1)
        mouse.press(Button.left)
        time.sleep(.1)
        mouse.release(Button.left)
        mouse.position = (4,4)
        logging.info(f'From automatization.py (Click): {self.DateAndTime(), "Coordinates: ",mouse.position}')

    def PressDisconnect(self, btnLocation):
        """
            Method to press the gray disconnect button, passing all the box data to Click method.
        """
        self.Click(btnLocation)

    def typeData(self, btnLocation):
        """
            Types the user data found at ./config/config.json file.
        """
        self.Click(btnLocation)
        time.sleep(.1)
        keyboard.press('tab')
        time.sleep(.1)
        keyboard.release('tab')
        time.sleep(.1)
        keyboard.write(self.LOGIN_DATA['username'])
        time.sleep(.1)
        keyboard.press('tab')
        time.sleep(.1)
        keyboard.release('tab')
        time.sleep(.1)
        keyboard.write(self.LOGIN_DATA['password'])
        USERNAME_LOCATION = pyautogui.locateOnScreen("assets/Botones/login.png", confidence=.9)
        self.Click(USERNAME_LOCATION)

    def LogOut(self, btnLocation):
        """
            Method to press the orange logout button, passing all the box data to Click method.
        """
        self.Click(btnLocation)

    def CheckScreen(self):
        """
            Checks button type that is currently on screen.

            Button types:

            disconnect: just press the gray button.
            logout: press the 'logout' button and type the login data of the user.
            login_screen: it means that user is logged out, so the program proceeds to type user data.
        """

        btnLocation = '' 
        btnType = ''
        for (key, value) in self.BTN_DICT.items():
            time.sleep(.1)
            btnLocation = pyautogui.locateOnScreen(value, confidence=.9)
            logging.info(f'From automatization.py (CheckScreen): {self.DateAndTime()} Checking for -> {key}')
            logging.info(f'From automatization.py (CheckScreen): {self.DateAndTime(), btnLocation}')
            if (btnLocation):
                btnType = key
                logging.info(f'From automatization.py (CheckScreen): {self.DateAndTime()} Found!')
                break

        if (btnType == "disconnect"): self.PressDisconnect(btnLocation)
        elif (btnType == "logout"): self.LogOut(btnLocation)
        elif (btnType == "login_screen"): self.typeData(btnLocation)



