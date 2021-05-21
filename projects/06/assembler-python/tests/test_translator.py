from unittest import TestCase

from translator import translate_a_instruction, translate_c_instruction, translate,\
        translate_dest, translate_jump, translate_comp, DESTINATION_PARIS, JUMP_PARIS, COMP_PAIRS, \
        divide_c_instruction


class TranslatorTest(TestCase):
    def test_translate_a_instruction(self):
        '''test simple traslate function from machine code to binary value'''
        machine_code = '@2'
        binary_value = '0000000000000010'

        self.assertEqual(translate_a_instruction(machine_code), binary_value)
        self.assertEqual(translate(machine_code), binary_value)

    def test_translate_dest(self):
        '''test translate destination code from c-instruction into 3 bits binary value'''
        for machine_code, binary_value in DESTINATION_PARIS.items():
            with self.subTest(machine_code=machine_code, binary_value=binary_value):
                self.assertEqual(translate_dest(machine_code), binary_value)

    def test_translate_jump(self):
        '''test translate jump code into 3 bits binary value'''
        for machine_code, binary_value in JUMP_PARIS.items():
            with self.subTest(machine_code=machine_code, binary_value=binary_value):
                self.assertEqual(translate_jump(machine_code), binary_value)

    def test_translate_comp(self):
        '''test translate comp code into 7 bits binary value'''
        for machine_code, binary_value in COMP_PAIRS.items():
            with self.subTest(machine_code=machine_code, binary_value=binary_value):
                self.assertEqual(translate_comp(machine_code), binary_value)

    def test_divide_c_instruction(self):
        machine_code = 'MD=D+1'
        c_ins = divide_c_instruction(machine_code)

        self.assertEqual(c_ins.dest, 'MD')
        self.assertEqual(c_ins.comp, 'D+1')
        self.assertEqual(c_ins.jump, '')

    def test_translate_c_instruction(self):
        '''test translate function for c instruction'''
        machine_code = 'MD=D+1'
        dest = '011'
        comp = '0011111'
        jump = '000'
        binary_value = f'111{comp}{dest}{jump}'

        self.assertEqual(translate_c_instruction(machine_code), binary_value)
        self.assertEqual(translate(machine_code), binary_value)
