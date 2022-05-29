import math
from random import random
from aws_api_mock.Entity_Generator_Command_Interface import Entity_Generator_Command_Interface
from aws_api_mock.Ip_Permission_Generator import Ip_Permission_Generator
from aws_api_mock.Tag_Generator import Tag_Generator
from aws_api_mock.aws_data_helpers import get_exadecimal_sample
from aws_api_mock.AWS_General_Entities_Mocker import AWS_General_Entities_Mocker

class Security_Group_Data_Generator(Entity_Generator_Command_Interface):

    def generate(self) -> dict:

        security_group_data_generator = Security_Group_Data_Generator()
        vpc_id = security_group_data_generator.get_vpc_id()

        data = {
            "SecurityGroups": [
                {
                    "Description": "Santa Fé",
                    "GroupName": "santa-fe",
                    "IpPermissions": security_group_data_generator.get_ip_permissions(0),
                    "OwnerId": AWS_General_Entities_Mocker().get_owner_id(),
                    "GroupId": security_group_data_generator.get_group_id(),
                    "IpPermissionEgress": security_group_data_generator.get_ip_permissions(1),
                    "Tags": security_group_data_generator.get_tags(1),
                    "VpcId": vpc_id
                }
            ]
        }

        return data


    def get_ip_permissions(self, num: int):
        
        ip_permissions = []

        for x in range(num):
            ip_permissions.append(Ip_Permission_Generator.get_ip_permission())

        return ip_permissions


    def get_group_id(self):
        return "sg-" + get_exadecimal_sample(17)


    def get_tags(self, num: int):

        tags = []

        for x in range(num):
            tags.append(Tag_Generator().get_tag())

        return tags


    def get_vpc_id(self) -> str:
        return "vpc-" + get_exadecimal_sample(8)

