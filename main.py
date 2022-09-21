import json
import os
from automatization import *
import logging
import datetime

logging.basicConfig(filename='./logfile.log', encoding='utf-8', level=logging.DEBUG)

try:
    JSON_FILE = open('./config/config.json')
    CONFIG_DATA = json.load(JSON_FILE)
    JSON_FILE.close()
    PROGRAM = Automatization(CONFIG_DATA["user_data"])
    
except FileNotFoundError:
    logging.error(f'From main.py: login_data.json not found') 
    raise

try:
    while True:
        time.sleep(.1)
        PROGRAM.CheckScreen()
except:
    logging.error('From main.py: ', 'Error in execution')
    raise
