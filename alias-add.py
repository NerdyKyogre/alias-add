# -*- coding: utf-8 -*-
"""
Created on Wed Dec  11 12:31:31 2019

@author: NerdyKyogre
"""
"""
alias-add v0.0.3
This program appends aliases permanently to shell rc files of any user for those not comfortable hand editing config files. Supports bash and zsh on MacOS, Linux, and BSD.
"""

import os

def start():
    print("Welcome to alias-add. This program will permanently add your shell aliases so you don't have to.\nFirst, let's determine what sort of system you have.")
    sh = input("Are you using bash or zsh?\nIf you don't know and you are on a mac with MacOS 10.15 Catalina or later, you probably have zsh. Otherwise, you probably have bash.\nIf you are using bash, type b or bash. For zsh, type z or zsh.\n")
    while sh != "b"and sh != "bash" and sh != "z" and sh != "zsh":
        sh = input("That's not a valid shell. Are you using bash or zsh? ")
    user = input("What user would you like to add the alias(es) to? Note: In order to add to root, this program must be run as root.\n")
    if user == "root":
        rootlink = os.path.exists("/home/root")
        if rootlink == False:
            os.symlink("/root", "/home/root")
        else:
            linkexists = input("Error: link already exists at /home/root. Continue? Y/N: ")
            if linkexists != "Y" and linkexists != "y":
                print("Goodbye, and thank you for using alias-add.")
                exit()
    if sh == "b" or sh == "bash":
        bash(user)
    if sh == "z" or sh == "zsh":
        zsh(user)   
    if user == "root":
        if rootlink == False:
            os.unlink("/home/root")
    print("Goodbye, and thank you for using alias-add.")
        
def bash(user):
    with open("/home/"+user+"/.bashrc", "a") as shrc:
        shrc.write("\n# The following lines are aliases written by NerdyKyogre's alias-add. See github.com/NerdyKyogre/alias-add for more info.")
    while True:
        alias = input("What would you like your alias to be?\n")
        cmd = input("What would you like it to stand for?\n")
        with open("/home/"+user+"/.bashrc", "a") as shrc:
            shrc.write('\nalias "'+alias+'"="'+cmd+'"')
        redo = input("Alias set. Log out of your terminal and log back in to save changes.\nWould you like to set another alias before closing? Y/N: ")
        if redo != "Y" and redo != "y":
            break
    while True:
        extLine = input ("Would you like to add any more lines to your shell rc file? Y/N: ")
        if extLine == "N" or extLine == "n":
            break
        with open("/home/"+user+"/.bashrc", "a") as shrc:
            append = "null"
            while append != "Finish":
                append = input("Please input another line, or type 'Finish' to end the program: ")
                if append != "Finish":
                    shrc.write("\n"+append)
            break

def zsh(user):
    with open("/home/"+user+"/.zshrc", "a") as shrc:
        shrc.write("\n# The following lines are aliases written by NerdyKyogre's alias-add. See github.com/NerdyKyogre/alias-add for more info.")
    while True:
        alias = input("What would you like your alias to be?\n")
        cmd = input("What would you like it to stand for?\n")
        with open("/home/"+user+"/.zshrc", "a") as shrc:
            shrc.write('\nalias "'+alias+'"="'+cmd+'"')
        redo = input("Alias set. Log out of your terminal and log back in to save changes.\nWould you like to set another alias before closing? Y/N: ")
        if redo != "Y" and redo != "y":
            break
    while True:
        extLine = input ("Would you like to add any more lines to your shell rc file? Y/N: ")
        if extLine == "N" or extLine == "n":
            break
        with open("/home/"+user+"/.zshrc", "a") as shrc:
            append = "null"
            while append != "Finish":
                append = input("Please input another line, or type 'Finish' to end the program: ")
                if append != "Finish":
                    shrc.write("\n"+append)
            break
    
start()
