import os
import shutil
import tempfile
from unittest import TestCase

from assembler import Assembler

ADD_ASM_FILENAME = os.path.join(os.path.dirname(__file__), 'Add.asm')
EXPECTED_ADD_HACK_FILENAME = os.path.join(os.path.dirname(__file__), 'Add.hack')



class AssemblerTest(TestCase):
    # def test_false(self):
        # self.assertTrue(False)

    def setUp(self):
        self.TMP_PATH = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.TMP_PATH)

    def test_assembler_result_in_path(self):
        assembler = Assembler(asm_filename=ADD_ASM_FILENAME, path=self.TMP_PATH)

        self.assertEqual(
            assembler.result_filename,
            self.TMP_PATH + '/Add.hack'
        )

    def test_assembler_result(self):
        pass
        expected_file = open(EXPECTED_ADD_HACK_FILENAME, 'r')
        result_file = open(assembler.result_filename, 'r')

