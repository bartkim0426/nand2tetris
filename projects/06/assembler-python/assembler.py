import os

from parser import Parser
from translator import Translator


class Assembler:
    '''main class'''
    def __init__(self, asm_filename: str, path: str=None):
        '''
        params:
            filename: relative path for asm file name
            path: relative path for target directory to save hack file
        '''
        self.path = path
        if not path:
            self.path = os.getcwd()

        self.asm_filename = asm_filename

    def _parse(self):
        '''read and parse asm file'''
        return Parser(self.asm_filename)

    


