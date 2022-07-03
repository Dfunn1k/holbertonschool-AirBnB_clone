#!/usr/bin/python3
<<<<<<< HEAD
import cmd
import re
from models import storage
from models import dict_class
=======
>>>>>>> f5f7ca36ee53b60d9841ae356200b7ea657ed5d7
"""
User this module for console

(HBNB CONSOLE)
"""
import cmd
from models import storage
from models import dict_class


class HBNBCommand(cmd.Cmd):
    """Console for instances that inherit"""
    prompt = '(hbnb) '

    def class_condition(self, tokens):
        """Metodo de Clase que verificará las condiciones de clase"""
        length = len(tokens)
        if length == 0:
            print("** class name missing **")
            return False
        elif tokens[0] not in dict_class.keys():
            print("** class doesn't exist **")
            return False
        return True

    def id_condition(self, tokens):
        """Metodo de Clase que verificará las condiciones de ID"""
        length = len(tokens)
        if length == 1:
            print("** instance id missing **")
            return False
        elif (tokens[0] + "." + tokens[1]) not in list(storage.all().keys()):
            print("** no instance found **")
            return False
        return True

    def attr_condition(self, tokens):
        """Metodo de Clase que verificará las condiciones de atributo"""
        length = len(tokens)
        if length == 2:
            print("** attribute name missing **")
            return False
        elif length == 3:
            print("** value missing **")
            return False
        return True

    def is_integer(self, value):
        """Check if a string is an integer"""
        if value.isnumeric() or value[0] == '-' and value[1:].isnumeric():
            return True
        return False

    def is_float(self, value):
        """Check if a string is a float"""
        str_partition = value.partition(".")
        if str_partition[0].isnumeric() and str_partition[-1].isnumeric():
            return True
        return False

    def checker(self, tokens, op_code):
        """
        Check the conditions of our cmd engine
        op_code:
        1 : verifica las condiciones de clase
        2 : verifica las condiciones de clase e id
        3 : verifica las condiciones de clase, id y atributo
        """
        check = True
        if op_code > 0:
            check = self.class_condition(tokens)
        if op_code > 1 and check:
            check = self.id_condition(tokens)
        if op_code > 2 and check:
            check = self.attr_condition(tokens)

        return check

    def do_create(self, line):
        """Creates a new instance of a model"""
        tokens = line.split()
        if self.checker(tokens, 1):
            obj = dict_class[tokens[0]]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        tokens = line.split()
        if self.checker(tokens, 2):
            print(storage.all()[tokens[0] + "." + tokens[1]])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        tokens = line.split()
        if self.checker(tokens, 2):
            del storage.all()[tokens[0] + "." + tokens[1]]
            storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
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
        Updates an instance based on the class name and id
        by adding or updating attribute
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

    def precmd(self, line):
        """La función hace lo que deberia pero se puede refactorizar
        Usamos regex para partir el texto como "User.all()" y retornar "all User" que si
        puede ser interpretado por la consola.
        PRECMD puede hacer algo con la linea ingresada antes de que se interprete la linea de comandos
        más información: https://docs.python.org/3.8/library/cmd.html#cmd.Cmd.precmd:~:text=una%20lista%20vac%C3%ADa.-,Cmd.precmd(%20l%C3%ADnea%20),-%C2%B6
        Solo he probado su funcionamiento con "all" "count"
        """
        token = line.split()
        var = token[0][0]
        result = re.split('([A-Z][a-z]*)\.([a-z]*)..([^"]*)',line)
        if 64 < ord(var) < 91:
            if result[2] == "all" or result[2] == "count":
                return f"{result[2]} {result[1]} "
            elif result[2] == "show" or result[2] == "destroy":
                return f"{result[2]} {result[1]} {result[3]}"
        else:
            return line

    def do_count(self, line):
        """"""
        tokens = line.split()
        if (len(tokens) != 1):
            print("FAltan argumentos")
        else:
            count = 0
            cls_name = tokens[0]
            for value in storage.all().values():
                if value.__class__.__name__ == cls_name:
                    count += 1
            print(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
