#!/usr/bin/python3

import cmd
import json
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    #def __init__(self):
    #    self.user = {}

    def do_EOF(self, line):
        """EOF command to exit the program"""
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
        if not args:
            print("** class name missing **")
            return
        
        class_name = arg[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
        else:
            print(eval(arg[0])().id)   
        storage.save()
    
    def do_show(self, args):
        """prints the string representation based on the class name and id
        syntax show <class name> <id>"""
        arg = args.split()
        
        if not args:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        #elif arg[1] and arg[0] != "objects":
            #print("** no instance found **") 
        else:
            print("{}{}".format(arg[0], arg[1]))
    
    def do_destroy(self, args):
        """Deletes an instance based on the class name and id 
        syntax destory <class_name> <id>"""
        arg = args.split()
        if not args:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) > 2:
            print("** instance id missing **")
        #elif arg[1] != "objects":
            #print("** no instance found **")
        else:
            del self.objects["{}{}".format(arg[0], arg[1])]
        storage.save()

    #def all(self, args):

        


if __name__ == "__main__":
    HBNBCommand().cmdloop()
