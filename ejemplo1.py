
import sqlite3

MiConexion = sqlite3.connect("PrimeraBase")


MiCursor = MiConexion.cursor()
MiCursor.execute("INSERT INTO PRODUCTOS VALUES('Arroz',2000,'media')")
productos=[
    ("Manzana", 600, "media"),
    ("Pera", 1200, "media"),
    ("Sandia", 900, "media"),
]
print ("esto es una prueba")
MiCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", productos)

MiConexion.commit()




print("se ejecuto")
MiConexion.close()