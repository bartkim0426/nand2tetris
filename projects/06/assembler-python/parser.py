from typing import Iterator, Optional


def read_asm_file(filename: str) -> Iterator:
    with open(filename, 'r') as f:
        value = f.readline()
        yield value.rstrip()


def remove_whitespaces(text: str) -> str:
    '''remove prefix, suffix whitespaces in text'''
    return text.strip()


def is_comment(text: str) -> bool:
    '''determine the text is comment or not in Hack language'''
    return text.startswith('//')


class Parser:
    '''
    Parse Hack machine language instructions into individual fields.
    Ignore whitespaces and comments (starts with //)

    input:
        filename: (Optional) File name of instruction. If filename is served, instructions params are ignored.
        instructions: (Optional) Iterable for instructions

    property:
        instruction_generator
        fields

    usage:
    >>> parser = Parser(iterator)
    # Use _parse_yield() to yield parsed instruction
    >>> for instruction in parser._parse_yield():
            ...  # do whatever with parsed instruction
    # Or iterate parser directly
    >>> for instruction in parser:
            ...
    # Or explicitly create parsed fields list. O(n)
    >>> parsed_fields: list = parser.parsed_fields()
    '''
    # TODO; change self.fields into generator
    def __init__(self, instructions: Optional[Iterator]=None, filename: Optional[str]=None):
        if filename:
            self.instructions = read_asm_file(filename)
        else:
            self.instructions = instructions
        self.fields = []

    def __iter__(self):
        '''yield parsed instruction'''
        return self._parse_yield()

    def _parse_yield(self):
        '''yield parsed instruction iterating instructions'''
        for instruction in self.instructions:
            instruction = remove_whitespaces(instruction)
            if not is_comment(instruction):
                yield instruction

    def _parse(self):
        '''
        Set fields by iterating all instructions at once.
        - O(n) time complexity
        '''
        for instruction in self._parse_yield():
            self.fields.append(instruction)

    def parsed_fields(self) -> list:
        '''return parsed fields explicitly. O(n)'''
        self._parse()
        return self.fields
