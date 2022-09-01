
import sqlite3

MiConexion = sqlite3.connect("PrimeraBase")


MiCursor = MiConexion.cursor()
#MiCursor.execute("INSERT INTO PRODUCTOS VALUES('Arroz',2000,'media')")

#productos=[
    # ("Manzana", 600, "media"),
    #("Pera", 1200, "media"),
    #("Sandia", 900, "media"),
#]


#MiCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", productos)
MiCursor.execute("SELECT * FROM PRODUCTOS")
miinfo= MiCursor.fetchall()
print(miinfo)


MiConexion.commit()




MiConexion.close()