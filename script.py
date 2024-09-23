import cx_Oracle
import requests
import argparse



class DB:
    username = 'TEST1'        # Reemplaza con tu usuario de la base de datos
    password = 'test1'     # Reemplaza con tu contraseña de la base de datos
    dsn = 'CONSTRURED'                   # Este es el alias definido en tu archivo tnsnames.ora
    url='https://resource.e-coordina.com/v5/caecalidade/control'
    parameter_table = "PARAMCONFIGURACION"
    main_table = "CONSTRURED"

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-obra', type=str)
    parser.add_argument('-cif', type=str)
    parser.add_argument('-fecha',type=str)
    return parser.parse_args()


def script():
    # Configurar los detalles de conexión
    cursor = None
    connection = None

    try:
        # Establecer la conexión usando el alias del archivo tnsnames.ora
        connection = cx_Oracle.connect(user=DB.username, password=DB.password, dsn=DB.dsn)
        print("Conectado con éxito a la base de datos Oracle")

        # Crear un cursor para ejecutar consultas
        cursor = connection.cursor()

        #Obtenemos usuario y contraseña
        cursor.execute(f"SELECT * FROM {DB.parameter_table}")
        for row in cursor:
            user = row[0]
            password = row[1]

        #Obtenemos los parametros de entrada
        args = get_args()
        parameters = {
            "usuario": user,
            "password": password, 
            "obra": args.obra,
            "cif": args.cif,
            "fecha": args.fecha
        }

        

        response = requests.post(DB.url, data=parameters)

        if response.status_code != "200":
            sql_query = f"INSERT INTO {DB.main_table} (ID, FECHA, STATUS_CODE,  MENSAJ)"
        

        response_json = response.json()

        if response_json["status"]=="OK":
            sql_query = f"INSERT INTO {DB.main_table} (ID, FECHA, STATUS_CODE,  MENSAJ)"
        else:
            sql_query = f"INSERT INTO {DB.main_table} (ID,)"
            

    except cx_Oracle.DatabaseError as e:
        print("Error al conectar a la base de datos: ", e)

    finally:
        # Cerrar el cursor y la conexión
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("Conexión cerrada")
    
if __name__=="__main__":
    script()