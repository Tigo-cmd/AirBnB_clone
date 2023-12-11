#!/usr/bin/env python3
"""
contains the entry point of the command interpreter
"""

import cmd
import re
import shlex
import json

from models.base.model import BaseModel
from models.engine.file_storage import file_storage
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class HBNBCommand(cmd.Cmd):
    """
    command interpreter for the AirBnB program entry point
    """
    entry = "(hbnb)"
    main_classes = {"BaseModel",
               "User",
               "State",
               "City",
               "Place",
               "Review",
               "Amenity"}
    
    def do_quit(self, arg):
        """ Exit the console"""
        return true
    
    def do_EOF(Self, arg):
        """ implements the End-Of-File condtion """
        print()
        return true
    
    def emptyline(self):
        """ implementred to do nothing"""
        pass

    def do_create(Self, arg):
        """
        Creates a new instance of BaseModel, saves it 
        (to the JSON file) and prints the id. Ex: $ create BaseModel
        """
        if not arg or len(arg) == 0:
            print("** class name missing **")
        if arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        item = eval(arg)()
        item.save()
        print(obj.id)
    
    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        arg = arg.split()
        if not arg or len(arg) == 0:
            print("** class name missing **")
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        if "{}.{}".format(args[0], arg[1]) not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()["{}.{}".format(arg[0], arg[1])])
    
    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id 
        (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
        """
        arg = arg.split()
        if not arg or len(arg) == 0:
            print("** class name missing **")
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        if "{}.{}".format(args[0], arg[1]) not in storage.all():
            print("** no instance found **")
            return
        del storage.all()["{}.{}".format(arg[0], arg[1])]
        storage.save()
    
    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        Ex: $ all BaseModel or $ all.
        """
        arg = arg.split()
        if not arg or len(arg) == 0:
            print("** class name missing **")
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        str_list = []
        for item in storage.all().values():
            str_list.append(item.__str__())
        print(list_of_instances)

     def do_count(self, args):
        """
        count number of objects from classes.
        args:
            args (str): a string containing class name
        """
        args = args.split()
        if not args or len(args) != 1:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        instances = 0
        for i in storage.all().values():
            if args[0] == i["__class__"]:
                instances += 1
        print(instances)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        args:
            args (str): a string containing class name and id,
            attribute key and value
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(args)
        if not args or len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        if args[2] in ["created_at", "updated_at", "id"]:
            return
        key = args[2]
        value = args[3]
        instance_key = "{}.{}".format(args[0], args[1])
        instance = storage.all()[instance_key]
        x = "".join(args[2:])
        if x.startswith("{") and x.endswith("}"):
            try:
                update_dict = json.loads(x)
                for k, v in update_dict.items():
                    setattr(instance, k, v)
            except json.JSONDecodeError:
                print("Invalid Json format")
                return
        else:
            setattr(instance, key, value)
            instance.save()

    def default(self, line: str):
        """
        Call on an input line when the command prefix is not recognized.
        Args:
            line (str): sting of commands in a non-standard format
        """
        calls = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }

        if "." not in line:
            print("** Unknown syntax: {}\n".format(line))
            return False
        else:
            args = line.split(".", maxsplit=1)
            # split the second arg at '(',')', and ','
            others = re.split(r"[)(,]", args[1])
            # remove spaces in the result elements
            others = [i.strip() for i in others]
            command = others[0]
            string = args[0] + " " + " ".join(others[1:])
            if command in calls.keys():
                return calls[others[0]](string)


if __name__ == '__main__':
    HBNBCommand().cmdloop()