from aws_api_mock.Entity_Generator_Command_Interface import Entity_Generator_Command_Interface
from aws_api_mock.VpcSecurityGroup_Data_Generator import VpcSecurityGroup_Data_Generator
from aws_api_mock.RDS_Factory import RDS_Factory

class RDS_Single_Data_Generator(Entity_Generator_Command_Interface):

    def __init__(self):
        self.security_group_id = None
        self.rds_factory = RDS_Factory()

    def set_security_group_id(self, security_group_id: str):
        self.security_group_id = security_group_id

    def generate(self) -> dict:

        sg_generator = VpcSecurityGroup_Data_Generator()

        if self.security_group_id:
            sg_generator.set_group_id(self.security_group_id)

        return {
              "DBInstanceIdentifier": self.rds_factory.get_DBInstanceIdentifier(),
              "DBInstanceClass": self.rds_factory.get_DBInstanceClass(),
              "Engine": "mysql",
              "DBInstanceStatus": "available",
              "MasterUsername": self.rds_factory.get_MasterUsername(),
              "DBName": self.rds_factory.get_DBName(),
              "Endpoint": {
                  "Address": self.rds_factory.get_EndpointAddress(),
                  "Port": 3306,
                  "HostedZoneId": self.rds_factory.get_EndpointHostedZoneId()
              },
              "AllocatedStorage": 20,
              "PreferredBackupWindow": self.rds_factory.get_PreferredBackupWindow(),
              "BackupRetentionPeriod": 72,
              "DBSecurityGroups": [],
              "VpcSecurityGroups": [
                  sg_generator.generate()
              ],
              "DBParameterGroups": [
                  {
                      "DBParameterGroupName": "default.mysql4.0",
                      "ParameterApplyStatus": "in-sync"
                  }
              ],
              "AvailabilityZone": "mo-east-4e",
              "DBSubnetGroup": {
                  "DBSubnetGroupName": "default",
                  "DBSubnetGroupDescription": "default",
                  "VpcId": "vpc-890ab56cd",
                  "SubnetGroupStatus": "Complete",
                  "Subnets": [
                      {
                          "SubnetIdentifier": "subnet-abab1212",
                          "SubnetAvailabilityZone": {
                              "Name": "mo-east-4a"
                          },
                          "SubnetStatus": "Active"
                      },
                      {
                          "SubnetIdentifier": "subnet-cdcd5656",
                          "SubnetAvailabilityZone": {
                              "Name": "mo-east-4b"
                          },
                          "SubnetStatus": "Active"
                      },
                      {
                          "SubnetIdentifier": "subnet-123fd12ab",
                          "SubnetAvailabilityZone": {
                              "Name": "mo-east-4d"
                          },
                          "SubnetStatus": "Active"
                      },
                      {
                          "SubnetIdentifier": "subnet-ab123456f",
                          "SubnetAvailabilityZone": {
                              "Name": "mo-east-4f"
                          },
                          "SubnetStatus": "Active"
                      },
                      {
                          "SubnetIdentifier": "subnet-a01b34c56",
                          "SubnetAvailabilityZone": {
                              "Name": "mo-east-4e"
                          },
                          "SubnetStatus": "Active"
                      },
                      {
                          "SubnetIdentifier": "subnet-d78e90f12",
                          "SubnetAvailabilityZone": {
                              "Name": "mo-east-4c"
                          },
                          "SubnetStatus": "Active"
                      }
                  ]
              },
              "PreferredMaintenanceWindow": "fri:04:33-fri:05:03",
              "PendingModifiedValues": {},
              "MultiAZ": False,
              "EngineVersion": "4.0.'01",
              "AutoMinorVersionUpgrade": False,
              "ReadReplicaDBInstanceIdentifiers": [],
              "LicenseModel": "mit",
              "OptionGroupMemberships": [
                  {
                      "OptionGroupName": "default:mysql-4-0",
                      "Status": "in-sync"
                  }
              ],
              "PubliclyAccessible": True,
              "StorageType": "gp2",
              "DbInstancePort": 0,
              "StorageEncrypted": False,
              "DbiResourceId": "db-AD89ASDFA7SDF6AS7D6",
              "CACertificateIdentifier": "rds-ca-2008",
              "DomainMemberships": [],
              "CopyTagsToSnapshot": False,
              "MonitoringInterval": 0,
              "DBInstanceArn": "arn:aws:rds:mo-east-4:13418273987:db:main-database",
              "IAMDatabaseAuthenticationEnabled": False,
              "PerformanceInsightsEnabled": False,
              "DeletionProtection": False,
              "AssociatedRoles": []
        }
