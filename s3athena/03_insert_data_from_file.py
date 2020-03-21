import boto3
import json

if __name__ == '__main__':
    s3 = boto3.client('s3', 'us-east-1')
    id=1
    with open("books.json") as json_file:
        books = json.load(json_file)
        for book in books:
            id+=1
            s3.put_object(Bucket='gium', Key=f'books/id{id}', Body=json.dumps(book), ContentType='application/json')