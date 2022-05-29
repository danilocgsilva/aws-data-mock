import unittest
import sys
sys.path.insert(1, "..")
from aws_api_mock.Instance_Request_Generator import Instance_Request_Generator

class test_Instance_Request_Generator(unittest.TestCase):
    def setUp(self):
        self.instanceRequestGenerator = Instance_Request_Generator()

    def test_generate_no_params_count(self):
        request_returned = self.instanceRequestGenerator.generate()
        instances_count = len(request_returned["Reservations"][0]["Instances"])
        self.assertEqual(1, instances_count)

    def test_generate_no_params_count_3(self):
        request_returned = self.instanceRequestGenerator.generate(3)
        instances_count = len(request_returned["Reservations"][0]["Instances"])
        self.assertEqual(3, instances_count)
