import os
import sys
import getopt

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


def main(argv):
    inputfile = ''
    try:
      opts, _ = getopt.getopt(argv,"hi",["ifile="])
    except getopt.GetoptError:
        print('python assembler.py -i <asm_file_path>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ['-h', '--help']:
            print('python assembler.py -i <asm_file_path>')
            sys.exit()
        elif opt in ('-i', '--input'):
            print(f'input path: {arg}')
            inputfile = arg

    assembler = Assembler(inputfile)
    assembler._translate()
    
    print(f'Translate completed with output file: {assembler.hack_path}')


if __name__ == '__main__':
    main(sys.argv[1:])
