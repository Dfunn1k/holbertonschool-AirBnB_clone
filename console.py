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

    def help_EOF(self):
        return

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def emptyline(self):
        """Ignore empty lines"""
        return cmd.Cmd.emptyline(self)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
