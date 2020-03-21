import boto3
import json

if __name__ == '__main__':
    s3 = boto3.client('s3', 'us-east-1')
    book = s3.get_object(Bucket='gium', Key='id1')['Body'].read().decode('utf-8')
    print(book)
