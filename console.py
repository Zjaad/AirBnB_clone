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

   
    def create(self, arg):
        """Creating a new instance of Basemodel. """
        
        arglenth = parse(arg)
        if len(arglenth) == 0:
            print("** class name missing **")
        elif arglenth[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arglenth[0])().id)
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
