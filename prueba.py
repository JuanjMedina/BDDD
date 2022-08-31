import sqlite3

mimain = sqlite3.connect("PrimeraBase")
micursor = mimain.cursor()

micursor.execute("INSERT INTO PRODUCTOS VALUES('Almuerzo',3600,'media')")

mimain.commit()

mimain.close()