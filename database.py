import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="document_db"
)
