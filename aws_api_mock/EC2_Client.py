from datetime import datetime


import datetime
from dateutil.tz import tzutc

class EC2_Client:

    def describe_images(self) -> list:
        return [
            {
                "AmiLaunchIndex": 0,
                "ImageId": "ami-c2db96fa4c97eafae",
                "InstanceId": "i-33f65e69d7e4c700c",
                "InstanceType": "t2.nano",
                "KeyName": "main4",
                "LaunchTime": datetime.datetime(2012,5,29,23,1,51, tzinfo=tzutc()),
                "Monitoring": {
                    "State": "disabled"
                },
                "Placement": {
                    "AvailabilityZone": "us-east-1b",
                    "GroupName": "",
                    "Tenancy": "default"
                },
                "PrivateDnsName": "ip-112-45-1-42.ec2.internal",
                "PrivateIpAddress": "112.45.1.2.42",
                "ProductCodes": [],
                "PublicDnsName": "ec2-43-112-265-55.compute-1.amazonaws.com",
                "PublicIpAddress": "43.112.265.55",
                "State": {
                    "Code": 16,
                    "Name": "running"
                },
                "StateTransitionReason": "",
                "SubnetId": "subnet-b4ed4596f46c79e50",
                "VpcId": "vpc-67c488b7474976a52",
                "Architecture": "x86_64",
                "BlockDeviceMappings": [
                    {
                        "DeviceName": "/dev/sda1",
                        "Ebs": {
                            "AttachTime": datetime.datetime(2012,5,29,23,1,52, tzinfo=tzutc()),
                            "DeleteOnTermination": True,
                            "Status": "attached",
                            "VolumeId": "vol-0add7002f633105d1"
                        }
                    }
                ],
                "ClientToken": "f015b066-af24-456b-97e9-3494e3e054a4",
                "EbsOptimized": False,
                "EnaSupport": True,
                "Hypervisor": "xen",
                "NetworkInterfaces": [
                    {
                        "Association": {
                            "IpOwnerId": "amazon",
                            "PublicDnsName": "ec2-43-112-265-55.compute-1.amazonaws.com",
                            "PublicIp": "43.112.265.55"
                        },
                        "Attachment": {
                            "AttachTime": datetime.datetime(2012,5,29,23,1,51, tzinfo=tzutc()),
                            "AttachmentId": "eni-attach-0658d7c11b9197790",
                            "DeleteOnTermination": True,
                            "DeviceIndex": 0,
                            "Status": "attached",
                            "NetworkCardIndex": 0
                        },
                        "Description": "",
                        "Groups": [
                            {
                                "GroupName": "securitygroup-at-20220529-20h01m37s",
                                "GroupId": "sg-577df71317764547b"
                            }
                        ],
                        "Ipv6Addresses": [],
                        "MacAddress": "12:b6:bf:d8:7e:5b",
                        "NetworkInterfaceId": "eni-0b88bdad9de246cd6",
                        "OwnerId": "063695957269",
                        "PrivateDnsName": "ip-112-45-1-42.ec2.internal",
                        "PrivateIpAddress": "112.45.1.2.42",
                        "PrivateIpAddresses": [
                            {
                                "Association": {
                                    "IpOwnerId": "amazon",
                                    "PublicDnsName": "ec2-43-112-265-55.compute-1.amazonaws.com",
                                    "PublicIp": "43.112.265.55"
                                },
                                "Primary": True,
                                "PrivateDnsName": "ip-112-45-1-42.ec2.internal",
                                "PrivateIpAddress": "112.45.1.2.42"
                            }
                        ],
                        "SourceDestCheck": True,
                        "Status": "in-use",
                        "SubnetId": "subnet-b4ed4596f46c79e50",
                        "VpcId": "vpc-67c488b7474976a52",
                        "InterfaceType": "interface"
                    }
                ],
                "RootDeviceName": "/dev/sda1",
                "RootDeviceType": "ebs",
                "SecurityGroups": [
                    {
                        "GroupName": "securitygroup-at-20120529-20h01m37s",
                        "GroupId": "sg-577df71317764547b"
                    }
                ],
                "SourceDestCheck": True,
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
                    "HttpEndpoint": "enabled",
                    "HttpProtocolIpv6": "disabled"
                },
                "EnclaveOptions": {
                    "Enabled": False
                },
                "PlatformDetails": "Linux/UNIX",
                "UsageOperation": "RunInstances",
                "UsageOperationUpdateTime": datetime.datetime(2012,5,29,23,1,51, tzinfo=tzutc())
            }
        ]

    def describe_vpcs(self) -> dict:

        return {
            "Vpcs": [
                {
                    "CidrBlock": "212.14.0.0/24",
                    "DhcpOptionsId": "dopt-df8915a4",
                    "State": "available",
                    "VpcId": "vpc-fc6d63e7c67246b85",
                    "OwnerId": "072414042480",
                    "InstanceTenancy": "default",
                    "CidrBlockAssociationSet": [
                        {
                            "AssociationId": "vpc-cidr-assoc-47d62c0ab29db840e",
                            "CidrBlock": "212.14.0.0/24",
                            "CidrBlockState": {
                                "State": "associated"
                            }
                        }
                    ],
                    "IsDefault": False
                },
                {
                    "CidrBlock": "212.14.0.0/24",
                    "DhcpOptionsId": "dopt-df8915a4",
                    "State": "available",
                    "VpcId": "vpc-fe60876b",
                    "OwnerId": "072414042480",
                    "InstanceTenancy": "default",
                    "CidrBlockAssociationSet": [
                        {
                            "AssociationId": "vpc-cidr-assoc-e936db7a",
                            "CidrBlock": "212.14.0.0/24",
                            "CidrBlockState": {
                                "State": "associated"
                            }
                        }
                    ],
                    "IsDefault": True
                },
                {
                    "CidrBlock": "212.14.0.0/24",
                    "DhcpOptionsId": "dopt-df8915a4",
                    "State": "available",
                    "VpcId": "vpc-d00f33fc1efcdc317",
                    "OwnerId": "072414042480",
                    "InstanceTenancy": "default",
                    "CidrBlockAssociationSet": [
                        {
                            "AssociationId": "vpc-cidr-assoc-4636c99db40da124f",
                            "CidrBlock": "212.14.0.0/24",
                            "CidrBlockState": {
                                "State": "associated"
                            }
                        }
                    ],
                    "IsDefault": False
                }
            ],
            "ResponseMetadata": {
                "RequestId": "5850b275-d588-7397-3a64-0887119c884f",
                "HTTPStatusCode": 200,
                "HTTPHeaders": {
                    "x-amzn-requestid": "5850b275-d588-7397-3a64-0887119c884f",
                    "cache-control": "no-cache, no-store",
                    "strict-transport-security": "max-age=31536000; includeSubDomains",
                    "vary": "accept-encoding",
                    "content-type": "text/xml;charset=UTF-8",
                    "content-length": "2465",
                    "date": "Sat, 28 May 2017 22:12:59 GMT",
                    "server": "AmazonEC2"
                },
                "RetryAttempts": 0
            }
        }

