import unittest
import sys
sys.path.insert(1, "..")
from aws_api_mock.Instance_Single_Generator import Instance_Single_Generator

class test_Instance_Single_Generator(unittest.TestCase):

    def setUp(self):
        self.instance_sinfgle_generator = Instance_Single_Generator()

    def test_setInstanceId(self):
        instance_hexa = "ab5471afda4120a1c"
        self.instance_sinfgle_generator.setInstanceId(instance_hexa)
        instance_data_generated = self.instance_sinfgle_generator.generate()
        self.assertEqual("i-" + instance_hexa, instance_data_generated["InstanceId"])

