import unittest

from Day_three_breakfast import*


import unittest


class TestStringToArray(unittest.TestCase):

    def test_normal_sentence(self):
        input_text = "I love programming"
        expected = ["I", "love", "programming"]
        actual = convert_string_to_array(input_text)
        self.assertEqual(actual, expected)

    def test_single_word(self):
        input_text = "Hello"
        expected = ["Hello"]
        actual = convert_string_to_array(input_text)
        self.assertEqual(actual, expected)

    def test_empty_string(self):
        input_text = ""
        expected = []
        actual = convert_string_to_array(input_text)
        self.assertEqual(actual, expected)

    def test_extra_spaces(self):
        input_text = "   Python   is   fun   "
        expected = ["Python", "is", "fun"]
        actual = convert_string_to_array(input_text)
        self.assertEqual(actual, expected)

    def test_numbers_and_symbols(self):
        input_text = "semicolon @ 26"
        expected = ["semicolon", "@", "26"]
        actual = convert_string_to_array(input_text)
        self.assertEqual(actual, expected)
