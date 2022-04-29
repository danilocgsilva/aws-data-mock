from awsapimock.Entity_Generator_Command_Interface import Entity_Generator_Command_Interface
from awsapimock.aws_data_helpers import generate_owner_code, get_exadecimal_sample, generate_random_string_with_hard_chars, random_until_n


class Lambda_Data_Generator(Entity_Generator_Command_Interface):

    def generate(self) -> dict:

        owner_code = generate_owner_code()

        data = {
            "FunctionName": "firstResponse",
            "FunctionArn": "arn:aws:lambda:mo-east-1:" + owner_code + ":function:firstResponse",
            "Runtime": "python3.6",
            "Role": "arn:aws:iam::" + owner_code + ":role/service-role/firstResponse",
            "Handler": "lambda_function.lambda_handler",
            "CodeSize": random_until_n(1000000),
            "Description": "",
            "Timeout": 3,
            "MemorySize": 128,
            "LastModified": "2011-08-17T18:56:00.842+0000",
            "CodeSha256": generate_random_string_with_hard_chars(44),
            "Version": "$LATEST",
            "TracingConfig": {
                "Mode": "PassThrough"
            },
            "RevisionId": get_exadecimal_sample(8) + "-" + get_exadecimal_sample(4) + "-" + get_exadecimal_sample(4) + "-" + get_exadecimal_sample(4) + "-" + get_exadecimal_sample(12)
        }

        return data

