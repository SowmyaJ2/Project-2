import json
import boto3
from time import gmtime, strftime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('contact-management-system-table')
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

def lambda_handler(event, context):
    name = event['firstname'] +' '+ event['lastname'] +' '+ event['phone_number']
    response = table.put_item(
        Item={
            'ID': name,
            'LatestGreetingTime':now
            })

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda, ' + name)
    }
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda, ' + name)
    }