import os
import shutil
import tempfile
from unittest import TestCase

from assembler import Assembler

ASM_CONTENT = '''@2
D=A
@3
D=D+A
@0
M=D
'''

HACK_CONTENT = [
    '0000000000000010',
    '1110110000010000',
    '0000000000000011',
    '1110000010010000',
    '0000000000000000',
    '1110001100001000',
]

class AssemblerTest(TestCase):
    def setUp(self):
        self.TMP_PATH = tempfile.mkdtemp()
        self.ADD_ASM_FILE = f'{self.TMP_PATH}/Add.asm'
        self.EXPECTED_ADD_HACK_FILE = f'{self.TMP_PATH}/Add.hack'

        # write test asm and hack
        with open(self.ADD_ASM_FILE, 'w') as f:
            f.write(ASM_CONTENT)

    def tearDown(self):
        shutil.rmtree(self.TMP_PATH)

    def test_assembler_result_in_path(self):
        assembler = Assembler(asm_path=self.ADD_ASM_FILE)

        self.assertEqual(
            assembler.hack_path,
            self.EXPECTED_ADD_HACK_FILE,
        )

    def test_assembler_translate(self):
        assembler = Assembler(asm_path=self.ADD_ASM_FILE)
        assembler._translate()

        result_file = open(assembler.hack_path, 'r')
        for result, expect in zip(result_file, HACK_CONTENT):
            with self.subTest(result=result, expect=expect):
                self.assertEqual(result.strip(), expect)
