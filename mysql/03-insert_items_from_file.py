import mysql.connector
import json

if __name__ == '__main__':

    mydb = mysql.connector.connect(
      host="db.cfqwfl51z1wh.us-east-1.rds.amazonaws.com",
      user="admin",
      passwd="1admin2admin",
      database="mydb"
    )
    cursor = mydb.cursor()
    with open("books.json") as json_file:
        books = json.load(json_file)
        for book in books:
            cursor.execute(f'INSERT INTO authors (author) values ("{book["Author"]}")')
            cursor.execute(f'INSERT INTO books (author_id, title, category, hardcover, paperback) values ({cursor.lastrowid}, "{book["Title"]}", "{book["Category"]}", "{book["Formats"]["Hardcover"]}", "{book["Formats"]["Paperback"]}")')

    mydb.commit()
    cursor.close()