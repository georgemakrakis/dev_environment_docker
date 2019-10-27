# File taken and modified from https://www.w3schools.com/python/python_mysql_select.asp
import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

mydb = mysql.connector.connect(
  host="db",
  user=os.getenv("MYSQL_USER"),
  passwd=os.getenv("MYSQL_PASSWORD"),
  database=os.getenv("MYSQL_DATABASE")
)

mycursor = mydb.cursor()

mycursor.execute("show databases;")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)