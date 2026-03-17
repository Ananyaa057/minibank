import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="minibank"
)

if conn.is_connected():
    print("✅ Connected to minibank database successfully!")