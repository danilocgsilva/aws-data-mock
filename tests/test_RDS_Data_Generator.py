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

    def test_generate_securities_groups_count_default(self):
        return_dict = self.rds_data_generator.generate()
        securities_groups = return_dict["DBInstances"][0]["VpcSecurityGroups"]
        self.assertEqual(1, len(securities_groups))

    def test_generate_instances_count_default(self):
        return_dict = self.rds_data_generator.generate()
        self.assertEqual(1, len(return_dict["DBInstances"]))

    def test_set_security_group_id(self):
        security_group_id_forced = "sg-123412abcd123"
        self.rds_data_generator.set_security_group_id(security_group_id_forced)
        returned_instances = self.rds_data_generator.generate()
        returned_security_group_id = returned_instances["DBInstances"][0]["VpcSecurityGroups"][0]["VpcSecurityGroupId"]
        self.assertEqual(security_group_id_forced, returned_security_group_id)
        
