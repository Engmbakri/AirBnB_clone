#!/usr/bin/python3

import cmd
import json
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    valid_classes = ["BaseModel"]

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
            
    def emptyline(self):
        """execute nothing when empty line"""
        pass
    
    def do_create(self, args):
        """create a new method type <create> <class name>"""
        arg = args.split()
        if not arg:
            print("** class name missing **")
            return
        
        if arg[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg[0])().id)   
        storage.save()
    
    def do_show(self, args):
        """
        Prints the string representation based on the class name and id.
        """
        arg = args.split()

        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(arg[0], arg[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")
    
    def do_destroy(self, args):
        """Deletes an instance based on the class name and id 
        syntax destory <class_name> <id>"""
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("**no instance found**")

    def do_all(self, args):
        """
        Print the string representation of all instances or a specific class.
        """
        objects = storage.all()
        arg = args.split()

        if len(arg) == 0:
            for key, value in objects.items():
                print(str(value))
        elif arg[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == arg[0]:
                    print(str(value))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
