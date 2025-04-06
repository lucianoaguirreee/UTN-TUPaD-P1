import random
from statistics import mode, median, mean

def actividad1():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            break
        except ValueError:
            print("Por favor ingrese un número válido.")

    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")

def actividad2():
    while True:
        try:
            nota = float(input("Ingrese su nota: "))
            break
        except ValueError:
            print("Por favor ingrese un número válido.")

    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")

def actividad3():
    while True:
        try:
            numero = int(input("Ingrese un número par: "))
            if numero % 2 == 0:
                print("Ha ingresado un número par.")
                break 
            else:
                print("Por favor, ingrese un número par.")
        except ValueError:
            print("Por favor ingrese un número válido.")

def actividad4():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            break
        except ValueError:
            print("Por favor ingrese un número válido.")

    if edad < 12:
        print("Niño/a")
    elif 12 <= edad < 18:
        print("Adolescente")
    elif 18 <= edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")

def actividad5():
    while True:
        contraseña = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")
        longitud = len(contraseña)

        if 8 <= longitud <= 14:
            print("Ha ingresado una contraseña correcta.")
            break
        else:
            print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

def actividad6():
    numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

    media = mean(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    moda = mode(numeros_aleatorios)

    print(f"Números aleatorios: {numeros_aleatorios}")

    # Media: promedio de los valores.
    print(f"Media: {media}")
    # Mediana: valor del medio al ordenar.
    print(f"Mediana: {mediana}")
    # Moda: valor que más se repite.
    print(f"Moda: {moda}")

    if media > mediana > moda:
        print("Sesgo positivo o a la derecha.")
    elif media < mediana < moda:
        print("Sesgo negativo o a la izquierda.")
    elif media == mediana == moda:
        print("No hay sesgo (distribución simétrica).")
    else:
        print("La distribución no cumple con las condiciones exactas de sesgo definidas.")

def actividad7():
    while True:
        texto = input("Ingrese una frase o palabra: ").strip()
        if texto != "":
            break
        else:
            print("El texto no puede estar vacío. Por favor, intente nuevamente.")

    if texto[-1].lower() in "aeiou":
        texto += "!"

    print("Resultado:", texto)

def actividad8():
    while True:
        nombre = input("Ingrese su nombre: ").strip()
        if nombre != "":
            break
        else:
            print("El nombre no puede estar vacío.")

    while True:
        try:
            opcion = int(input("Ingrese una opción (1: MAYÚSCULAS, 2: minúsculas, 3: Capitalizado): "))
            if opcion in [1, 2, 3]:
                break
            else:
                print("Por favor ingrese 1, 2 o 3.")
        except ValueError:
            print("Debe ingresar un número válido (1, 2 o 3).")

    if opcion == 1:
        print("Resultado:", nombre.upper())
    elif opcion == 2:
        print("Resultado:", nombre.lower())
    elif opcion == 3:
        print("Resultado:", nombre.title())

def actividad9():
    while True:
        try:
            magnitud = float(input("Ingrese la magnitud del terremoto: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    if magnitud < 3:
        print("Muy leve (imperceptible)")
    elif 3 <= magnitud < 4:
        print("Leve (ligeramente perceptible)")
    elif 4 <= magnitud < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños)")
    elif 5 <= magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles)")
    elif 6 <= magnitud < 7:
        print("Muy Fuerte (puede causar daños significativos)")
    else:
        print("Extremo (puede causar graves daños a gran escala)")

def actividad10():
    while True:
        hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
        if hemisferio in ['N', 'S']:
            break
        else:
            print("Por favor, ingrese 'N' para norte o 'S' para sur.")

    while True:
        try:
            mes = int(input("Ingrese el número del mes (1-12): "))
            if 1 <= mes <= 12:
                break
            else:
                print("El mes debe estar entre 1 y 12.")
        except ValueError:
            print("Ingrese un número válido para el mes.")

    while True:
        try:
            dia = int(input("Ingrese el día del mes (1-31): "))
            if 1 <= dia <= 31:
                break
            else:
                print("El día debe estar entre 1 y 31.")
        except ValueError:
            print("Ingrese un número válido para el día.")

    fecha = (mes, dia)

    if (fecha >= (12, 21)) or (fecha <= (3, 20)):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (fecha >= (3, 21)) and (fecha <= (6, 20)):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (fecha >= (6, 21)) and (fecha <= (9, 20)):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    elif (fecha >= (9, 21)) and (fecha <= (12, 20)):
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"

    if hemisferio == "N":
        print("Estás en la estación:", estacion_norte)
    else:
        print("Estás en la estación:", estacion_sur)

def ejecutar_actividad(numero_actividad):
    actividades = {
        1: actividad1,
        2: actividad2,
        3: actividad3,
        4: actividad4,
        5: actividad5,
        6: actividad6,
        7: actividad7,
        8: actividad8,
        9: actividad9,
        10: actividad10,
    }

    if numero_actividad in actividades:
        actividades[numero_actividad]()
        return True
    else:
        print("Número de actividad inválido.")
        return False
    
def main():
  while True:
    try:
        actividad_a_ejecutar = int(input("Ingrese el número de la actividad que desea ejecutar (1-10): "))
        if ejecutar_actividad(actividad_a_ejecutar):
          break
    except ValueError:
        print("Por favor ingrese un numero entero.")

if __name__ == "__main__":
    main()