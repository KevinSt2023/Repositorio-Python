import random

def adivina_el_numero_computadora(x):
    print("*************************")
    print("  ¡Bienvenido al Juego!")
    print("*************************")
    print(f"Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo: ")

    limite_inferior = 1
    limite_superior = x

    respuesta_usuario = ""

    while respuesta_usuario != "c":
        #Genera una prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior,limite_superior)
        else:
            prediccion = limite_inferior #Podria ser el limite superior
        #Obtener una respuesta del usuario
        respuesta_usuario = input(f"Mi prediccion es: {prediccion}. Si es muy alta ingresa (A), si es muy baja ingresa (B), y si es correcta ingresa (C): ").lower()

        if respuesta_usuario == "a":
            limite_superior = prediccion - 1
        elif respuesta_usuario == "b":
            limite_inferior = prediccion + 1

        print(f"Siiiiiiiiiiii La computadora adivino tu numero correctamente: {prediccion}")

adivina_el_numero_computadora(10)

