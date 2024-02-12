#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def emptyline(self):
        """Empty line"""
        pass

    @staticmethod
    def do_quit(_):
        """Quit command to exit the program"""
        return True

    @staticmethod
    def do_EOF(_):
        """Exits the program"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
