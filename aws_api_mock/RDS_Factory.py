from aws_api_mock.Factory_Simple import Factory_Simple

class RDS_Factory:

    def __init__(self):

        self.DBInstanceIdentifierFactory = Factory_Simple().\
            set_possibles("main-database").\
            set_possibles("myinstance")

        self.DBInstanceClassFactory = Factory_Simple().\
            set_possibles("db.t2.supermini").\
            set_possibles("db.t2.micro")

        self.MasterUsernameFactory = Factory_Simple().\
            set_possibles("root").\
            set_possibles("master_name")

        self.DBNameFactory = Factory_Simple().\
            set_possibles("themaindatabase").\
            set_possibles("main_database")

        self.EndpointAddressFactory = Factory_Simple().\
            set_possibles("main-database.abcdefgwyz.mo-east-4.rds.amazonaws.com").\
            set_possibles("main_database.luisdkjsghf.mo-east-2.rds.amazonaws.com")

        self.EndpointHostedZoneIdFactory = Factory_Simple().\
            set_possibles("ABCDEXYZ1234890").\
            set_possibles("asldjfhakslalkj")

        self.PreferredBackupWindowFactory = Factory_Simple().\
            set_possibles("12:00-13:00").\
            set_possibles("06:19-06:49")

    def get_DBInstanceIdentifier(self) -> str:
        return self.DBInstanceIdentifierFactory.get_extracting()

    def get_DBInstanceClass(self) -> str:
        return self.DBInstanceClassFactory.get_extracting()

    def get_MasterUsername(self) -> str:
        return self.MasterUsernameFactory.get_extracting()

    def get_DBName(self) -> str:
        return self.DBNameFactory.get_extracting()

    def get_EndpointAddress(self) -> str:
        return self.EndpointAddressFactory.get_extracting()

    def get_EndpointHostedZoneId(self) -> str:
        return self.EndpointHostedZoneIdFactory.get_extracting()

    def get_PreferredBackupWindow(self) -> str:
        return self.PreferredBackupWindowFactory.get_extracting()
