import sqlite3

miconexion = sqlite3.connect("Proyecto")
Micursor= miconexion.cursor()
#Micursor.execute("CREATE TABLE NOTAS(NOTA INTEGER, MATERIA VARCHAR(29), PROFESOR VARCHAR(30), DESCRIPCION VARCHAR(100))")
#Micursor.execute("ALTER TABLE NOTAS DROP DESCRIPCION")
Micursor.execute("ALTER TABLE NOTAS ADD COLUMN DESCRIPCION TEXT")
miconexion.commit()

miconexion.close()