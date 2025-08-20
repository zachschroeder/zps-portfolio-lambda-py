import boto3
import uuid

from common.commands import CreateMovie


def lambda_handler(command, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("Events")

    print(f"Command: {command}")

    try:
        CreateMovie.validate_dict(command)
        command["id"] = str(uuid.uuid4())
        command["type"] = "MovieCreated"
        table.put_item(Item=command)
    except ValueError as e:
        print(e)
        return {"status_code": 400, "body": "Invalid data supplied"}
    except Exception as e:
        print(e)
        return {"status_code": 500, "body": "Item not inserted"}

    return {"status_code": 200, "body": "Item successfully inserted!"}
