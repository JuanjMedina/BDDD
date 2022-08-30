
import sqlite3

MiConexion = sqlite3.connect("PrimeraBase")


MiCursor = MiConexion.cursor()
MiCursor.execute("INSERT INTO PRODUCTOS VALUES('Pan',3600,'media')")
MiConexion.commit()

print("hola mundo , esto es una pruba de si funciona GIt")



MiConexion.close()