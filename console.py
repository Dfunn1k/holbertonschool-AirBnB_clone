#!/usr/bin/python3
import cmd
"""
User this module for console

(HBNB CONSOLE)
"""


class HBNBCommand(cmd.Cmd):
    """Console for instances that inherit"""
    prompt = '(hbnb) '

    def create(self):
        """"""
        # first finish tasks 3-5

    def do_EOF(self, line):
        """Terminates the running program\n"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Ignore empty lines\n"""
        self.lastcmd = ''
        return cmd.Cmd.emptyline(self)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
