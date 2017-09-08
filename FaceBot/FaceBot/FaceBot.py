#!/usr/bin/python3.5

#Class to access facebook with at least : login, logout, get post, message

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class FaceBot(webdriver.PhantomJS):
    """ 
           FaceBot class : instance for a facebot, provides
           functions to access facebook accounts, such as login, 
           logout...
           Inherits from webdriver.PhantomJS class

    """

    def __init__(self):
        self._url = 'https://mbasic.facebook.com/'
        webdriver.PhantomJS.__init__(self)

    def get(self, url):
        """ 
           overloading get method of selenium webdriver, 
           so we can modify the url to access mbasic version
           of facebook instead of normal version. (todo: finish
           this method)

        """
        super(FaceBot, self).get(url)

    def login(self,email,password):
        """ 
           login method. Allows to login to a facebook account

        """
        self.get(self._url)
        email_element = self.find_element_by_name("email")
        email_element.send_keys(email)
        pass_element = self.find_element_by_name("pass")
        pass_element.send_keys(password)
        pass_element.send_keys(Keys.ENTER)
        #self.save_screenshot('out.png')
        try:
            self.find_element_by_name("xc_message")
            print("Logged in")
            return True
        except NoSuchElementException as e:
            try:
                ok_element = self.find_element_by_tag_name('a')
                ok_element.send_keys(Keys.ENTER)
                try:
                    self.find_element_by_name("xc_message")
                    print("Logged in")
                    return True
                except:
                    print("Failed to login")
                    return False
            except:
                print("Failed to login")
                return False
            
    def logout(self):
        """ 
           logout method. Allows to logout from a facebook account

        """
        try:
            ok_element = self.find_element_by_partial_link_text('connexion')
            ok_element.send_keys(Keys.ENTER)
            print("Logged out")
            return True
        except:
            print("Failed to logout")
            return False
        
    def get_friend(self,name):
        """ 
           get_friend method. queries a facebook account for the given name, 
           to find a friend. return False if no friends were found.

        """
        url = "https://mbasic.facebook.com/friends/selector/?return_uri=%2Fmessages%2Fcompose%2F&cancel_uri=https%3A%2F%2Fm.facebook.com%2Fmessages%2F&friends_key=ids&context=select_friend_timeline&refid=11"
        self.get(url)
        q = self.find_element_by_name("query")
        q.send_keys(name)
        q.send_keys(Keys.ENTER)
        if "/messages/compose/?ids=" not in self.page_source:
            print ('You have no friend with this name')
            return False
        id = self.page_source.split("/messages/compose/?ids=")[1].split('"><span>')[0].split('"><span>')[0]
        return id
        
    def message(self,friend,message):
        """Send a message to a friend"""

        id = self.get_friend(friend)
        if id == 0:
            print('Failed to send a message')
            return False
        
        url = "https://mbasic.facebook.com/messages/compose/?ids=" + id
        self.get(url)
        try:
            t = self.find_element_by_name("body")
            t.send_keys(message)
            t.send_keys(Keys.ENTER)
            send = self.find_element_by_name("Send")
            send.send_keys(Keys.ENTER)
        except:
            print ('Error during message sending')
            return False
        return True

    def get_header(self):
        """ 
            Retrieves the header bloc of facebook page (blue bar on top of the
            page). Usefull to select links in that bloc (notifications)
        """
        try:
            res = self.find_element_by_id('header')
            return res
        except:
            return False

    def get_header_link(self,name):
        """ 
            Retrieves the given link in the header bloc of facebook page 
            (blue bar on top of the page). 
        """
        header = self.get_header()
        if (header == False):
            return False
        links = header.find_elements_by_tag_name('a')
        for link in links:
            if name in link.get_attribute('href'):
                return link
        return False
        
    def get_notifications(self):
        """ 
            Retrieves the notifications on the notification lists
        """
        notif_link = self.get_header_link('notifications')
        notif_link.send_keys(Keys.ENTER)
        try:
            notifs_list = self.find_element_by_id('notifications_list')
            notifs_all = notifs_list.find_elements_by_tag_name('a')
            notifs = []
            for notif in notifs_all:
                try:
                    href = notif.get_attribute('href')
                    if '/a/notifications.php' in href:
                        notifs.append(notif.text)
                except:
                    pass
            return notifs
        except:
            print('Could not get notifications list')
            return False
    def stop_phantom(self):
        """ 
            stops the phantom instance. Otherwise the process is still 
            running after the python script has ended.
        """
        self.quit()
