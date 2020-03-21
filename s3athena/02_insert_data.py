import boto3
import json

if __name__ == '__main__':
    s3 = boto3.client('s3', 'us-east-1')

    book = {
                 "Author": "John Grisham",
                 "Title": "The Rainmaker",
                 "Category": "Suspense",
                 "Formats": {
                                "Hardcover": "J4SUKVGU",
                                "Paperback": "D7YF4FCX"
                            }
            }
    book_ser = json.dumps(book)
    s3.put_object(Bucket='gium', Key='books/id1', Body=book_ser)