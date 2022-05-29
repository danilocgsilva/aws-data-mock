import unittest
import sys
sys.path.insert(1, "..")
from aws_api_mock.VpcSecurityGroup_Data_Generator import VpcSecurityGroup_Data_Generator
from aws_api_mock.aws_data_helpers import get_exadecimal_sample

class test_VpcSecurityGroup_Data_Generator(unittest.TestCase):

    def setUp(self):
        self.vpc_security_group = VpcSecurityGroup_Data_Generator()

    def test_generate_return_type(self):
        returned_dict = self.vpc_security_group.generate()
        self.assertTrue(isinstance(returned_dict, dict))

    def test_set_group_id_fluent_interface(self):
        returned_after_set = self.vpc_security_group.set_group_id("sg-" + get_exadecimal_sample(11))
        self.assertTrue(isinstance(returned_after_set, VpcSecurityGroup_Data_Generator))

    def test_set_group_id(self):
        group_id_sample = "sg-abcd1234ef90"
        self.vpc_security_group.set_group_id(group_id_sample)
        vpc_security_group_data = self.vpc_security_group.generate()
        self.assertEqual(group_id_sample, vpc_security_group_data["VpcSecurityGroupId"])
