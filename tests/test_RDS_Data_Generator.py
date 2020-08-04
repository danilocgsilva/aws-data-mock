import unittest
import sys
sys.path.insert(1, "..")
from awsapimock.RDS_Data_Generator import RDS_Data_Generator


class test_RDS_Data_Generator(unittest.TestCase):

    def setUp(self):
        self.rds_data_generator = RDS_Data_Generator()

    def test_generate_return_type(self):
        return_dict = self.rds_data_generator.generate()
        self.assertTrue(isinstance(return_dict, dict))
