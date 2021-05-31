import os
import sys
import argparse

from asm_parser import Parser
from translator import translate


class Assembler:
    '''
    main class for assmbler: translate hack machine language into binary code

    input asm file should be 'xxx.asm'
    output binary file will be 'xxx.hack' in same directory

    usage
    >>> assembler = Assembler(asm_path)
    >>> assembler._translate()
    '''
    def __init__(self, asm_path: str):
        '''
        params:
            asm_path: absolute path for asm file
        '''
        asm_path = os.path.abspath(asm_path)

        dir_name = os.path.dirname(asm_path)
        filename_without_ext = os.path.basename(asm_path).split('.')[0]

        self.asm_path = asm_path
        self.hack_path = f'{dir_name}/{filename_without_ext}.hack'

    def _parse(self):
        '''read and parse asm file'''
        return Parser(filename=self.asm_path)

    def _translate(self):
        '''translate from parsed asm into binary code'''
        with open(self.hack_path, 'w') as f:
            for field in self._parse():
                f.write(f'{translate(field)}\n')


def main(args):
    inputfile = args.input
    assembler = Assembler(inputfile)
    assembler._translate()
    print(f'Translate completed with output file: {assembler.hack_path}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Assembler for Hack language')
    parser.add_argument('-i', '--input', type=str, help='path for asm file.')
    args =parser.parse_args(sys.argv[1:])
    main(args)
