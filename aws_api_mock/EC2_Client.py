class EC2_Client:

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

