import datetime
import math
import time
from random import random
from awsapimock.aws_data_helpers import get_exadecimal_sample


class Elasticbeanstalk:

    def describe_single_application(self, application_name = None):

        fake_region = 'mo-north-1'
        # print("---" + application_name + "---")
        if application_name == None:
            application_name = "app-name-" + str(math.ceil(random() * 10000))
        datetimesimulated = datetime.datetime.fromtimestamp(
            time.time() - (random() * 300000000)
        )
        
        return {
            "ApplicationArn": "arn:aws:elasticbeanstalk:us-east-1:" + fake_region + ":application/" + application_name,
            "ApplicationName": application_name,
            "DateCreated": datetimesimulated,
            "DateUpdated": datetimesimulated,
            "ConfigurationTemplates": [],
            "ResourceLifecycleConfig": {
                "VersionLifecycleConfig": {
                    "MaxCountRule": {
                        "Enabled": False,
                        "MaxCount": 200,
                        "DeleteSourceFromS3": False
                    },
                    "MaxAgeRule": {
                        "Enabled": False,
                        "MaxAgeInDays": 180,
                        "DeleteSourceFromS3": False
                    }
                }
            }
        }

    def describe_applications(self):

        request_id = get_exadecimal_sample(8) + "-" + get_exadecimal_sample(4) + "-" + get_exadecimal_sample(4) + "-" + get_exadecimal_sample(4) + "-" + get_exadecimal_sample(12)

        return {
            "Applications": [
                self.describe_single_application()
            ],
            "ResponseMetadata": {
                "RequestId": request_id,
                "HTTPStatusCode": 200,
                "HTTPHeaders": {
                    "content-type": "text/xml",
                    "date": "Mon, 14 Sep 2020 23:37:52 GMT",
                    "vary": "accept-encoding",
                    "x-amzn-requestid": request_id,
                    "content-length": "12345",
                    "connection": "keep-alive"
                },
                "RetryAttempts": 0
            }
        }