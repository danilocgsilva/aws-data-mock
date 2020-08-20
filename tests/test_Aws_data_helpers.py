import unittest
import sys
sys.path.insert(1, "..")
from awsapimock.aws_data_helpers import \
    generate_owner_code, get_exadecimal_sample, generate_random_string_with_hard_chars, random_until_n


class test_Aws_data_helpers(unittest.TestCase):

    def test_generate_owner_code_string_count(self):
        user_code_sample = generate_owner_code()
        self.assertEqual(12, len(user_code_sample))

    def test_generate_owner_code_return_type(self):
        user_code_sample = generate_owner_code()
        self.assertTrue(isinstance(user_code_sample, str))

    def test_get_exadecimal_sample_return_type(self):
        exadecimal_sample = get_exadecimal_sample(12)
        self.assertTrue(isinstance(exadecimal_sample, str))

    def test_get_exadecimal_sample_string_length_1(self):
        string_length = 12
        exadecimal_sample = get_exadecimal_sample(string_length)
        self.assertEqual(string_length, len(exadecimal_sample))

    def test_get_exadecimal_sample_string_length_2(self):
        string_length = 8
        exadecimal_sample = get_exadecimal_sample(string_length)
        self.assertEqual(string_length, len(exadecimal_sample))

    def test_generate_random_string_with_hard_chars_str_len(self):
        string_length = 44
        exadecimal_sample = generate_random_string_with_hard_chars(string_length)
        self.assertEqual(string_length, len(exadecimal_sample))

    def test_random_until_n_return_type(self):
        returned_randomly = random_until_n(100)
        self.assertTrue(isinstance(returned_randomly, int))
