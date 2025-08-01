import json
import os

from event_projector.event_data import dev_event_json


def main():
    input = json.loads(dev_event_json)
    result = lambda_handler(input, "local_context")
    print(result)


def lambda_handler(event, context):
    for record in event['Records']:
        event_data = record['dynamodb']['NewImage']
        print(event_data['title']['S'])

    return 'Successfully processed records'


if os.getenv("AWS_EXECUTION_ENV") is None:
    main()
