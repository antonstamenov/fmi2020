import boto3
from boto3.dynamodb.conditions import Key


if __name__ == '__main__':

    dynamodb = boto3.resource('dynamodb','us-east-1')
    table = dynamodb.Table('Books')

    resp = table.query(KeyConditionExpression=Key('Author').eq('John Grisham'))

    print("The query returned the following items:")
    for item in resp['Items']:
        print(item)
