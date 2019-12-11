#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 19:44:05 2019

@author: NerdyKyogre
"""
"""
alias-add v0.0.1
This program appends aliases permanently to shell rc files of any user for those not comfortable hand editing config files. Supports bash and zsh on MacOS, Linux, and BSD.
"""
def start():
    print("Welcome to alias-add. This program will permanently add your shell aliases so you don't have to.\nFirst, let's determine what sort of system you have.")
    sh = input("Are you using bash or zsh?\nIf you don't know and you are on a mac with MacOS 10.15 Catalina or later, you probably have zsh. Otherwise, you probably have bash.\nIf you are using bash, type b or bash. For zsh, type z or zsh.\n")
    user = input("What user would you like to add the alias(es) to? Note: In order to add to root, this program must be run as root.\n")
    if sh == "b" and user != "root" or sh == "bash" and user != "root":
        bash(user)
    if sh == "z" and user != "root" or sh == "zsh" and user != "root":
        zsh(user)
    if sh == "b" and user == "root" or sh == "bash" and user == "root":
        bashroot()
    if sh == "z" and user == "root" or sh == "zsh" and user == "root":
        zshroot()

    print("Goodbye.")
        
def bash(user):
    with open("/home/"+user+"/.bashrc", "a") as shrc:
        shrc.write("\n# The following lines are aliases written by NerdyKyogre's alias-add. See the github for more info.")
    while True:
        alias = input("What would you like your alias to be?\n")
        cmd = input("What would you like it to stand for?\n")
        with open("/home/"+user+"/.bashrc", "a") as shrc:
            shrc.write('\nalias "'+alias+'"="'+cmd+'"')
        redo = input("Alias set. Log out of your terminal and log back in to save changes.\nWould you like to set another alias before closing? Y/N: ")
        if redo != "Y" and redo != "y":
            break

def zsh(user):
    with open("/home/"+user+"/.zshrc", "a") as shrc:
        shrc.write("\n# The following lines are aliases written by NerdyKyogre's alias-add. See the github for more info.")
    while True:
        alias = input("What would you like your alias to be?\n")
        cmd = input("What would you like it to stand for?\n")
        with open("/home/"+user+"/.zshrc", "a") as shrc:
            shrc.write('\nalias "'+alias+'"="'+cmd+'"')
        redo = input("Alias set. Log out of your terminal and log back in to save changes.\nWould you like to set another alias before closing? Y/N: ")
        if redo != "Y" and redo != "y":
            break
    
def bashroot():
    with open("/root/.bashrc", "a") as shrc:
        shrc.write("\n# The following lines are aliases written by NerdyKyogre's alias-add. See the github for more info.")
    while True:
        alias = input("What would you like your alias to be?\n")
        cmd = input("What would you like it to stand for?\n")
        with open("/root/.bashrc", "a") as shrc:
            shrc.write('\nalias "'+alias+'"="'+cmd+'"')
        redo = input("Alias set. Log out of your terminal and log back in to save changes.\nWould you like to set another alias before closing? Y/N: ")
        if redo != "Y" and redo != "y":
            break
    
def zshroot():
    with open("/root/.zshrc", "a") as shrc:
        shrc.write("\n# The following lines are aliases written by NerdyKyogre's alias-add. See the github for more info.")
    while True:
        alias = input("What would you like your alias to be?\n")
        cmd = input("What would you like it to stand for?\n")
        with open("/root/.zshrc", "a") as shrc:
            shrc.write('\nalias "'+alias+'"="'+cmd+'"')
        redo = input("Alias set. Log out of your terminal and log back in to save changes.\nWould you like to set another alias before closing? Y/N: ")
        if redo != "Y" and redo != "y":
            break
    
start()