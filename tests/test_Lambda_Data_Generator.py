import unittest
import sys
sys.path.insert(1, "..")
from awsapimock.Lambda_Data_Generator import Lambda_Data_Generator


class test_Lambda_Data_Generator(unittest.TestCase):

    def setUp(self):
        self.lambda_data_generator = Lambda_Data_Generator()

    def test_generate_return_type(self):
        returned_data = self.lambda_data_generator.generate()
        self.assertTrue(isinstance(returned_data, dict))

