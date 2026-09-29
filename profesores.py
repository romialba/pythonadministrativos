import mysql.connector
import os
#conexion = mysql.connect ()
#cursor = conexion.cursor()
conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "FESARAGON",
    database = "escuela"
)
cursor = conexion.cursor()

cursor.execute(
    """
    create table if not exists profesores (
    id integer primary key auto_increment,
    nombre varchar (100) not null,
        apellido varchar (100),
        rfc bigint,
        especialidad varchar (100),
        correo varchar (100),
        telefono bigint,
        materia varchar (100),
        horainicio time,
        horafinal time,
        perfil longblob
    )
    """
)
archivo_imagenes = ["profesor1.jpeg", "profesor2.jpeg", "profesor3.jpeg", "profesor4.jpeg" ]
imagenes = []
for archivo in archivo_imagenes:
    with open(archivo, "rb") as f:
        imagenes.append (f.read())
        print (f"se leyeron {len (imagenes)} imagenes insertadas")
        sql = "insert into profesores(nombre, apellido, rfc, especialidad, correo, telefono, materia, horainicio, horafinal, perfil) values (%s, %s, %s, %s,%s, %s, %s, %s, %s, %s)"
personas = [
    ("Jorge", "Valencia", "8503151", "robotica", "jorge.valencia@escuela.com", 5689120347, "vision por computadora", "8:00", "13:20", imagenes[0]),
    ("Karla", "Negrete", "9007212", "ingenieria en sistemas", "karla.negrete@escuela.com", 5643925078, "reconocimiento de patrones", "7:00", "13:20", imagenes[1]),
    ("Edgar", "Irala", "7804083", "sistemas computacionales", "edgar.irala@escuela.com",5687126459, "uso de herramientas de explotacion de datos", "7:00", "12:20", imagenes[2]), 
    ("Estela", "Paz", "9201124", "fisico matematico", "estela.paz@escuela.com", 5620134967, "temas selectos de matematicas", "10:00", "13:20",imagenes[3])
]

cursor.executemany (sql, personas)
conexion.commit()
print(f"{cursor.rowcount} profesores insertados")

cursor.execute("select id, nombre, perfil from profesores")
resultados = cursor.fetchall()


for id, nombre, imagen in resultados: 
    if imagen:
        nombre_archivo = f"profesores{id}.jpeg" 
    with open(archivo, "wb") as f:
        f.write (imagen)
    print (f"imagen de {nombre} guardada como {nombre_archivo}")
else:
     print (f" {nombre} no tiene imagen")

cursor.execute ("describe profesores")
print ("\n tablas profesores")
for column in cursor.fetchall(): 
    print (column)
    cursor.close()

    conexion.close()