#!/usr/bin/python3
""" The console. """
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State

cls = {
    'BaseModel': BaseModel,
    'User': User,
    'City': City,
    'Place': Place,
    'Amenity': Amenity,
    'State': State}

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def emptyline(self):
        """ Empty input. """
        pass
    def do_quit(self, arg):
        """ Quit the console. """
        return(True) 
    def do_EOF(self, arg):
        """ also Quit the console. """
        return(True)
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
        """ show """
        argList = arg.split()
        if not argList:
            print("** class name missing **")
            return

        className = argList[0]
        
        if className not in cls:
            print("** class doesn't exist **")
            return
        insId = argList[1] if len(argList) > 1 else None
        
        i = "{}.{}".format(className, insId) if insId else None
        
        storedObjs = storage.all()

        if i and i in storedObjs:
            print(storedObjs[i])
        else:
            print("** instance id missing **" if not insId else "** no instance found **")

    def destroy(self, arg):
        ArgSp = arg.split()
        if not argSp:
            print("** class name missing **")
            return
        
        className = argSp[0]

        if className not in cls:
            print("** class doesn't exist **")
            return
        if len(argsp)< 2:
            print("** instance id missing **")
            return

        insId = argspl[1]
        x = f"{className}.{insId}"
        objcDi = storage.all()
        objcSv = storage.save()

        if x not in objcDi:
            print("** no instance found **")
            return

        del objcDi[x]
        return(objcSv)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
