from aws_api_mock.Entity_Generator_Command_Interface import Entity_Generator_Command_Interface
from aws_api_mock.AWS_General_Entities_Mocker import AWS_General_Entities_Mocker
from aws_api_mock.Instance_Single_Generator import Instance_Single_Generator
from aws_api_mock.aws_data_helpers import get_exadecimal_sample

class Instance_Request_Generator(Entity_Generator_Command_Interface):

    def generate(self, count = 1) -> dict:
        aws_general_entities_mocker = AWS_General_Entities_Mocker()

        owner_id = aws_general_entities_mocker.get_owner_id()

        instance_single_generator = Instance_Single_Generator()
        instances = []
        for i in range(0, count):
            instances.append(instance_single_generator.generate())

        data = {
            "Reservations": [
                {
                    "Groups": [],
                    "Instances": instances,
                    "OwnerId": owner_id,
                    "ReservationId": "r-" + get_exadecimal_sample(17)
                }
            ]
        }

        return data
