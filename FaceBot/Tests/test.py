#!/usr/bin/python3.5

from FaceBot import FaceBot
import getpass

#from selenium import webdriver


#print dir(webdriver.PhantomJS)

bot = FaceBot()

password = getpass.getpass()

bot.login('rougailsaucix',password)

# print ('Friend id:' + bot.get_friend('Céliane'))
# bot.message('Céliane','Coucou')

# bot.get_header_link('notifications')
notifs = bot.get_notifications()

if not notifs is False:
for notif in notifs:
    print(notif)

bot.logout()

bot.stop_phantom()
