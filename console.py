#!/usr/bin/python3
""" This module writes a program that prints to the console"""

import cmd, sys
#from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Program that implements a console terminal. """

    prompt = "(hbnb) "

    def emptyline(self):
        """Empty line"""
        pass

    @staticmethod
    def do_quit(_):
        """Quit command to exit the program"""
        exit()

    @staticmethod
    def do_EOF(_):
        """Exits the program"""
        print("")
        exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
