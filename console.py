#!/usr/bin/python3
""" The console. """
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def emptyline(self):
        """ Empty input. """
        pass

    def do_quit(self, arg):
        """ Quit the console. """
        return (True)
    
    def do_EOF(self, arg):
        """ also Quit the console. """
        return (True)
    

    # def do_help(self, arg):
    #    """ Help. """
     #   cmd.Cmd.do_help(self,arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
