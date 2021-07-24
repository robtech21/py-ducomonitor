#!/usr/bin/env python3

import sys
import duco_api
from os import system
from time import sleep

debug = False
delay = False

if '--debug' in sys.argv:
    debug = True
if '--delay' in sys.argv:
    delay = True

def figlet(text):
    system('figlet -f big.flf -w 999 '+str(text))

def clr():
    system('clear')

user    = input('user> ')
passwd  = input('pass> ')

clr()
while True:
    try:
        if debug:
            print("Connecting")
        api_connection = duco_api.Wallet()
        if debug:
            print("Logging in")
        api_connection.login(username=str(user), password=str(passwd))
        price = api_connection.get_duco_price()
        bal   = api_connection.get_balance()
        value = float(bal) * float(price)
        sleep(0.5)
        clr()
        figlet(text="'User:  '"+str(user))
        if delay:
            sleep(0.5)
        figlet(text="'Duco:  '"+str(bal))
        if delay:
            sleep(0.5)
        figlet(text="'Price: $'"+str(price))
        if delay:
            sleep(0.5)
        figlet(text="'Money: $"+str(value)+"'")
    except Exception as e:
        if debug:
            print("Failed: "+str(e))
        pass
