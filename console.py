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
    
    def show(self, arg):
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

    def destroy(self, arg):
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
        elif "{}.{}".format(arglenth[0], arglenth[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(arglenth[0], arglenth[1])]
            storage.save()

    def all(self, arg):
        """Printing all string representation of all instances
        based or not on the on the class name ."""
        arglenth = parse(arg)
        if len(arglenth) > 0 and arglenth[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            Cstring = []
            for obj in storage.all().values():
                if len(arglenth) > 0 and arglenth[0] == obj.__class__.__name__:
                    Cstring.append(obj.__str__())
                elif len(arglenth) == 0:
                    Cstring.append(obj.__str__())
            print(Cstring)

    def update(self, arg):
        """."""
        arglenth = parse(arg)
        objdict = storage.all()

        if len(arglenth) == 0:
            print("** class name missing **")
            return False
        if arglenth[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arglenth) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arglenth[0], arglenth[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(arglenth) == 2:
            print("** attribute name missing **")
            return False
        if len(arglenth) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arglenth) == 4:
            obj = objdict["{}.{}".format(arglenth[0], arglenth[1])]
            if arglenth[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arglenth[2]])
                obj.__dict__[arglenth[2]] = valtype(arglenth[3])
            else:
                obj.__dict__[arglenth[2]] = arglenth[3]
        elif type(eval(arglenth[2])) == dict:
            obj = objdict["{}.{}".format(arglenth[0], arglenth[1])]
            for k, v in eval(arglenth[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
