import os
from typing import Generator
from unittest import TestCase

from parser import Parser, remove_whitespaces, is_comment, read_asm_file


ADD_ASM_FILENAME = os.path.join(os.path.dirname(__file__), 'Add.asm')

class ReaderTest(TestCase):
    def test_reader(self):
        '''test read Add.asm file and yield line by line'''
        reader = read_asm_file(ADD_ASM_FILENAME)

        expected_file = open(ADD_ASM_FILENAME, 'r')
        for result, expect in zip(reader, expected_file):
            with self.subTest(result=result, expect=expect):
                self.assertEqual(result, expect.replace('\n', ''))
        expected_file.close()

class ParserTest(TestCase):
    def test_parse(self):
        '''test parse function'''
        result = remove_whitespaces('@2')
        self.assertEqual(result, '@2')

    def test_parse_remove_whitespace(self):
        result = remove_whitespaces('  with_whitespace  ')
        self.assertEqual(result, 'with_whitespace')

    def test_is_comment(self):
        self.assertTrue(is_comment('// comment'))
        self.assertFalse(is_comment('comment'))

    def test_parse_yield(self):
        '''test parse_yield that yield instruction'''
        instruction_generator = (
            ins for ins in ['@2', 'D=A']
        )
        parser = Parser(instruction_generator)
        parsed: Generator = parser._parse_yield()

        self.assertEqual(next(parsed), '@2')
        self.assertEqual(next(parsed), 'D=A')

    def test_parse_yield_ignore_comments(self):
        '''parse_yield가 //로 시작하는 주석 무시하는지'''
        instruction_generator = (
            ins for ins in ['// this comment should be ignored', 'D=A']
        )
        parser = Parser(instruction_generator)
        parsed: Generator = parser._parse_yield()

        self.assertEqual(next(parsed), 'D=A')
        with self.assertRaises(StopIteration):
            next(parsed)

    def test_parse_yield_remove_whitespace(self):
        '''parse_yield가 instruction의 띄어쓰기 제거하는지'''
        instruction_generator = (
            ins for ins in ['  prefix_whitespace', 'suffix_whitespace  ', ' both ']
        )
        parser = Parser(instruction_generator)
        parsed: Generator = parser._parse_yield()

        self.assertEqual(next(parsed), 'prefix_whitespace')
        self.assertEqual(next(parsed), 'suffix_whitespace')
        self.assertEqual(next(parsed), 'both')

    def test_parse(self):
        '''parser의 _parse 메소드가 fields 추가해주는지'''
        instructions = ['@2', 'D=A', '@3', 'D=D+A', '@0', 'M=D',]
        instruction_generator = (
            ins for ins in instructions
        )
        parser = Parser(instruction_generator)
        parser._parse()

        self.assertEqual(len(parser.fields), len(instructions))

    def test_parser_iter_magic_method(self):
        '''parser의 __iter__ 매직메소드 작동하는지'''
        instructions = ['@2', 'D=A', '@3', 'D=D+A', '@0', 'M=D',]
        instruction_generator = (
            ins for ins in instructions
        )
        parser = Parser(instruction_generator)

        for result, expected in zip(parser, instructions):
            with self.subTest(result=result, expected=expected):
                self.assertEqual(result, expected)

    def test_parser_with_filename(self):
        '''parser with filename instead of iterator'''
        instructions = ['@2', 'D=A', '@3', 'D=D+A', '@0', 'M=D',]
        parser = Parser(filename=ADD_ASM_FILENAME)

        for result, expected in zip(parser, instructions):
            with self.subTest(result=result, expected=expected):
                self.assertEqual(result, expected)
