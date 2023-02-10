#Creo una chiave primaria in una tabella già esistente (costumer)

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

mycursor.execute("ALTER TABLE customer ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")b