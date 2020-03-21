import boto3

if __name__ == '__main__':

    dynamodb = boto3.resource('dynamodb','us-east-1')
    table = dynamodb.Table('Books')
    r = table.put_item(Item={
                         "Author": "John Grisham",
                         "Title": "The Rainmaker",
                         "Category": "Suspense",
                         "Formats": {
                                        "Hardcover": "J4SUKVGU",
                                        "Paperback": "D7YF4FCX"
                                    }
                        })

    print(r)