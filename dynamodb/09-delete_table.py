import boto3

if __name__ == '__main__':
    dynamodb = boto3.client('dynamodb','us-east-1')
    resp = dynamodb.delete_table(TableName="Books")
    print("Table deleted successfully!")
