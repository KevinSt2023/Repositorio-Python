#CREAR UN CRUD BASICO CON SQL SERVER Y PYTHON

#Importar libreria pyodbc
import pyodbc

#Crear variables de conexion
server = 'localhost'
database = 'PRUEBA'

#Crear la cadena de conexion
conecction_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

#Conectar y verificar conexion
try:
    if not server or not database:
        raise ValueError("El nombre de la base de datos o del servidor se encuentran vacios")

    #Creando conexion
    conn = pyodbc.connect(conecction_string)
    print("Conexion establecida correctamente")

    #LISTADO DE PERSONAS DE LA BD
    # try:
    #     cursor_Listado = conn.cursor()
    #     cursor_Listado.execute("SELECT * FROM RECURSOS")
    #     personas = cursor_Listado.fetchall()
    #     for i in personas:
    #         print(i)
    #         personas = cursor_Listado.fetchall()
    #     cursor_Listado.commit()
    #     cursor_Listado.close()
    # except Exception as e:
    #     print("No se pudo listar la lista de personas por error: ", e)


    #INGRESAR DATOS DE UNA PERSONA
    # try:
    #     cursor_Agregar = conn.cursor()
    #     consulta = "Insert into RECURSOS (nombre,apellidos,DNI,telefono,sexo) values (?,?,?,?,?)"
    #     cursor_Agregar.execute(consulta,'Diana','Rivera Souza','74855963','963225784','Femenino')
    #     print("Los datos fueron agregados correctamente")
    #     cursor_Agregar.commit()
    #     cursor_Agregar.close()
    # except Exception as e:
    #     print("No se pudo insertar los datos de la persona", e)


    #ACTUALIZAR LOS DATOS DE UNA PERSONA
    # try:
    #     cursor_Update = conn.cursor()
    #     consulta = "Update RECURSOS set nombre=? where id=?"
    #     cursor_Update.execute(consulta,'Stef',4)
    #     print("Se actualizaron los datos de la persona correctamente")
    #     cursor_Update.commit()
    #     cursor_Update.close()
    # except Exception as a:
    #     print("No se pudo actualizar los datos de la persona solicitada",a)


    #ELIMINAR LOS DATOS DE UNA PERSONA
    try:
        cursor_Delete = conn.cursor()
        consulta = "Delete from RECURSOS where id=?"
        cursor_Delete.execute(consulta,13)
        print("Se eliminaron los datos de la persona solicitada")
        cursor_Delete.commit()
        cursor_Delete.close()
    except Exception as o:
        print("No se pudo eliminar los datos de la persona solicitada", o)



    conn.close()

except Exception as e:
    print("No se pudo establecer la conexion a la base de datos por error,", e)