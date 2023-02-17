import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
val = [
  ('Bob', 'Cane', '65', '18'),
  ('Ignazio', 'Ratto', '8', '11'),
  ('Geltrude', 'Rana', '30', '8'),
  ('Zaini', 'Umano', '90', '18'),
  ('Gianpiero', 'Panda', '200', '3'),
    ]

mycursor.executemany(sql, val)

mydb.commit()

