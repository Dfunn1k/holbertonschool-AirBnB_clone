#!/usr/bin/python3
"""
User this module for console

(HBNB CONSOLE)
"""
import cmd
import re
from models import storage
from models import dict_class


class HBNBCommand(cmd.Cmd):
    """
    Template for instances that inherit from the Cmd class in the cmd module,
    so you can run a console

    Attributes:
        prompt (str): The prompt issued to solicit input.
    """
    prompt = '(hbnb) '

    def do_create(self, line):
        """
        Creates a new instance of BaseModel and Storage in JSON file.

        Usage:
            (hbnb) <classname>.create()
            (hbnb) create <classname>
        """
        tokens = line.split()
        if self.checker(tokens, 1):
            obj = dict_class[tokens[0]]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance

        Usage:
            (hbnb) <classname>.show("id")
            (hbnb) show <classname> id
        """
        tokens = line.split()
        if self.checker(tokens, 2):
            print(storage.all()[tokens[0] + "." + tokens[1]])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id

        Usage:
            (hbnb) <classname>.destroy("id")
            (hbnb) destroy <classname> id
        """
        tokens = line.split()
        if self.checker(tokens, 2):
            del storage.all()[tokens[0] + "." + tokens[1]]
            storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances by classname

        Usage:
            (hbnb) <classname>.all()
            (hbnb) all <classname>
        """
        tokens = line.split()
        if len(tokens) == 0:
            all_objs = storage.all()
            for obj in all_objs.values():
                print(obj)
        elif self.checker(tokens, 1):
            all_objs = storage.all()
            for obj_key in all_objs.keys():
                model_name = obj_key.partition(".")[0]
                if model_name == tokens[0]:
                    print(all_objs[obj_key])

    def do_update(self, line):
        """
        Updates an instance(add or set attribute)

        Usage:
            (hbnb) <classname>.update("id", "Attribute", "Value")
            (hbnb) update <classname> id Attribute Value
        """
        tokens = line.split()
        if self.checker(tokens, 3):
            all_objs = storage.all()
            obj = all_objs[tokens[0] + "." + tokens[1]]
            key, value = tokens[2], tokens[3]
            if value[0] == '"' and value[-1] == '"':
                value = value[1:-1]
            elif self.is_integer(value):
                value = int(value)
            elif self.is_float(value):
                value = float(value)
            setattr(obj, key, value)
            obj.save()

    def do_count(self, line):
        """Shows the number of instances por class.

        Usage:
            (hbnb) <classname>.count()
            (hbnb) count <classname>
        """
        tokens = line.split()
        if (len(tokens) != 1):
            cmd.Cmd.do_help(self, "count")
        else:
            count = 0
            cls_name = tokens[0]
            for value in storage.all().values():
                if value.__class__.__name__ == cls_name:
                    count += 1
            print(count)

    def precmd(self, line):
        """Format user input before executing the command, to direct them
        to already existing commands.

        Args:
            line (str): Line entered by the user.

        Attributes:
            token (list): Separate user input.
            var (str): the first char of the first word.
            result (str): patterns found by regex.

        Returns:
            str: format line to direct them commands.
        """

        token = line.split()
        if len(token) == 0 or token[0] == 'EOF':
            return line
<<<<<<< HEAD
        
=======
>>>>>>> 02191d4164b93ce29e6dbcc8db893fb385ba9153
        if re.search(r'([\w]*)\.([a-z]*)..([^"]*)', line):
            result = re.split(r'([\w]*)\.([a-z]*)..([^"]*)', line)
            if result[2] == "all" or result[2] == "count":
                return f"{result[2]} {result[1]} "
            elif result[2] == "show" or result[2] == "destroy":
                return f"{result[2]} {result[1]} {result[3]}"
        else:
            return line

    def checker(self, tokens, op_code):
        """
        Validates if the parameters required for the operation
        of the executing command were passed.

        Args:
            tokens (str): Separate user input.
            op_code (int): Operation code to know what conditions to check.
                1 => class condition
                2 => id condition
                3 => attributes condition
        Attributes:
            check (bool): Mark.

        Return:
            -True if it was successful.
            -False if unsuccessful.
        """
        check = True
        if op_code > 0:
            check = self.class_condition(tokens)
        if op_code > 1 and check:
            check = self.id_condition(tokens)
        if op_code > 2 and check:
            check = self.attr_condition(tokens)
        return check

    def class_condition(self, tokens):
        """
        Class method that will check the class conditions.

        Args:
            tokens (str): Separate user input.

        Attributes;
            length (int): length of the tokens.

        Return:
            -True if it was successful.
            -False if unsuccessful.
        """
        length = len(tokens)
        if length == 0:
            print("** class name missing **")
            return False
        elif tokens[0] not in dict_class.keys():
            print("** class doesn't exist **")
            return False
        return True

    def id_condition(self, tokens):
        """
        Class method that will check ID conditions.

        Args:
            tokens (str): Separate user input.

        Attributes;
            length (int): length of the tokens.

        Return:
            -True if it was successful.
            -False if unsuccessful.
        """
        length = len(tokens)
        if length == 1:
            print("** instance id missing **")
            return False
        elif (tokens[0] + "." + tokens[1]) not in list(storage.all().keys()):
            print("** no instance found **")
            return False
        return True

    def attr_condition(self, tokens):
        """
        Class method that will check attribute conditions.

        Args:
            tokens (str): Separate user input.

        Attributes;
            length (int): length of the tokens.

        Return:
            -True if it was successful.
            -False if unsuccessful.
        """
        length = len(tokens)
        if length == 2:
            print("** attribute name missing **")
            return False
        elif length == 3:
            print("** value missing **")
            return False
        return True

    def is_integer(self, value):
        """
        Check if a string is an integer.

        Args:
            value (int): value to check

        Return:
            -True if it was successful.
            -False if unsuccessful.
        """
        if value.isnumeric() or value[0] == '-' and value[1:].isnumeric():
            return True
        return False

    def is_float(self, value):
        """
        Check if a string is a float.

        Args:
            value (int): value to check.

        Return:
            -True if it was successful.
            -False if unsuccessful.
        """
        str_partition = value.partition(".")
        if str_partition[0].isnumeric() and str_partition[-1].isnumeric():
            return True
        return False

    def do_EOF(self, line):
        """Terminates the running program."""
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Ignore empty lines."""
        self.lastcmd = ''
        return cmd.Cmd.emptyline(self)

    def do_help(self, arg):
        """
        Help for commands.

        Usage:
            (hbnb) help // List available commands
            (hbnb) help <command> // Detailed help on the command(cmd)
        """
        return super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
