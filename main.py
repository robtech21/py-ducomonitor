#!/usr/bin/env python3

import sys
import duco_api
from os import system
from time import sleep

timerAmount = 0

def figlet(text):
    system('figlet -w 999 '+str(text))

def clr():
    system('clear')

user    = input('user> ')
passwd  = input('pass> ')

clr()
while True:
    try:
        api_connection = duco_api.api_actions()
        api_connection.login(username=str(user), password=str(passwd))

        price = duco_api.get_duco_price()
        bal   = api_connection.balance()
        value = float(bal) * float(price)
        sleep(0.5)
        clr()
        figlet(text="'User:  '"+str(user))
        figlet(text="'Duco:  '"+str(bal))
        figlet(text="'Price: $'"+str(price))
        figlet(text="'Money: $"+str(value)+"'")
    except Exception as e:
        if '--debug' in sys.argv:
            print(e)
        pass
