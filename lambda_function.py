import uuid
import boto3
import os

from movie import Movie


def main():
    input = {"id": str(uuid.uuid4()), "title": "New Movie", "director": "Mr. Director"}
    result = lambda_handler(input, "local_context")
    print(result)

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("Items")

    print(f"Event: {event}")

# Temp code for reading items
    # items = table.scan()
    # for item in items['Items']:
    #     print(item)
    #     print(item.get('temp'))

    try:
        Movie.validate_data(event)
        table.put_item(Item=event)
    except ValueError as e:
        print(e)
        return {"statusCode": 400, "body": "Invalid data supplied"}
    except Exception as e:
        print(e)
        return {"statusCode": 500, "body": "Item not inserted"}

    return {"statusCode": 200, "body": "Item successfully inserted!"}


if os.getenv("AWS_EXECUTION_ENV") is None:
    main()
