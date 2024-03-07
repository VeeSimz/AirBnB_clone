#!/usr/bin/python3
""" This module writes a program that prints to the console"""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel


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
    """ Program that implements a console terminal. """

    prompt = "(hbnb) "
    my_classes = {"BaseModel": BaseModel}

    def emptyline(self):
        """Empty line"""
        pass

    def do_create(self, argu):
        """This method creates a new instance of BaseModel"""
        try:
            if not argu:
                raise SyntaxError()

            new_list = argu.split(" ")

            class_name = new_list[0]
            if class_name not in self.my_classes:
                raise NameError()

            new_instance = self.my_classes[class_name]()
            new_instance.save()
            print(new_instance.id)

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, argu):
        """ This shows the string representation of an instance of class """
        arg_var = parse(argu)
        obje_dict = storage.all()

        if len(arg_var) == 0:
            print("** class name missing **")
        elif arg_var[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        elif len(arg_var) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_var[0], arg_var[1]) not in obje_dict:
            print("** no instance found **")
        else:
            print(obje_dict["{}.{}".format(arg_var[0], arg_var[1])])

    def do_destroy(self, argu):
        """ This method is used to delete an instance based
        on the class name and id """
        arg_var = parse(argu)
        obje_dict = storage.all()

        if len(arg_var) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        elif len(arg_var) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in obje_dict.keys():
            print("** no instance found **")
        else:
            del obje_dict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, argu):
        """ This method prints all string representations of
        instances based or not on the class name """
        arg_var = parse(argu)

        if len(arg_var) > 0 and arg_var[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        else:
            new_obj = []
            for obj in storage.all().values():
                if len(arg_var) > 0 and arg_var[0] == obj.__class__.__name__:
                    new_obj.append(obj.__str__())
                elif len(arg_var) == 0:
                    new_obj.append(obj.__str__())
            print(new_obj)

    def do_update(self, argu):
        """ This update the class name, id, attribute nem, attribute value """
        arg_var = parse(argu)
        stored_dic = storage.all()

        if len(arg_var) == 0:
            print("** class name missing **")
            return False
        if arg_var[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
            return False
        if len(arg_var) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_var[0], arg_var[1]) not in stored_dic.keys():
            print("** no instance found **")
            return False
        if len(arg_var) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_var) == 3:
            print("** value missing **")
            return False
        if len(arg_var) == 4:
            obj = stored_dic["{}.{}".format(arg_var[0], arg_var[1])]
            if arg_var[2] in obj.__class__.__dict__.keys():
                val_in = type(obj.__class__.__dict__[arg_var[2]])
                obj.__dict__[arg_var[2]] = val_in(arg_var[3])
            else:
                obj.__dict__[arg_var[2]] = arg_var[3]
        elif type(eval(arg_var[2])) == dict:
            obj = stored_dic["{}.{}".format(arg_var[0], arg_var[1])]
            for el, em in eval(arg_var[3]).items():
                if (el in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[el]) in {str, int, float}):
                    val_in = type(obj.__class__.__dict__[el])
                    obj.__dict__[el] = val_in(em)
                else:
                    obj.__dict__[el] = em
        storage.save()

    @staticmethod
    def do_quit(_):
        """Quit command to exit the program"""
        exit()

    @staticmethod
    def do_EOF(_):
        """Exits the program by the system, control D, Z"""
        print("")
        exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
