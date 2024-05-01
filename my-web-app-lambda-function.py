import json

def lambda_handler(event, context):
    name = event['firstname'] +' '+ event['lastname'] +' '+ event['phone_number']

    return {
    'statusCode': 200,
    'body': json.dumps('Hello from Lambda, ' + name)
    }