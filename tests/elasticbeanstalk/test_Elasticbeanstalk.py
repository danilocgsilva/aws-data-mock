import unittest
import sys
sys.path.insert(1, "..")
from awsapimock.elasticbeanstalk.Elasticbeanstalk import Elasticbeanstalk


class test_Elasticbeanstalk(unittest.TestCase):

    def setUp(self):
        self.elasticbeanstalk_datamocker = Elasticbeanstalk()

    def test_response_with_name(self):
        app_name = "my-app-name-mocker"
        elasticbeanstalk_single_data_instance = self.elasticbeanstalk_datamocker\
            .describe_single_application(app_name)
        self.assertEqual(app_name, elasticbeanstalk_single_data_instance["ApplicationName"])
    