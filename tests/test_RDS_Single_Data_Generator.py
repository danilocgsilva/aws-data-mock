import unittest
import sys
sys.path.insert(1, "..")
from aws_api_mock.RDS_Single_Data_Generator import RDS_Single_Data_Generator

class test_RDS_Single_Data_Generator(unittest.TestCase):

    def setUp(self) -> None:
        self.rds_single_data_generator = RDS_Single_Data_Generator()

    def test_generate_type(self):
        returned_result = self.rds_single_data_generator.generate()
        self.assertTrue(isinstance(returned_result, dict))

    def test_set_security_group_id(self):
        security_group_id = "sg-abc1234"
        self.rds_single_data_generator.set_security_group_id(security_group_id)
        returned_result = self.rds_single_data_generator.generate()
        sg_returned = returned_result["VpcSecurityGroups"][0]["VpcSecurityGroupId"]
        self.assertEqual(security_group_id, sg_returned)

    def test_generate_security_group_count_default(self):
        returned_result = self.rds_single_data_generator.generate()
        sg_count = len(returned_result["VpcSecurityGroups"])
        self.assertEqual(1, sg_count)
