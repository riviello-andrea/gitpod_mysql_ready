#Mi collego a mysql e creo un nuovo database

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

#Faccio una lista di tutti i database per controllare se il mio esiste

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

#Mi connetto direttamente al mio database su mysql

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)