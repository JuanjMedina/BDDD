
import sqlite3

MiConexion = sqlite3.connect("PrimeraBase")


MiCursor = MiConexion.cursor()
MiCursor.execute("INSERT INTO PRODUCTOS VALUES('Pan',3600,'media')")
#productos=[
    #("Manzana", 600, "media"),
    #("Pera", 1200, "media"),
   # ("Sandia", 900, "media"),
#]
#MiCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", productos)

MiConexion.commit()





MiConexion.close()