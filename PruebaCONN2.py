import pyodbc

server = 'localhost'
database = 'PRUEBA'

conecction_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

try:
    if not server or not database:
        raise ValueError("El nombre de la base de datos o del server esta vacio")
    
    conn = pyodbc.connect(conecction_string)
    print("Se establecio la conexion con BD")

    # #CREATE
    # try:
    #     cursor_Create = conn.cursor()
    #     consulta = "Insert into RECURSOS (nombre,apellidos,DNI,telefono,sexo) values (?,?,?,?,?)"
    #     cursor_Create.execute(consulta,'Jesus','Pacheco C','47589632','958774112','Masculino')
    #     print("Se registro correctamente a la persona")
    #     cursor_Create.commit()
    #     cursor_Create.close()
    # except Exception as e:
    #     print("No se pudo registrar a la persona solicitada", e)

    #READ
    # try:
    #     cursor_Read = conn.cursor()
    #     cursor_Read.execute("Select * from RECURSOS")
    #     consulta = cursor_Read.fetchall()
    #     for i in consulta:
    #         print(i)
    #         consulta = cursor_Read.fetchall()
    #     cursor_Read.commit()
    #     cursor_Read.close()
    # except Exception as e:
    #     print("No se pudo realizar el listado", e)

    # UPDATE
    # try:
    #     cursor_Update = conn.cursor()
    #     consulta = "Update RECURSOS set telefono=? where id=?"
    #     cursor_Update.execute(consulta,'988888888',10)
    #     print("Se actualizaron los datos de la persona solicitada")
    #     cursor_Update.commit()
    #     cursor_Update.close()
    # except Exception as e:
    #     print("No se pudo actualizar los datos de la persona por el error, ", e)

    # DELETE
    try:
        cursor_Delete = conn.cursor()
        consulta = "Delete from RECURSOS where id=?"
        cursor_Delete.execute(consulta,14)
        print("Se eliminaron los datos de la persona solicitada")
        cursor_Delete.commit()
        cursor_Delete.close()
    except Exception as e:
        print("No se pudo eliminar los datos de la persona solicitada")

    conn.close()

except Exception as e:
    print("No se pudo conectar con la base de datos por error: ",e)