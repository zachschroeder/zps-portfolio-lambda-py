import boto3
import uuid
import os


def main():
    result = lambda_handler("local_event", "local_context")
    print(result)


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Items')

    item = {
        'id': str(uuid.uuid4()),
        'name': 'Sample Item',
        'category': 'Example'
    }

    try:
        table.put_item(Item=item)
    except:
        return {
            'statusCode': 500,
            'body': 'Item not inserted'
        }

    return {
        'statusCode': 200,
        'body': 'Item successfully inserted!'
    }


if os.getenv("AWS_EXECUTION_ENV") is None:
    main()
