import boto3

if __name__ == '__main__':

    dynamodb = boto3.resource('dynamodb', 'us-east-1')
    table = dynamodb.Table('Books')
    resp = table.get_item(Key={"Author": "Иван Вазов", "Title": "Под игото"})

    print(resp['Item'])
