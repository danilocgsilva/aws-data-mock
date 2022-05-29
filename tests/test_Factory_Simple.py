import unittest
import sys
sys.path.insert(1, "..")
from aws_api_mock.Factory_Simple import Factory_Simple

class test_Factory_Simple(unittest.TestCase):

    def setUp(self) -> None:
        self.factory_simple = Factory_Simple()

    def test_set_possibles_fluent_interface(self):
        factory_resulted = self.factory_simple.set_possibles("one_possibility")
        self.assertTrue(isinstance(factory_resulted, Factory_Simple))

    def test_set_possibles_fluent_interface_twice(self):
        factory_resulted = self.factory_simple.set_possibles("one_possibility").set_possibles("two_possibles")
        self.assertTrue(isinstance(factory_resulted, Factory_Simple))

    def test_set_possibles_adding_two(self):
        self.factory_simple.set_possibles("first")
        self.factory_simple.set_possibles("second")
        possibles = self.factory_simple.get_possibles()
        self.assertEqual(2, len(possibles))

    def test_get_extracting(self):
        self.factory_simple.set_possibles("first").set_possibles("second")
        extracted = self.factory_simple.get_extracting()
        remaining_listing = self.factory_simple.get_possibles()
        self.assertEqual(1, len(remaining_listing))

    def test_get_extracting_exception(self):
        with self.assertRaises(Exception):
            self.factory_simple.get_extracting()
