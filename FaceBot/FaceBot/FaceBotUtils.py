#!/usr/bin/python3.5

import FaceBot
import shlex

class Router:
    """ Class Router : redirects user input to corresponding callbacks, if any """
    @staticmethod
    def route(bot,command):
        """ 
           route method : main method of class Router, static method that does
           the actual redirection

        """
        args = shlex.split(command)
        if args[0] == 'message':
            return Router.messager(bot,args)
        elif args[0] == 'notifications':
            return Router.notifications(bot)
        elif args[0] == 'discuter':
            return Router.discuter(bot,args)
        elif args[0] == 'friends':
            return Router.friends(bot)
        elif args[0] == 'list' or args[0] == 'help':
            return Router.usage()
        else:
            print('Bad command name: type "list" to get full commands list')
            return False

    @staticmethod
    def discuter(bot,args):
        """
        Sends given message 3 times to the last conversation in your message page
        """
        if len(args) < 2:
            print('Usage : discuter <message>')
            return False
        return bot.chat_last(args[1])
    @staticmethod
    def friends(bot):
        return bot.get_friend_list();
        
    @staticmethod
    def messager(bot,args):
        """
        Checks arguments and call the bot method to send a private message to the named friend (if existing)
        """
        if len(args) < 3:
            print('Usage : message <friendname> <message body>')
            return False
        return bot.message(args[1],args[2])
        
    @staticmethod
    def usage():
        """
        Prints list of available commands
        """
        print('Commands list:')
        print('    notifications: print last notifications')
        print('    message: send a message to a friend')
        print('    discuter: spam a message to the last friend you had a conversation with')
        print('    friends: display a list of your friends')
        print('    list: print this list')
        print('    stop: stop the bot and logout')
        return True
    
    @staticmethod
    def notifications(bot):
        """
        Calls the bot method to retrieve notifications and displays them, if any
        """
        notifs = bot.get_notifications()
        if not notifs is False:
            for notif in notifs:
                print('        '+notif)
                return True
            else:
                print('No notifications found')
                return False
            
        
