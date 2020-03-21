import boto3
import json

if __name__ == '__main__':

    dynamodb = boto3.resource('dynamodb', 'us-east-1')
    table = dynamodb.Table('Books')

    with open("books.json") as json_file:
        books = json.load(json_file)
        with table.batch_writer() as batch:
            for book in books:
                batch.put_item(Item=book)