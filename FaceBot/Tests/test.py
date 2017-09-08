#!/usr/bin/python3.5

import sys
import os 
import getpass

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path+'/../FaceBot/')

from FaceBot import FaceBot

bot = FaceBot()

login = input('Username: ')
password = getpass.getpass()

bot.login(login,password)

notifs = bot.get_notifications()

if not notifs is False:
    for notif in notifs:
        print(notif)

bot.logout()

bot.stop_phantom()
