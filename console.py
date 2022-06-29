#!/usr/bin/python3
import cmd
"""
User this module for console

(HBNB CONSOLE)
"""


class HBNBCommand(cmd.Cmd):
    """Console for instances that inherit"""
<<<<<<< HEAD
    prompt = '(hbnb)'

    def create(self):
        """"""
        # first finish tasks 3-5
=======
    prompt = '(hbnb) '
>>>>>>> f1994926428d136bdf29e5bc9a95e5b34a149068

    def do_EOF(self, line):
        """Terminates the running program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Ignore empty lines"""
        return cmd.Cmd.emptyline(self)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
