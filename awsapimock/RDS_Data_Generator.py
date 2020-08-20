from awsapimock.Entity_Generator_Command_Interface import Entity_Generator_Command_Interface
from awsapimock.RDS_Single_Data_Generator import RDS_Single_Data_Generator


class RDS_Data_Generator(Entity_Generator_Command_Interface):

    def __init__(self):
        self.security_group_id = None

    def set_security_group_id(self, security_group_id: str):
        self.security_group_id = security_group_id

    def generate(self):

        rds_single_generator = RDS_Single_Data_Generator()

        if self.security_group_id:
            rds_single_generator.set_security_group_id(self.security_group_id)

        return {
            "DBInstances": [
                rds_single_generator.generate()
            ],
            "ResponseMetadata": {
                "RequestId": "abc12-def0990-12ab-cd56-fab123456ab",
                "HTTPStatusCode": 200,
                "HTTPHeaders": {
                    "x-amzn-requestid": "abc12-def0990-12ab-cd56-fab123456ab",
                    "content-type": "text/xml",
                    "content-length": "4123124523",
                    "vary": "accept-encoding",
                    "date": "Tue, 32 Aug 2012 14:61:22 GMT"
                },
                "RetryAttempts": 0
            }
        }