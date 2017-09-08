#!/usr/bin/python3.5

import FaceBot
import shlex

class Router:
    """ Class Router : redirects user input to corresponding callbacks, if any """
    _routes = {}
    @staticmethod
    def route(bot,command):
        """ 
           route method : main method of class Router, static method that does
           the actual redirection

        """
        args = shlex.split(command)
        if args[0] == 'message':
            if len(args) < 3:
                print('Usage : message <friendname> <message body>')
                return False
            return bot.message(args[1],args[2])
            #print (args)
            return True
        elif args[0] == 'notifications':
            notifs = bot.get_notifications()
            if not notifs is False:
                for notif in notifs:
                    print('        '+notif)
                return True
            else:
                print('No notifications found')
                return False
        elif args[0] == 'list' or args[0] == 'help':
            print('Commands list:')
            print('    notifications: print last notifications')
            print('    message: send a message to a friend')
            print('    list: print this list')
            print('    stop: stop the bot and logout')
            return True
        else:
            print('Bad command name: type "list" to get full commands list')
            return False
    
    pass
