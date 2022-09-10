import sqlite3
miConexion = sqlite3.connect("Proyecto")
micursor= miConexion.cursor()
#UNIQUE no se repite informacion
#micursor.execute('''CREATE TABLE PRODUCTOS(ID INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE VARCHAR(20), PRECIO INTEGER(15))''')
micursor.execute("UPDATE PRODUCTOS SET PRECIO=45 WHERE NOMBRE ='Lentejas'")
#productos=[
 #   ("Lentejas",1000),
  #  ("Frijoles",5000),
   # ("Manzanas",2500)
#]
micursor.execute("SELECT * FROM PRODUCTOS ")
elementos = micursor.fetchall()
print(elementos)
#micursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?)",productos)
miConexion.commit()
miConexion.close()