class EC2_Client:

    def describe_images(self, *args, **kwargs) -> list:
        return {
            "Images": [
                {
                    "Architecture": "x86_64",
                    "CreationDate": "2020-09-08T00:55:25.000Z",
                    "ImageId": "ami-0dba2cb6798deb6d8",
                    "ImageLocation": "099720109477/ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-20200907",
                    "ImageType": "machine",
                    "Public": True,
                    "OwnerId": "099720109477",
                    "PlatformDetails": "Linux/UNIX",
                    "UsageOperation": "RunInstances",
                    "State": "available",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "DeleteOnTermination": True,
                                "SnapshotId": "snap-0f06f1549ff7327c9",
                                "VolumeSize": 8,
                                "VolumeType": "gp2",
                                "Encrypted": False
                            }
                        },
                        {
                            "DeviceName": "/dev/sdb",
                            "VirtualName": "ephemeral0"
                        },
                        {
                            "DeviceName": "/dev/sdc",
                            "VirtualName": "ephemeral1"
                        }
                    ],
                    "Description": "Canonical, Ubuntu, 20.04 LTS, amd64 focal image build on 2020-09-07",
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "Name": "ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-20200907",
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SriovNetSupport": "simple",
                    "VirtualizationType": "hvm",
                    "DeprecationTime": "2022-09-08T00:55:25.000Z"
                }
            ],
            "ResponseMetadata": {
                "RequestId": "fe624dc5-f56b-4dca-8ec7-f91ba02ba4f4",
                "HTTPStatusCode": 200,
                "HTTPHeaders": {
                    "x-amzn-requestid": "fe624dc5-f56b-4dca-8ec7-f91ba02ba4f4",
                    "cache-control": "no-cache, no-store",
                    "strict-transport-security": "max-age=31536000; includeSubDomains",
                    "vary": "accept-encoding",
                    "content-type": "text/xml;charset=UTF-8",
                    "content-length": "2256",
                    "date": "Tue, 31 May 2022 04:21:19 GMT",
                    "server": "AmazonEC2"
                },
                "RetryAttempts": 0
            }
        }

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

