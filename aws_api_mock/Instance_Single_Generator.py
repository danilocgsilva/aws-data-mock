from email.policy import default
from aws_api_mock.Entity_Generator_Command_Interface import Entity_Generator_Command_Interface
from aws_api_mock.aws_data_helpers import get_exadecimal_sample
from aws_api_mock.AWS_General_Entities_Mocker import AWS_General_Entities_Mocker
from aws_api_mock.FullFormatDateMocking import FullFormatDateMocking

class Instance_Single_Generator(Entity_Generator_Command_Interface):

    def __init__(self):
        self.instance_id = None
        self.public_ip = None
        self.tags = []
        self.aws_general_entities_mocker = AWS_General_Entities_Mocker()

    def setInstanceId(self, instance_id: str):
        self.instance_id = instance_id
        return self

    def setPublicIp(self, publicId: str):
        self.public_ip = publicId

    def addTag(self, key: str, value: str):

        new_tags = {
            "Key": key,
            "Value": value
        }

        self.tags.append(new_tags)

    def set_data(self):
        if not self.public_ip:
            self.public_ip = self.aws_general_entities_mocker.get_ip()

    def generate(self) -> dict:
        self.set_data()
        private_ip = self.aws_general_entities_mocker.get_ip()
        subnet_id = "subnet-" + get_exadecimal_sample(8)
        vpc_id = "vpc-" + get_exadecimal_sample(8)
        security_group_id = "sg-" + get_exadecimal_sample(17)
        owner_id = self.aws_general_entities_mocker.get_owner_id()
        if self.instance_id:
            instance_id_hexa = self.instance_id
        else:
            instance_id_hexa = get_exadecimal_sample(17)

        default_tag = {
            "Key": "Description",
            "Value": "General porpouse machine"
        }

        self.tags.append(default_tag)

        instance_data = {
            "AmiLaunchIndex": 0,
            "ImageId": "ami-" + get_exadecimal_sample(17),
            "InstanceId": "i-" + instance_id_hexa,
            "InstanceType": "t2.micro",
            "KeyName": "my-secret-key",
            "LaunchTime": FullFormatDateMocking().getRandomTimeStringZ(),
            "Monitoring": {
                "State": "disabled"
            },
            "Placement": {
                "AvailabilityZone": "us-east-1b",
                "GroupName": "",
                "Tenancy": "default"
            },
            "Platform": "windows",
            "PrivateDnsName": "ip-" + private_ip.replace(".", "-") + ".ec2.internal",
            "PrivateIpAddress": private_ip,
            "ProductCodes": [],
            "PublicDnsName": "",
            "PublicIpAddress": self.public_ip,
            "State": {
                "Code": 80,
                "Name": "stopped"
            },
            "StateTransitionReason": "User initiated (2018-12-11 11:13:25 GMT)",
            "SubnetId": subnet_id,
            "VpcId": vpc_id,
            "Architecture": "x86_64",
            "BlockDeviceMappings": [
                {
                    "DeviceName": "/dev/sda1",
                    "Ebs": {
                        "AttachTime": "2018-10-18T00:44:49.000Z",
                        "DeleteOnTermination": True,
                        "Status": "attached",
                        "VolumeId": "vol-" + get_exadecimal_sample(17)
                    }
                }
            ],
            "ClientToken": "",
            "EbsOptimized": False,
            "EnaSupport": True,
            "Hypervisor": "xen",
            "NetworkInterfaces": [
                self.aws_general_entities_mocker.get_mocked_network_interface_data(
                    security_group_id, 
                    owner_id, 
                    private_ip,
                    subnet_id,
                    vpc_id
                )
            ],
            "RootDeviceName": "/dev/sda1",
            "RootDeviceType": "ebs",
            "SecurityGroups": [
                {
                    "GroupName": "default",
                    "GroupId": security_group_id
                }
            ],
            "SourceDestCheck": True,
            "StateReason": {
                "Code": "Client.UserInitiatedShutdown",
                "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
            },
            "Tags": self.tags,
            "VirtualizationType": "hvm",
            "CpuOptions": {
                "CoreCount": 1,
                "ThreadsPerCore": 1
            },
            "CapacityReservationSpecification": {
                "CapacityReservationPreference": "open"
            },
            "HibernationOptions": {
                "Configured": False
            },
            "MetadataOptions": {
                "State": "applied",
                "HttpTokens": "optional",
                "HttpPutResponseHopLimit": 1,
                "HttpEndpoint": "enabled"
            }
        }
                 
        return instance_data
