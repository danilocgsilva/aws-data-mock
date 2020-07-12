import math
from random import random
from awsapimock.Ip_Permission_Generator import Ip_Permission_Generator
from awsapimock.Tag_Generator import Tag_Generator
from awsapimock.aws_data_helpers import get_exadecimal_sample

class Security_Group_Data_Generator:

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
            tags.append(TagGenerator.get_tag())

        return tags


    def get_vpc_id(self) -> str:
        return "vpc-" + get_exadecimal_sample(8)

