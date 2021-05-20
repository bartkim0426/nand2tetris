import re
from typing import NamedTuple
from collections import namedtuple

DESTINATION_PARIS: dict = {
    '': '000',
    'M': '001',
    'D': '010',
    'MD': '011',
    'A': '100',
    'AM': '101',
    'AD': '110',
    'AMD': '111',
}

JUMP_PARIS: dict = {
    '': '000',
    'JGT': '001',
    'JEQ': '010',
    'JGE': '011',
    'JLT': '100',
    'JNE': '101',
    'JLE': '110',
    'JMP': '111',
}

COMP_PAIRS: dict = {
    '0':   '0101010',
    '1':   '0111111',
    '-1':  '0111010',
    'D':   '0001100',
    'A':   '0110000',
    '!D':  '0001101',
    '!A':  '0110001',
    '-D':  '0001111',
    '-A':  '0110011',
    'D+1': '0011111',
    'A+1': '0110111',
    'D-1': '0001110',
    'A-1': '0110010',
    'D+A': '0000010',
    'D-A': '0010011',
    'A-D': '0000111',
    'D&A': '0000000',
    'D|A': '0010101',
    'M':   '1110000',
    '!M':  '1110001',
    '-M':  '1110011',
    'M+1': '1110111',
    'M-1': '1110010',
    'D+M': '1000010',
    'D-M': '1010011',
    'M-D': '1000111',
    'D&M': '1000000',
    'D|M': '1010101',
}

CInstruction = namedtuple('CInstruction', ['dest', 'comp', 'jump'])

def translate_a_instruction(machine_code: str) -> str:
    '''translate A-instruction into 16 bits binary value'''
    value = int(machine_code[1:])
    binary_value = bin(value)[2:]
    # make binary_value to 15 bit length
    rest_value = '0' * (15 - len(binary_value))
    return f'0{rest_value}{binary_value}'


def translate_dest(machine_code: str) -> str:
    '''translate destination code into 3 bits binary value'''
    return DESTINATION_PARIS[machine_code]


def translate_jump(machine_code: str) -> str:
    '''translate jump code into 3 bits binary value'''
    return JUMP_PARIS[machine_code]

def translate_comp(machine_code: str) -> str:
    '''translate comp code into 7 bits binary value'''
    return COMP_PAIRS[machine_code]

def divide_c_instruction(machine_code: str) -> NamedTuple:
    '''divide C-instruction into dest, comp, jump namedtuple'''
    c_pattern = '([^=]*)=?([^;]+);?([JGT|JGE|JGE|JLT|JNE|JLE|JMP]?)'
    match = re.match(c_pattern, machine_code)
    if not match:
        raise ValueError()
    dest, comp, jump = match.groups()
    return CInstruction(dest, comp, jump)

def translate_c_instruction(machine_code: str) -> str:
    '''
    translate C-intruction into 16-bits binary value
    dest = comp ; jump
    '''
    c_ins: NamedTuple = divide_c_instruction(machine_code)
    
    binary_dest = translate_dest(c_ins.dest)
    binary_comp = translate_comp(c_ins.comp)
    binary_jump = translate_jump(c_ins.jump)
    return f'111{binary_comp}{binary_dest}{binary_jump}'

def translate(machine_code: str) -> str:
    '''
    translate machine_code into binary value

    pseudocode

    '''
    # without symbol

    # A-instruction: 0 + binary_value
    if machine_code.startswith('@'):
        return translate_a_instruction(machine_code)
    return translate_c_instruction(machine_code)
