import mysql.connector
import json

if __name__ == '__main__':

    mydb = mysql.connector.connect(
      host="db.cfqwfl51z1wh.us-east-1.rds.amazonaws.com",
      user="admin",
      passwd="1admin2admin",
      database="mydb",
    )
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("select authors.author, books.title, books.category, books.hardcover, books.paperback from authors, books "
                             "where books.author_id=authors.id "
                             "  and authors.author='Ivan Vazov' "
                             "  and books.title='Pod igoto'")


    for r in cursor:
        print(json.dumps(r, indent=4))

    cursor.close()