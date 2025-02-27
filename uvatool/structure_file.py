import sys
from os.path import isfile, basename, dirname, abspath

from .node import Node
from .element import Element
from .structure import Structure
from .colors import to_blue, to_green, to_red


class StructureFile:
    """ """

    # This class define a how to load a script file (.py)
    # for now, it just load a script file with a Structure defined
    # possible improovements: verify if the file contains some var with list[Nodes] and list[Elements] and try to load it

    def __init__(self, file_name: str, verbose: bool = False) -> None:
        self.file_name = file_name
        self.__checkFile(file_name)
        self.verbose = verbose
        self.__structure: list[Structure] = []
        self.__findStructure()

    def __checkFile(self, file_name: str):
        if not isfile(file_name):
            raise Exception("File not Exist!")

    def __writeOutput(self, msg: str) -> None:
        if self.verbose:
            print(msg)

    def __addStructure(self, item: Structure) -> None:
        if not self.__structure.__contains__(item):
            self.__structure.append(item)

    def __findStructure(self) -> list[Structure]:
        path = abspath(dirname(self.file_name))
        module_name = basename(self.file_name)[:-3]
        sys.path.append(path)
        struct = __import__(module_name)

        self.__writeOutput(f"path={path}")
        self.__writeOutput(f"module_name={module_name}")
        self.__writeOutput(f"StructureFile={struct}")

        from types import FunctionType

        for i in dir(struct):
            item = getattr(struct, i)

            # PRINT ALL ITEM VALUE AND TYPE
            if sys.gettrace() is not None:
                self.__writeOutput(to_blue(f"item={item}, type={type(item)}"))

            # CHECK IF IS NODE OR ELEMENT
            if isinstance(item, Node) or isinstance(item, Element):
                self.__writeOutput(f"item={item}, type={type(item)}")

            # CHECK IF IS A FUNCTION
            if isinstance(item, FunctionType):
                try:
                    self.__writeOutput(f"item()={item()}, type={type(item())}")
                except Exception:
                    import traceback

                    print(to_red(traceback.format_exc()))
                # CHECK IF IS A FUNCTION WITH A STRUCTURE
                try:
                    if isinstance(item(), Structure):
                        self.__addStructure(item())
                except Exception:
                    import traceback

                    print(to_red(traceback.format_exc()))

            # CHECK IF IS A STANDALONE STRUCTURE
            if isinstance(item, Structure):
                self.__addStructure(item)

        self.__writeOutput(
            to_green(f"Founded {len(self.__structure)} structures in this File.")
        )

        if len(self.__structure) == 0:
            raise Exception("This file not contains a Structure!")

    def getStructure(self) -> list[Structure]:
        return self.__structure
