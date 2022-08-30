
import sqlite3

MiConexion = sqlite3.connect("PrimeraBase")


MiCursor = MiConexion.cursor()
MiCursor.execute("INSERT INTO PRODUCTOS VALUES('Pan',3600,'media')")
MiConexion.commit()





MiConexion.close()