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
   
    def do_create(self, arg):
        """Creating a new instance of Basemodel. """
        
        arglenth = parse(arg)
        if len(arglenth) == 0:
            print("** class name missing **")
        elif arglenth[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arglenth[0])().id)
            storage.save()
    
    def do_show(self, arg):
        """Printing the string representation of an
        instance based on the class name and id. """
        
        arglenth = parse(arg)
        objdict = storage.all()
        if len(arglenth) == 0:
            print("** class name missing **")
        elif arglenth[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arglenth) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arglenth[0], arglenth[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(arglenth[0], arglenth[1])])

    def do_destroy(self, arg):
        """Deleting an instance based 
        on the class name and id. """
        arglenth = parse(arg)
        objdict = storage.all()
        if len(arglenth) == 0:
            print("** class name missing **")
        elif arglenth[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arglenth) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arglenth[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(arglenth[0], arglenth[1])]
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
