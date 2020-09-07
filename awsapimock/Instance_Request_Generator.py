from awsapimock.Entity_Generator_Command_Interface import Entity_Generator_Command_Interface
from awsapimock.AWS_General_Entities_Mocker import AWS_General_Entities_Mocker
from awsapimock.Instance_Single_Generator import Instance_Single_Generator
from awsapimock.aws_data_helpers import get_exadecimal_sample


class Instance_Request_Generator(Entity_Generator_Command_Interface):

    def generate(self) -> dict:
        aws_general_entities_mocker = AWS_General_Entities_Mocker()

        owner_id = aws_general_entities_mocker.get_owner_id()

        data = {
            "Reservations": [
                {
                    "Groups": [],
                    "Instances": [
                        Instance_Single_Generator().generate()
                    ],
                    "OwnerId": owner_id,
                    "ReservationId": "r-" + get_exadecimal_sample(17)
                }
            ]
        }

        return data
