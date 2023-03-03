import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

def insert_Mammifero():
 val=[]
 Nome_Proprio = input("Inserisci il nome dell'animale:")
 Razza =  input("Inserisci la razza dell'animale:")
 Peso = int( input("Inserisci il peso dell'animale:"))
 Eta = int( input("Inserisci l'età dell'animale:"))
 val.append((Nome_Proprio, Razza, Peso, Eta))
 sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
 mycursor.executemany(sql, val)
 mydb.commit()
 print(mycursor.rowcount, "mammifero inserito con successo!")


def show_Mammiferis():
  mycursor.execute("SELECT * FROM Mammiferi")
  for animal in mycursor:
    print(animal)

def delete_animal():
    id = input("Inserisci l'id del mammifero da eliminare: ")
    sql = "DELETE FROM Mammiferi WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "mammifero eliminato con successo!")

def update_animal():
    id = input("Inserisci l'id del mammifero da modificare: ")
    Nome_Proprio = input("Inserisci il nuovo nome del mammifero: ")
    Peso = int(input("Inserisci il nuovo peso del mammifero: "))
    sql = "UPDATE Mammiferi SET Nome_Proprio = %s, Peso = %s WHERE id = %s"
    val = (Nome_Proprio, Peso, id)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "mammifero modificato con successo!")

x = 0
while x!=5:
  print("Premi 1 per inserire un nuovo animale")
  print("Premi 2 per visualizzare tutti gli animali")
  print("Premi 3 per eliminare un animale")
  print("Premi 4 per modificare un animale")
  print("Premi 5 per uscire dal programma")

  x = int(input("INSERISCI LA TUA PREFERENZA: "))

  if x==1:
    insert_Mammifero()
  if x==2:
    show_Mammiferis()
  if x==3:
    delete_animal()
  if x==4:
    update_animal()
  if x==5:
    exit


