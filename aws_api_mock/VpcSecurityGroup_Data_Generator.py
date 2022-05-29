from aws_api_mock.Entity_Generator_Command_Interface import Entity_Generator_Command_Interface
from aws_api_mock.aws_data_helpers import get_exadecimal_sample

class VpcSecurityGroup_Data_Generator(Entity_Generator_Command_Interface):

    def __init__(self):
        self.group_id = "sg-" + get_exadecimal_sample(11)

    def set_group_id(self, group_id: str):
        self.group_id = group_id
        return self

    def generate(self):
        return {
            "VpcSecurityGroupId": self.group_id,
            "Status": "active"
        }
