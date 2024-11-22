#!/usr/bin/python3
"""
Module: console.py
Author: Sheriff Abdulfatai
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ the commanded interpreter for this project """
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, line):
        """ exits the console """
        return True

    def do_EOF(self, line):
        """ exit the program """
        return True
        
if __name__ == "__main__":
    HBNBCommand().cmdloop()
