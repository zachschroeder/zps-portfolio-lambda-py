def lambda_handler(event, context):
    for record in event['Records']:
        event_data = record['dynamodb']['NewImage']
        print(event_data['title']['S'])

    return 'Successfully processed records'
