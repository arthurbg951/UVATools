from UVATool.Structure import Structure
import sys
from os.path import isfile, basename, dirname, abspath

class StructureFile:
    """
    """
    # This class define a how to load a script file (.py)
    # for now, it just load a script file with a Structure defined
    # possible improovements: verify if the file contains some var with list[Nodes] and list[Elements] and try to load it
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.__checkFile(file_name)
    
    def __checkFile(self, file_name: str):
        if not isfile(file_name):
            raise Exception('File not Exist!')

    def getStructure(self) -> Structure:
        path = abspath(dirname(self.file_name))
        sys.path.append(path)
        module_name = basename(self.file_name)[:-3]
        struct = __import__(module_name)
        for i in dir(struct):
            item = getattr(struct, i)
            if isinstance(item, Structure):
                return item
        raise Exception('This file not contains a Structure!')
