#!/usr/bin/python3
"""
Module: console.py
Author: Sheriff Abdulfatai
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """ the commanded interpreter for this project """
    prompt = '(hbnb) '
    classes = ["BaseModel", "User"]

    def emptyline(self):
        pass

    def do_quit(self, line):
        """ exits the console """
        return True

    def do_EOF(self, line):
        """ exit the program """
        return True

    def do_create(self, arg):
        """ creates a new instance of BaseModel, saves it to JSON file
        and prints the id
        Eg: $ create BaseModel """
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            obj = eval(arg)()
            storage.new(obj)
            storage.save()
            print(obj.id)

    def do_show(self, arg):
        """ prints the string representation of an instance based on the
        class name and id
        Eg: $ show BaseModel 1234-1234-1234 """
        args = arg.split(' ')
        ids = []

        storage.reload()
        obj_dict = storage.all()

        for x in obj_dict.keys():
            y = obj_dict[x]
            ids.append(y.id)

        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[1] not in ids:
            print("** no instance found **")
        else:
            print(obj_dict.get(f"{args[0]}.{args[1]}"))

    def do_destroy(self, arg):
        """ deletes an instance based on teh class name
        and id and save the changes back to JSON file
        Eg: $ destory BaseModel 1234-1234-1234 """
        args = arg.split(' ')
        ids = []

        storage.reload()
        obj_dict = storage.all()

        for x in obj_dict.keys():
            y = obj_dict[x]
            ids.append(y.id)

        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[1] not in ids:
            print("** no instance found **")
        else:
            del obj_dict[f"{args[0]}.{args[1]}"]
            storage.save()

    def do_all(self, arg):
        """ prints all string representation of all
        instances based or not on the class name
        Eg: $ all BaseModel or $ all """
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
        else:
            list_obj = []
            storage.reload()
            obj_dict = storage.all()
            for y in obj_dict.values():
                if arg and str(y.__class__.__name__) == str(arg):
                    list_obj.append(str(y))
                if not arg:
                    list_obj.append(str(y))
            print(list_obj)

    def do_update(self, arg):
        """ updates an instance based on teh class name and id by adding
        or updating attribute and save it back to the JSON file
        Eg: $ update BaseModel 1234-1234-1234 email "aibnb@gmail.com" """
        args = arg.split(' ')
        ids = []

        storage.reload()
        obj_dict = storage.all()

        for x in obj_dict.keys():
            y = obj_dict[x]
            ids.append(y.id)

        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[1] not in ids:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj = obj_dict.get(f"{args[0]}.{args[1]}")
            setattr(obj, args[2], type(f'{obj}.{args[2]}')(args[3]))
            obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
