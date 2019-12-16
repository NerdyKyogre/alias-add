# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 09:54:22 2019

@author: NerdyKyogre
"""
"""
alias-add v1.0.0
This program appends aliases permanently to shell rc files of any user for those not comfortable hand editing config files. Supports bash and zsh on MacOS, Linux, and BSD.
"""

import os
import sys

def main():
    argCount = len(sys.argv) - 1
    if argCount != 4 or sys.argv[1] == "--help" or sys.argv[1] == "-h" or sys.argv[1] == "help":
        print("Usage: (sudo) python3 alias-add.py [user] [shell] ['alias'] ['command']")
        exit()
    user = sys.argv[1]
    if user == "root":
        rootlink = os.path.exists("/home/root")
        if rootlink == False:
            os.symlink("/root", "/home/root")
        else:
            linkexists = input("Error: link already exists at /home/root. Continue? Y/N: ")
            if linkexists != "Y" and linkexists != "y":
                exit()
    shell = sys.argv[2]
    if shell != "bash" and shell != "zsh":
        print("That's not a valid shell. Please use bash or zsh.")
        exit()
    alias = sys.argv[3]
    target = sys.argv[4]
    
    with open("/home/"+user+"/."+shell+"rc", "a") as shrc:
        shrc.write("\n# The following alias was written by NerdyKyogre's alias-add. See github.com/NerdyKyogre/alias-add for more info.")
        shrc.write('\nalias "'+alias+'"="'+target+'"' )
    
    print("Done. Alias "+alias+" mapped to "+target+" for "+user+"'s "+shell+".")
    
    if user == "root" and rootlink == False:
        os.unlink("/home/root")
    
main()
