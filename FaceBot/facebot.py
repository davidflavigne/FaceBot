#!/usr/bin/python3.5

"""
   The FaceBot module allows you to connect to 
   your facebook account and do several actions on it:
       send a message to a friend
       get your notifications list

"""

import FaceBot.FaceBotUtils
import FaceBot.FaceBot
import FaceBot
import getpass

if __name__ == "__main__":
    bot = FaceBot.FaceBot.FaceBot()
    continuer = True
    logged = False
    while(not logged):
        login = input('Type in your username : ')
        password = getpass.getpass()
        logged = bot.login(login,password)
    
    while(continuer):
        command = input(login+'@FaceBot > ')
        if command == 'stop':
            continuer = False
        else:
            res = FaceBot.FaceBotUtils.Router.route(bot,command)
            if res :
                print (command + ' done')
            else :
                print (command + ' failed')

    bot.logout()
    bot.stop_phantom()
