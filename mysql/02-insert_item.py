import mysql.connector

if __name__ == '__main__':

    mydb = mysql.connector.connect(
      host="db.cfqwfl51z1wh.us-east-1.rds.amazonaws.com",
      user="admin",
      passwd="1admin2admin",
      database="mydb"
    )
    cursor = mydb.cursor()

    cursor.execute('INSERT INTO authors (author) values ("John Grisham")')
    cursor.execute(f'INSERT INTO books (author_id, title, category, hardcover, paperback) values ({cursor.lastrowid}, "The Rainmaker", "Suspense", "J4SUKVGU", "D7YF4FCX")')
    mydb.commit()
    cursor.close()