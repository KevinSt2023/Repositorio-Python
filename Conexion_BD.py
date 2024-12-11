import pyodbc

#Variables de conexion
server = 'localhost'
database = 'PRUEBA'

#Crear conexion string
conecction_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database}; Trusted_Connection=yes;'

#Manejo de errores
try:
    if not server or not database:
        raise ValueError("El nombre del servidor o de la base de datos esta vacia")
    
    #Generando la conexion
    conn = pyodbc.connect(conecction_string)
    print("Conexion exitosa sin novedad")

    #Creando el cursor
    # cursor = conn.cursor()
    # #Haciendo la consulta a la base de datos
    # # cursor.execute("SELECT GETDATE()")
    # # row = cursor.fetchone()
    # # print("La hora y fecha es: ", row[0])
    # cursor.execute("SELECT * FROM RECURSOS;")
    # # persona = cursor.fetchone()
    # # while persona:
    # #     print(persona)
    # #     persona = cursor.fetchone()
    # print("Recorrido de lista exitosa")
    # # personas = cursor.fetchall()
    # # for persona in personas:
    # #     print(persona)    
    # cursor.close()

    #Listando base de datos
    # cursor_Lista = conn.cursor()
    # cursor_Lista.execute("Select * from RECURSOS")
    # personas = cursor_Lista.fetchall()
    # for i in personas:
    #     print(i)    
    #     personas = cursor_Lista.fetchone



    #Insertando valores a la base de datos
    #Crear cursor para insertar
    # try:
    #     cursor_Insertar = conn.cursor()
    #     cursor_Insertar.execute("INSERT INTO RECURSOS (nombre,apellidos,DNI,telefono,sexo) VALUES ('Antolina','Escate Ruiz','15599455','957441236','Femenino');")
    #     print("Persona agregada correctamente")
    #     # cursor_Insertar.execute(consulta)
    #     cursor_Insertar.commit()#OBLIGATORIO
    #     cursor_Insertar.close()
    # except Exception as a:
    #     print("No se pudo agregar a la persona", a)
    # try:
    #     cursor_Insertar = conn.cursor()
    #     consulta = "Insert into RECURSOS (nombre,apellidos,DNI,telefono,sexo) values (?,?,?,?,?)"
    #     cursor_Insertar.execute(consulta,'Sergio','Valdiviezo','15447887','958774223','Masculino')
    #     print("Se agrego correctamente al usuario")
    #     cursor_Insertar.commit()
    #     cursor_Insertar.close()
    # except Exception as e:
    #     print("No se pudo agregar a la persona", e)



    #Actualizando informacion en la base de datos
    # try:
    #     # Creando cursos obligatorio
    #     cursor_Actualizar = conn.cursor()
    #     consulta = "Update RECURSOS set apellidos=? where nombre=?"
    #     cursor_Actualizar.execute(consulta,'De La Cruz Morales','David')
    #     print("Se actualizo la informacion requerida")
    #     cursor_Actualizar.commit()
    #     cursor_Actualizar.close()
        
    # except Exception as i:
    #     print("No se pudo actualizar la informacion requerida", i)


    # Eliminando informacion de la base de datos
    # try:
    #     cursor_Eliminar = conn.cursor()
    #     consulta = "Delete from RECURSOS where id=?"
    #     cursor_Eliminar.execute(consulta,2)
    #     print("Usuario eliminado de la base de datos exitosamente")
    #     cursor_Eliminar.commit()
    #     cursor_Eliminar.close()
    # except Exception as a:
    #     print("No se pudo eliminar al usuario con el id solicitado, error: ", a)


    conn.close()

except Exception as e:
    print("No se pudo conectar al servidor por el error de tipo: ", e)

