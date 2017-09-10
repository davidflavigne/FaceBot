#!/usr/bin/python3.5

import sys
import os 
import getpass

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path+'/../FaceBot/')

from FaceBot import FaceBot

def login(bot):
    login = input('Username or email:')
    password = getpass.getpass()
    return bot.login(login,password)

def test_login():
    bot = FaceBot()
    assert login(bot) == True

def test_logout():
    bot = FaceBot()
    login(bot)
    assert bot.logout() == True

def test_notifications():
    bot = FaceBot()
    login(bot)
    assert bot.get_notifications() != False

def test_message():
    pass
