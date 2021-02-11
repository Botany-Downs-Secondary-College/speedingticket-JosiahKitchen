# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 14:34:05 2021

@author: josiah
"""

import math

wanted_list = ("|")
admin_code = 73
loop = 1
loop2 = 2
name = input("Please enter your name")
admin = input("Please press enter")

while loop == 1:
    if name in wanted_list:
        print("You are required to go to jail")
        
    elif admin == admin_code:
        while loop2 == 2:
            print("1. Set Speed Limit \n 2. View Crime List")
            choice = input("Select program")
            try:
                choice = int(choice)
                loop2 = 3
            else:
                continue
                
        if choice == 1:
            speed_limit = input("Enter Speed Limit")
            
        elif choice == 2:
            print(wanted_list)
    else:
        speed = input("Enter speed")
        if speed <= speed_limit + (speed_limit / 10):
            print("Below speed limit \n Enjoy your day")
            
        elif speed >= speed_limit and speed <= (speed_limit + 30):
            print("You are over the speed limit by {1} km/h \n You will be fined ${2}".format(
        
        
        
        
        
        
        
