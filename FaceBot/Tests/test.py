#!/usr/bin/python3.5

import sys
import os 
import getpass

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path+'/../FaceBot/')

from FaceBot import FaceBot

#from selenium import webdriver


#print dir(webdriver.PhantomJS)

bot = FaceBot()

password = getpass.getpass()

bot.login('rougailsaucix',password)

# bot.get_header_link('notifications')
notifs = bot.get_notifications()

if not notifs is False:
    for notif in notifs:
        print(notif)

bot.logout()

bot.stop_phantom()
