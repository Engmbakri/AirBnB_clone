#!/usr/bin/python3
"""
Console Module
"""
import cmd
import re
import shlex
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


def split_curly_braces(extra_argument):
    """
    Splits Curly Braces For The Update Method
    """
    curly_braces = re.search(r"\{(.*?)\}", extra_argument)

    if curly_braces:
        id_with_comma = shlex.split(extra_argument[:curly_braces.span()[0]])
        identifier = [i.strip(",") for i in id_with_comma][0]

        str_data = curly_braces.group(1)
        try:
            argument_dict = ast.literal_eval("{" + str_data + "}")
        except Exception:
            print("**  invalid dictionary format **")
            return
        return identifier, argument_dict
    else:
        arg_list = extra_argument.split(",")
        if arg_list:
            try:
                identifier = arg_list[0]
            except Exception:
                return "", ""
            try:
                attribute_name = arg_list[1]
            except Exception:
                return identifier, ""
            try:
                attribute_value = arg_list[2]
            except Exception:
                return identifier, attribute_name
            return f"{identifier}", f"{attribute_name} {attribute_value}"


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand Console Class
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "Amenity",
                     "Place", "Review", "State", "City"]

    def emptyline(self):
        """
        Do nothing When Empty Line Is Entered.
        """
        pass

    def do_EOF(self, args):
        """
        EOF (Ctrl+D) Exit The Program.
        """
        return True

    def do_quit(self, args):
        """
        Quit Command To Exit The Program.
        """
        return True

    def do_create(self, args):
        """
        Create new Instance of BaseModel and save it to JSON file.
        Usage: create <class_name>
        """
        arg_list = shlex.split(args)

        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{arg_list[0]}()")
            storage.save()
            print(new_instance.id)

    def do_show(self, args):
        """
        Show the string representation of an Instance.
        Usage: show <class_name> <id>
        """
        arg_list = shlex.split(args)

        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(arg_list[0], arg_list[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """
        Delete Instance based on the Class Name and Id.
        Usage: destroy <class_name> <id>
        """
        arg_list = shlex.split(args)

        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(arg_list[0], arg_list[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """
        Print the string representation of all Instances or a Specific Class.
        Usage: <User>.all()
                <User>.show()
        """
        objects = storage.all()

        arg_list = shlex.split(args)

        if len(arg_list) == 0:
            for key, value in objects.items():
                print(str(value))
        elif arg_list[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == arg_list[0]:
                    print(str(value))

    def do_count(self, args):
        """
        Counts Number of Instances of a class
        usage: <class name>.count()
        """
        objects = storage.all()

        arg_list = shlex.split(args)

        if args:
            class_name = arg_list[0]

        count = 0

        if arg_list:
            if class_name in self.valid_classes:
                for obj in objects.values():
                    if obj.__class__.__name__ == class_name:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

    def do_update(self, args):
        """
        Update an Instance by adding or updating an attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        arg_list = shlex.split(args)

        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(arg_list[0], arg_list[1])
            if key not in objects:
                print("** no instance found **")
            elif len(arg_list) < 3:
                print("** attribute name missing **")
            elif len(arg_list) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                curly_braces = re.search(r"\{(.*?)\}", args)

                if curly_braces:
                    try:
                        str_data = curly_braces.group(1)

                        arg_dict = ast.literal_eval("{" + str_data + "}")

                        attribute_names = list(arg_dict.keys())
                        attribute_values = list(arg_dict.values())
                        try:
                            attr_name1 = attribute_names[0]
                            attr_value1 = attribute_values[0]
                            setattr(obj, attr_name1, attr_value1)
                        except Exception:
                            pass
                        try:
                            attr_name2 = attribute_names[1]
                            attr_value2 = attribute_values[1]
                            setattr(obj, attr_name2, attr_value2)
                        except Exception:
                            pass
                    except Exception:
                        pass
                else:

                    attribute_name = arg_list[2]
                    attribute_value = arg_list[3]

                    try:
                        attribute_value = eval(attribute_value)
                    except Exception:
                        pass
                    setattr(obj, attribute_name, attribute_value)

                obj.save()

    def default(self, args):
        """
        Default Behavior for CMD module when input is invalid
        """
        arg_list = args.split('.')

        class_name = arg_list[0]

        command = arg_list[1].split('(')

        command_method = command[0]

        extra_argument = command[1].split(')')[0]

        method_dict = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
                }

        if command_method in method_dict.keys():
            if command_method != "update":
                return method_dict[command_method](
                    "{} {}".format(class_name, extra_argument))
            else:
                if not class_name:
                    print("** class name missing **")
                    return
                try:
                    identifier, argument_dict = split_curly_brace
                    (extra_argument)
                except Exception:
                    pass
                try:
                    call = method_dict[command_method]
                    return call("{} {} {}".format(
                        class_name,
                        identifier,
                        argument_dict
                        ))
                except Exception:
                    pass
        else:
            print("*** Unknown syntax: {}".format(argument))
            return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
