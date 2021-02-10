# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 14:34:05 2021

@author: josia
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
                print("Enter as number")
                
        while loop2 == 3:
            if choice == 1:
                speed_limit = input("Enter Speed Limit")
            
            elif  
    else:
        speed = input("Enter speed")
        if speed <= 