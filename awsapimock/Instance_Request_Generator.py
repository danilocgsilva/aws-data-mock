from awsapimock.Entity_Generator_Command_Interface import Entity_Generator_Command_Interface
from awsapimock.AWS_General_Entities_Mocker import AWS_General_Entities_Mocker
from awsapimock.aws_data_helpers import get_exadecimal_sample


class Instance_Request_Generator(Entity_Generator_Command_Interface):

    def generate(self) -> dict:
        aws_general_entities_mocker = AWS_General_Entities_Mocker()

        owner_id = aws_general_entities_mocker.get_owner_id()
        private_ip = aws_general_entities_mocker.get_ip()
        subnet_id = "subnet-" + get_exadecimal_sample(8)
        vpc_id = "vpc-" + get_exadecimal_sample(8)
        security_group_id = "sg-" + get_exadecimal_sample(17)

        data = {
            "Reservations": [
                {
                    "Groups": [],
                    "Instances": [
                        {
                            "AmiLaunchIndex": 0,
                            "ImageId": "ami-" + get_exadecimal_sample(17),
                            "InstanceId": "i-" + get_exadecimal_sample(17),
                            "InstanceType": "t2.micro",
                            "KeyName": "my-secret-key",
                            "LaunchTime": "2018-01-05T09:05:52.000Z",
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
                                aws_general_entities_mocker.get_mocked_network_interface_data(
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
                            "Tags": [
                                {
                                    "Key": "Description",
                                    "Value": "General porpouse machine"
                                },
                            ],
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
                    ],
                    "OwnerId": owner_id,
                    "ReservationId": "r-" + get_exadecimal_sample(17)
                }
            ]
        }

        return data