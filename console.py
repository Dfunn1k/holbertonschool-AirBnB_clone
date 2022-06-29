#!/usr/bin/python3
import cmd
"""
User this module for console

(HBNB CONSOLE)
"""


class HBNBCommand(cmd.Cmd):
    """Console for instances that inherit"""
    prompt = '(hbnb) '

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
