import mysql.connector;
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1307",
    database="food_ordering"
)
if db.is_connected():
    print("Mysql Connected Successfully!")

db.close()
