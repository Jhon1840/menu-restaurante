import sqlite3

conexion = sqlite3.connect('estudiantes.db')

cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Estudiantes (
        ID INTEGER PRIMARY KEY,
        Nombre TEXT,
        Correo TEXT,
        Cursos TEXT,
        EstadoEconomico TEXT
    )
''')

cursor.execute('''
    INSERT INTO Estudiantes (ID, Nombre, Correo, Cursos, EstadoEconomico)
    VALUES (1, 'Juan Arce Vargas Suarez', 'vfj600392@gmail.com', 'Iot, Calculo1', 'No tiene deudas')
''')

cursor.execute('''
    INSERT INTO Estudiantes (ID, Nombre, Correo, Cursos, EstadoEconomico)
    VALUES (2, 'Neymar Junior Campeon do mundo', 'grt620492@gmail.com', 'Domir1, dominadas 3, joga Bonito 4', 'Debe 1400')
''')

conexion.commit()

conexion.close()
