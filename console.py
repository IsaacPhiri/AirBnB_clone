#!/usr/bin/python3
""" Cmd module """

import cmd


class Console(cmd.Cmd):
    """Airbnb command processor"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """quit()"""
        return True

    def do_EOF(self, line):
        """Ctrl+D \ ^D"""
        return True

if __name__ == '__main__':
    Console().cmdloop()
