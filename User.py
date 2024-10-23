# -*- coding: utf-8 -*-
"""
Created for the community of Ravers!!
Enjoy it!

@author: Deneider
"""

#%%% User class

#  User
class User:
    def __init__(self, name, password, hoursListening):
        self.name = name
        self.name = password
        self.hoursListening = hoursListening

# Admin user is a type of user
class Admin(User):
    def __init__(self, name, password, hoursListening, admin = True):
        super().__init__(name, password, hoursListening)
        self.admin = admin
        


