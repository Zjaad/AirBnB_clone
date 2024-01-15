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
        arglenth = arg.split()
        larg = len(arglenth)
        if larg == 0:
            print("** class name missing **")
        elif arglenth[0] not in cls:
            print("** class doesn't exist **")
        else:
            print(eval(arglenth[0])().id)
            storage.save()
    
    def all(self, arg):
        """ It prints all str of insts."""
        storedObjs = storage.all()
        argSp = arg.split()
        sov = storedObjs.values()
        if not argSp:
            for objc in sov:
                print(objc)
            return
        className = argSp[0]
        if className not in cls:
            print("** class doesn't exist **")
            return
        instns = [x for x in sov if x.__class__.__name__ == className]
        if not instns:
            print("** no instance found **")
        else:
            for x in instns:
                print(x)

    def update(self, arg):
        """ update. """
        argList = arg.split()
        larl = len(argList)
        if larl == 0:
            print("** class name missing **")
            return
        className = argList[0]
        if className not in cls:
            print("** class doesn't exist **")
            return
        if larl == 1:
            print("** instance id missing **")
            return
        insId = argList[1]
        p = "{}.{}".format(className, instId)
        storedObjs = storage.all()

        if p not in storedObjs:
            print("** no instance found **")
            return
        if larl == 2:
            print("** attribute name missing **")
            return
        atName = argList[2]

        if larl == 3:
            print("** value missing **")
            return
        atVal = argList[3]
        ins = storedObjs[p]

        if not hasattr(ins, atName):
             print("** attribute doesn't exist for this instance **")
             return

        if atName in ["id", "created_at", "updated_at"]:
             print("** can't update {} **".format(atName))
             return
        atType = type(getattr(ins, atName))
        try:
            cv = atType(atVal)
        except ValueError:
            print("** invalid value type for attribute {} **".format(attrName))
            return
        setattr(ins, atName, cv)
        ins.save()


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
        if len(argSp)< 2:
            print("** instance id missing **")
            return

        insId = argSp[1]
        x = f"{className}.{insId}"
        objcDi = storage.all()
        objcSv = storage.save()

        if x not in objcDi:
            print("** no instance found **")
            return

        del objcDi[x]
        return(objcSv)


setattr(HBNBCommand, 'do_all', HBNBCommand.all)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
