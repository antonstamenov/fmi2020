import mysql.connector

if __name__ == '__main__':

    mydb = mysql.connector.connect(
      host="db.cfqwfl51z1wh.us-east-1.rds.amazonaws.com",
      user="admin",
      passwd="1admin2admin",
      database="mydb"
    )
    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE authors ("
                        "id INT NOT NULL AUTO_INCREMENT, "
                        "author VARCHAR(255),"
                        "PRIMARY KEY (id))")
    mycursor.execute("CREATE TABLE books ("
                        "id INT NOT NULL AUTO_INCREMENT, "
                        "title VARCHAR(255), "
                        "category VARCHAR(255), "
                        "hardcover VARCHAR(255), "
                        "paperback VARCHAR(255),"
                        "author_id int,"
                        "primary key (id),"
                        "FOREIGN KEY (author_id) REFERENCES authors(id))"
                     )
