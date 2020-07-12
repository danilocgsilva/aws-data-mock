from awsclimock.Commands_Output.Entity_Generator_Command_Interface import Entity_Generator_Command_Interface

class Regions_Data_Generator(Entity_Generator_Command_Interface):

    def generate(self) -> dict:

        return {
            "Regions": [
                {
                    "Endpoint": "ec2.eu-north-1.amazonaws.com",
                    "RegionName": "eu-north-1",
                    "OptInStatus": "opt-in-not-required"
                },
                {
                    "Endpoint": "ec2.ap-south-1.amazonaws.com",
                    "RegionName": "ap-south-1",
                    "OptInStatus": "opt-in-not-required"
                },
                {
                    "Endpoint": "ec2.eu-west-3.amazonaws.com",
                    "RegionName": "eu-west-3",
                    "OptInStatus": "opt-in-not-required"
                },
                {
                    "Endpoint": "ec2.eu-west-2.amazonaws.com",
                    "RegionName": "eu-west-2",
                    "OptInStatus": "opt-in-not-required"
                },
                {
                    "Endpoint": "ec2.eu-west-1.amazonaws.com",
                    "RegionName": "eu-west-1",
                    "OptInStatus": "opt-in-not-required"
                },
                {
                    "Endpoint": "ec2.ap-northeast-2.amazonaws.com",
                    "RegionName": "ap-northeast-2",
                    "OptInStatus": "opt-in-not-required"
                },
                {
                    "Endpoint": "ec2.ap-northeast-1.amazonaws.com",
                    "RegionName": "ap-northeast-1",
                    "OptInStatus": "opt-in-not-required"
                },
                {
                    "Endpoint": "ec2.sa-east-1.amazonaws.com",
                    "RegionName": "sa-east-1",
                    "OptInStatus": "opt-in-not-required"
                },
                {
                    "Endpoint": "ec2.ca-central-1.amazonaws.com",
                    "RegionName": "ca-central-1",
                    "OptInStatus": "opt-in-not-required"
                },
                {
                    "Endpoint": "ec2.ap-southeast-1.amazonaws.com",
                    "RegionName": "ap-southeast-1",
                    "OptInStatus": "opt-in-not-required"
                },
                {
                    "Endpoint": "ec2.ap-southeast-2.amazonaws.com",
                    "RegionName": "ap-southeast-2",
                    "OptInStatus": "opt-in-not-required"
                },
                {
                    "Endpoint": "ec2.eu-central-1.amazonaws.com",
                    "RegionName": "eu-central-1",
                    "OptInStatus": "opt-in-not-required"
                },
                {
                    "Endpoint": "ec2.us-east-1.amazonaws.com",
                    "RegionName": "us-east-1",
                    "OptInStatus": "opt-in-not-required"
                },
                {
                    "Endpoint": "ec2.us-east-2.amazonaws.com",
                    "RegionName": "us-east-2",
                    "OptInStatus": "opt-in-not-required"
                },
                {
                    "Endpoint": "ec2.us-west-1.amazonaws.com",
                    "RegionName": "us-west-1",
                    "OptInStatus": "opt-in-not-required"
                },
                {
                    "Endpoint": "ec2.us-west-2.amazonaws.com",
                    "RegionName": "us-west-2",
                    "OptInStatus": "opt-in-not-required"
                }
            ]
        }
