# -*- coding: utf-8 -*-
"""
Created for the community of Ravers!!
Enjoy it!

@author: Deneider
"""

#%%% Imports
from User import * 


# %%% default admin

superAdmin = Admin(name = "Deneider", password= "123456", hoursListening= 0)

# %%% Start the programm

print("Welcome to No ADS radio.")
# I used the strip().lower() for not have a problems with the key sensitive
welcome = input("1. LogIn or 2. SignUp ").strip().lower() 

if welcome == "login" or welcome == "1" :
    print("Start session... ")
    
elif welcome == "signup" or welcome == "2":
    print("Okey, let's go to create an account.")
    
else:
    print("Sorry, I don't understand you.")
    





