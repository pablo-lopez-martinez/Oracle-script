import cx_Oracle

# Configurar los detalles de conexión
username = 'TEST1'        # Reemplaza con tu usuario de la base de datos
password = 'test1'     # Reemplaza con tu contraseña de la base de datos
dsn = 'CONSTRURED'                   # Este es el alias definido en tu archivo tnsnames.ora
cursor = None
connection = None

# Crear la conexión
try:
    # Establecer la conexión usando el alias del archivo tnsnames.ora
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    
    print("Conectado con éxito a la base de datos Oracle")

    # Crear un cursor para ejecutar consultas
    cursor = connection.cursor()

    # Ejecutar una consulta de ejemplo
    cursor.execute("SELECT * FROM nombre_de_tabla")

    # Imprimir los resultados
    for row in cursor:
        print(row)

except cx_Oracle.DatabaseError as e:
    print("Error al conectar a la base de datos: ", e)

finally:
    # Cerrar el cursor y la conexión
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        print("Conexión cerrada")
