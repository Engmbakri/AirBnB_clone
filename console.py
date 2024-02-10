#!/usr/bin/python3
"""
The Console Module
"""

import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class HBNBCommand(cmd.Cmd):
    """
    HBNB Console Class
    """

    prompt = "(hbnb) "

    valid_classes = ["BaseModel", "User"]

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

    def do_update(self, args):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        Usage: update <class name> <id> <attribute name> <attribute value> """
        arg = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif arg[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key not in objects:
                print("**No Instance Found**")
            elif len(arg) < 3:
                print("**Attibute Name Missing**")
            elif len(arg) < 4:
                print("**Attribute Value Missing**")

            attr_name = arg[2]
            attr_value = arg[3]

            # Handle string arguments with spaces between double quotes
            if attr_value.startswith('"') and attr_value.endswith('"'):
                attr_value = attr_value[1:-1]
            # Convert attribute value to the appropriate type
            try:
                if '.' in attr_value:
                    attr_value = float(attr_value)
                else:
                    attr_value = int(attr_value)
            except ValueError:
                pass

            # Update the attribute if it's a simple type
            if isinstance(attr_value, (str, int, float)):
                obj = objects[key]
                setattr(obj, attr_name, attr_value)
                obj.save()
                print("Attribute updated successfully!")
            else:
                print("Invalid attribute value type."
                      "Only string, integer, and float are allowed.")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
