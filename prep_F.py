import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

x=int(input("Quanti animali vuoi inserire? "))

val=[]
for i in range (x):
    Nome_Proprio = input("Inserisci il nome dell'animale:")
    Razza =  input("Inserisci la razza dell'animale:")
    Peso = int( input("Inserisci il peso dell'animale:"))
    Eta = int( input("Inserisci l'età dell'animale:"))
    val.append((Nome_Proprio, Razza, Peso, Eta))

sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"

mycursor.executemany(sql, val)

mydb.commit()