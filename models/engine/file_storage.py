#!/usr/bin/python3
""" The FileStorage class. """
import json



class FileStorage:
    """ FileStorage that serializes instances to
    a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ it returns the dict __objects. """
        return(self.__objects)

    def new(self, obj):
        """ it sets the obj in __objects
        with key the obj. """
        className = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[className] = obj

    def save(self):
        """ It serializes __objects to JSON file. """
        srl = {i: y.to_dict() for i, y in self.__objects.items()}
        try:
            with open(self.__file_path, 'w', encoding="utf-8") as file:
                json.dump(srl, file)
        except Exception:
                pass

    def reload(self):
        """ It deserializes the JSON file to __objects
        only if the JSON file (__file_path) exists. """
        try :
            with open(self.__file_path, 'r') as file:
                objc = json.load(file)
                for k, i in objc.items():
                    className , id = k.split('.')
                    cl = eval(className)
                    objInst = cl(**i)
                    self.__objects[k] = objInst
        except Exception:
            pass
