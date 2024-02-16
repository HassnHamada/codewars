import unittest
from ..src.simple_pig_latin import pig_it


class TestPigLatin(unittest.TestCase):

    def test_simple_word(self):
        self.assertEqual(pig_it('hello'), 'ellohay')

    def test_sentence(self):
        self.assertEqual(pig_it('hello world'), 'ellohay orldway')

    def test_punctuation(self):
        self.assertEqual(pig_it('hello!'), 'hello!')

    def test_punctuation_space(self):
        self.assertEqual(pig_it('hello !'), 'ellohay !')

    def test_mixed_case(self):
        self.assertEqual(pig_it('HeLLo'), 'eLLoHay')

    def test_numbers(self):
        self.assertEqual(pig_it('123 hello'), '123 ellohay')


if __name__ == '__main__':
    unittest.main()
