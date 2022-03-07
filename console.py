#!/usr/bin/python3
""" Console module package"""

import cmd
import os
import shlex

from attr import attr
# import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

dict_class = {"BaseModel": BaseModel(), "User": User(), "State": State(),
              "City": City(), "Amenity": Amenity(), "Place": Place(),
              "Review": Review()}


class HBNBCommand(cmd.Cmd):
    """ console """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """ Exits console """
        return True

    def emptyline(self):
        """ overwriting the emptyline """
        pass

    def do_quit(self, arg):
        """ Exit the program """
        return True

    def do_clear(self, arg):
        """Clear command"""
        os.system('clear')

    def do_create(self, arg):
        """Create a New Object"""
        if arg in dict_class:
            new_var = "{}()".format(arg)
            new_item = eval(new_var)
            new_item.save()
            print(new_item.id)
        elif len(arg) == 0:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show an object"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        splitted_arg = arg.split()
        if splitted_arg[0] not in dict_class:
            print("** class doesn't exist **")
            return
        if len(splitted_arg[1]) == 0:
            print("** instance id missing **")
            return
        new_str = "{}.{}".format(splitted_arg[0], splitted_arg[1])
        recuento = storage.all()
        if new_str in recuento.keys():
            print(recuento[new_str])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Under Development"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        splitted_arg = arg.split()
        if splitted_arg[0] not in dict_class:
            print("** class doesn't exist **")
            return
        if len(splitted_arg[1]) == 0:
            print("** instance id missing **")
        new_str = "{}.{}".format(splitted_arg[0], splitted_arg[1])
        recuento = storage.all()
        if new_str in recuento.keys():
            recuento.pop(new_str)
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all objects"""
        recuento = storage.all()
        new_list = []
        if len(arg) == 0:
            for key, value in recuento.items():
                new_list.append(value.__str__())
        else:
            if arg not in dict_class:
                print("** class doesn't exist **")
                return
            else:
                for key, value in recuento.items():
                    if arg == value.to_dict()["__class__"]:
                        new_list.append(value.__str__())
        print(new_list)

    def do_update(self, arg):
        """Update an object"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        splitted_arg = shlex.split(arg)
        if splitted_arg[0] not in dict_class:
            print("** class doesn't exist **")
            return
        if len(splitted_arg) == 1:
            print("** instance id missing **")
            return
        recuento = storage.all()
        key_compare = "{}.{}".format(splitted_arg[0], splitted_arg[1])
        if key_compare in recuento.keys():
            if len(splitted_arg) == 2:
                print("** attribute name missing **")
                return
            if len(splitted_arg) == 3:
                print("** value missing **")
                return
            setattr(recuento[key_compare], splitted_arg[2], splitted_arg[3])
            storage.save()
        else:
            print("** no instance found **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
