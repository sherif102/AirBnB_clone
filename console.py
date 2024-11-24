#!/usr/bin/python3
"""
Module: console.py
Author: Sheriff Abdulfatai
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ the commanded interpreter for this project """
    prompt = '(hbnb) '
    classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]
    methods = ["help", "?", "!", "quit", "EOF", "create", "show", "destroy", "update", "all"]

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
            if y.__class__.__name__ == args[0]:
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
            if y.__class__.__name__ == args[0]:
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


    def parseline(self, arg):
        """ defines a custome command input """
        value, sep, command = arg.partition('.')
        if (value.strip() not in self.methods) and '.' in arg:
            if command[:-2] == "count":
                # run  the command of count and return the number of class-name available
                count = 0
                all_objects = storage.all()
                obj_lists = list(all_objects.values())
                for x in obj_lists:
                    if x.__class__.__name__ == value.strip():
                        count += 1
                print(count)
                return self.cmdloop()
            elif command[:4] == "show":
                # run the command of show and return the object match
                try:
                    return command[:4], f'{value.strip()} {command[6:-2]}', arg
                except:
                    print("** no instance found **")
                    return self.cmdloop()
            elif command[:7] == "destroy":
                # run the command of destroy and update the file
                try:
                    return command[:7], f'{value.strip()} {command[9:-2]}', arg
                except:
                    print("** no instance found **")
                    return self.cmdloop()
            elif command[:6] == "update":
                # run the command of update and update the file
                update_values = command.split(' ')
                print(update_values)
                return self.cmdloop()

            
            return command[:-2].strip(), value.strip(), arg
        return super().parseline(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
