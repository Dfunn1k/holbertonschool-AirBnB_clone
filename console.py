#!/usr/bin/python3
import cmd
from models import storage
from models import dict_class
"""
User this module for console

(HBNB CONSOLE)
"""


class HBNBCommand(cmd.Cmd):
    """Console for instances that inherit"""
    prompt = '(hbnb) '

    def class_condition(self, tokens):
        """Clase que verificará las condiciones de clase"""
        length = len(tokens)
        if length == 0:
            print("** class name missing **")
            return False
        elif tokens[0] not in dict_class.keys():
            print("** class doesn't exist **")
            return False

    def id_condition(self, tokens):
        """Clase que verificará las condiciones de ID"""
        length = len(tokens)
        if length == 1:
            print("** instance id missing **")
            return False
        elif (tokens[0] + "." + tokens[1]) not in list(storage.all().keys()):
            print("** no instance found **")
            return False

    def checker(self, tokens, op_code):
            """
            op_code 
                1 : verifica las condiciones de clase
                2 : verifica las condiciones de clase e id
                3 : 
            """
            length = len(tokens)
            check = True
            if op_code > 0:
                check = self.class_condition(tokens)
            if op_code > 1 and check:
                check = self.id_condition(tokens)

            return check

    def do_create(self, line):
        """"""
        tokens = line.split()
        if self.checker(tokens, 1):
            obj = dict_class[tokens[0]]()
            storage.save()
            print(obj.id)

    def do_show(self, line):
        """"""
        tokens = line.split()
        if self.check_conditions(tokens, 2):
            print(storage.all()[tokens[0] + "." + tokens[1]])
 
    def do_destroy(self, line):
        """"""
        tokens = line.split()
        if self.check_conditions(tokens, 2):
            del storage.all()[tokens[0] + "." + tokens[1]]
            storage.save()

    def do_EOF(self, line):
        """Terminates the running program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Ignore empty lines"""
        self.lastcmd = ''
        return cmd.Cmd.emptyline(self)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
