# def saludar():
#     pass

# def saludar():
#     print("Hola mundo")

# saludar()

# def saludar_amigo(nombre, apellido):
#     print("Hola estimado " + nombre + " " + apellido)

# saludar_amigo("Jhon", "De La Cruz")

# def operacion(a,b):
#     resultado = a + b
#     return resultado

# print(operacion(5,4))

# def operacion(a,b=4):
#     resultado = a * b
#     return resultado

# print(operacion(5))

# Creacion de modulos

# import modulo_test

# print(modulo_test.OperacionM(4))

# POO - CLASE Y ATRIBUTOS
# class Persona:
    
#     # Constructor 
#     def __init__(self, nombre, apellido, DNI, telefono, sexo):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.DNI = DNI
#         self.telefono = telefono
#         self.sexo = sexo

#     def saludar(self):
#         saludo = "Hola, mi nombre es: " + self.nombre + " " + self.apellido
#         return saludo

#     def datos(self):
#         datos = "Mi numero de telefono es: " + self.telefono + ", mi numero de DNI es: " + self.DNI + " y mi sexo es: " + self.sexo
#         return datos
    

# # Herencia
# class Planilla(Persona):
#     salario = 15000
#     moneda = "Soles"

#     def miSalario(self):
#         mensaje = "Mi salario mensual es de " + str(self.salario) + " y esta en " + self.moneda
#         return mensaje

# p1 = Planilla("Kevin", "De La Cruz", "72406805", "947838193", "Masculino")
# print(p1.saludar())

# p2 = Persona("Kevin", "De La Cruz", "72406805", "947838193", "Masculino")
# print(p2.datos())

# p3 = Planilla("Kevin", "De La Cruz", "72406805", "947838193", "Masculino")
# print(p3.miSalario())

# Manejo de errores y el exception abarca todos los erroes
# try:
#     print(10/"c")
# except Exception as x:
#     print("Error en el sistema de tipo" , x)
# except TypeError as e:
#     print("El nombre del error es: ", e)
# finally:
#     print("LLegaste al final del try")
    
# Conexion a base de datos
# import pyodbc

# # Parametros de conexion
# server = 'localhost'
# database = 'PRUEBA'

# # Conectar usuario con windows authentication
# connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database}; Trusted_Connection=yes;'

# # connection_string = "Server=localhost,1433;Database=RECURSOS;"

# try:
#     if not server or not database:
#         raise ValueError("El nombre del servidor o de la base de datos esta vacio.")
    
#     conn = pyodbc.connect(connection_string)
#     print("Conexion exitosa")

#     cursor = conn.cursor()

#     cursor.execute("SELECT GETDATE()")
#     row = cursor.fetchone()
#     print("La hora y fecha es: ", row[0])

#     conn.close()
# except Exception as e:
#     print("Error al conectar con la base de datos", e)

# # try:
# #     conn = pyodbc.connect(connection_string)
# #     print("Conexion exitosa")

# #     # Creando cursor para crear consultas
# #     cursor = conn.cursor()

# #     # Ejecutar una consulta de prueba
# #     cursor.execute("SELECT GETDATE()") #Obtiene la hora y fecha actual del servidor
# #     row = cursor.fetchone()
# #     print("Fecha y hora del servidor SQL", row[0])

# #     # Cerrar la conexion
# #     conn.close()
# # except Exception as e:
# #     print("Error al conectar con la Base de Datos", e)

# # import pyodbc

# # drivers = [x for x in pyodbc.drivers()]

# # print(drivers)
