#!/usr/bin/python3
"""This module contains the HBNBCommand class."""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB console."""
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
        }

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module that accept arg"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl+D)."""
        print()
        return True

    def help_quit(self):
        """Print help message for the quit command."""
        print("Exit the program.")

    def help_EOF(self):
        """Print help message for the EOF"""
        print("Exit the program using EOF (Ctrl+D).")

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it and print the id."""
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """Print the string representation of an instance."""
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        arg_len = parse(arg)
        obje_dict = storage.all()
        if len(arg_len) == 0:
            print("** class name missing **")
        elif arg_len[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_len) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_len[0], arg_len[1]) not in obje_dict.keys():
            print("** no instance found **")
        else:
            del obje_dict["{}.{}".format(arg_len[0], arg_len[1])]
            storage.save()

    def do_all(self, arg):
        """Prints string representation of all instances."""
        arg_len = parse(arg)
        if len(arg_len) > 0 and arg_len[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_len = []
            for obj in storage.all().values():
                if len(arg_len) > 0 and arg_len[0] == obj.__class__.__name__:
                    obj_len.append(obj.__str__())
                elif len(arg_len) == 0:
                    obj_len.append(obj.__str__())
            print(obj_len)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        arg_len = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arg_len[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        arg_len = parse(arg)
        obje_dict = storage.all()

        if len(arg_len) == 0:
            print("** class name missing **")
            return False
        if arg_len[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_len) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_len[0], arg_len[1]) not in obje_dict.keys():
            print("** no instance found **")
            return False
        if len(arg_len) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_len) == 3:
            try:
                type(eval(arg_len[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_len) == 4:
            obj = obje_dict["{}.{}".format(arg_len[0], arg_len[1])]
            if arg_len[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg_len[2]])
                obj.__dict__[arg_len[2]] = valtype(arg_len[3])
            else:
                obj.__dict__[arg_len[2]] = arg_len[3]
        elif type(eval(arg_len[2])) == dict:
            obj = obje_dict["{}.{}".format(arg_len[0], arg_len[1])]
            for k, v in eval(arg_len[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
