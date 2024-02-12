#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def emptyline(self):
        """Empty line"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        print("")
        return True

    def do_EOF(self, line):
        """Exits the program"""
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
