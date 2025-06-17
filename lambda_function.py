import uuid
import boto3
import json
import os

from movie import Movie


def main():
    jsonDict = {"id": str(uuid.uuid4()), "title": "New Movie", "director": "Mr. Director"}
    result = lambda_handler(jsonDict, "local_context")
    print(result)


def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("Items")

    print(f"Event: {event}")
    
    try:
        # movie = Movie(**json.loads(event))

        table.put_item(Item=event)
    except Exception as e:
        print(e)
        return {"statusCode": 500, "body": "Item not inserted"}

    return {"statusCode": 200, "body": "Item successfully inserted!"}


if os.getenv("AWS_EXECUTION_ENV") is None:
    main()
