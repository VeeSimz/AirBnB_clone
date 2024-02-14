#!/usr/bin/python3

import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) " if sys.__stdin__.isatty() else ""

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
