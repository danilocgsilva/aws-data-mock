import math
from random import random
from awsapimock.aws_data_helpers import random_until_255, get_exadecimal_sample, get_mac_address

class AWS_General_Entities_Mocker:

    def get_owner_id(self):

        owner_id = ""
        for x in range(12):
            owner_id += str(math.ceil(random() * 10))

        return owner_id


    def get_ip(self):
        return "-".join([random_until_255(), random_until_255(), random_until_255(), random_until_255()])


    def get_mocked_network_interface_data(
        self,
        security_group_id: str, 
        owner_id: str, 
        private_ip: str,
        subnet_id: str,
        vpc_id: str
    ) -> dict:
        return {
            "Attachment": {
                "AttachTime": self.getRandomTimeStringZ(),
                "AttachmentId": "eni-attach-" + get_exadecimal_sample(17),
                "DeleteOnTermination": True,
                "DeviceIndex": 0,
                "Status": "attached"
            },
            "Description": "",
            "Groups": [
                {
                    "GroupName": "default",
                    "GroupId": security_group_id
                }
            ],
            "Ipv6Addresses": [],
            "MacAddress": get_mac_address(),
            "NetworkInterfaceId": "eni-" + get_exadecimal_sample(17),
            "OwnerId": owner_id,
            "PrivateDnsName": "ip-" + private_ip.replace(".", "-") + ".ec2.internal",
            "PrivateIpAddress": private_ip,
            "PrivateIpAddresses": [
                {
                    "Primary": True,
                    "PrivateDnsName": "ip-" + private_ip.replace(".", "-") + ".ec2.internal",
                    "PrivateIpAddress": private_ip
                }
            ],
            "SourceDestCheck": True,
            "Status": "in-use",
            "SubnetId": subnet_id,
            "VpcId": vpc_id,
            "InterfaceType": "interface"
        }

    def getRandomTimeStringZ(self) -> str:

        year = str(math.ceil((random() * 10) + 2010))
        month = '{:02}'.format(math.ceil(random() * 12))
        day = '{:02}'.format(math.ceil(random() * 28))
        hour = '{:02}'.format(math.floor(random() * 24))
        minute = '{:02}'.format(math.floor(random() * 60))
        second = '{:02}'.format(math.floor(random() * 60))

        return year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + ".000Z"

    def getRandomTimeStringGMT(self) -> str:
        return '2018-12-11 11:13:25 GMT'