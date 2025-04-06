import random

def actividad1():
    for i in range(101):
        print(i)

def actividad2():
    while True:
        numero = input("Ingresá un número entero: ")
        
        # Validamos que sea un entero (positivo o negativo)
        if numero.lstrip('-').isdigit():
            numero_sin_signo = numero.lstrip('-')
            cantidad_digitos = len(numero_sin_signo)
            print(f"El número tiene {cantidad_digitos} dígito(s).")
            break
        else:
            print("Eso no es un número entero válido. Intentá de nuevo.")

def actividad3():
    while True:
        try:
            a = int(input("Ingresá el primer número entero: "))
            b = int(input("Ingresá el segundo número entero: "))
            break
        except ValueError:
            print("Por favor, ingresá solo números enteros.")

    # Asegurarse de que a sea el menor y b el mayor
    if a > b:
        a, b = b, a

    numeros_a_sumar = list(range(a + 1, b))
    print(f"Números sumados: {numeros_a_sumar}") #

    suma = 0
    for i in range(a + 1, b):
        suma += i

    print(f"La suma de los números enteros entre {a} y {b} es: {suma}")

def actividad4():
    total = 0

    while True:
        try:
            numero = int(input("Ingresá un número entero (0 para terminar): "))
            if numero == 0:
                break
            total += numero
        except ValueError:
            print("Por favor, ingresá un número entero válido.")

    print(f"La suma total de los números ingresados es: {total}")
    
def actividad5():
    numero_secreto = random.randint(0, 9)
    intentos = 0

    print("¡Adiviná el número secreto entre 0 y 9!")

    while True:
        try:
            intento = int(input("Tu intento: "))
            intentos += 1

            if intento == numero_secreto:
                if intentos == 1:
                    print("¡Increíble! ¡Lo adivinaste en el primer intento!")
                else:
                    print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
                break
            else:
                print("Incorrecto, intentá de nuevo.")
        except ValueError:
            print("Por favor, ingresá un número entero entre 0 y 9.")

def actividad6():
    print("Números pares entre 0 y 100 en orden decreciente:")
    for i in range(100, -1, -1):
        if i % 2 == 0:
            print(i)

def actividad7():
    while True:
        try:
            limite = int(input("Ingresá un número entero positivo: "))
            if limite < 0:
                print("Debe ser un número positivo. Intentá de nuevo.")
            else:
                break
        except ValueError:
            print("Eso no es un número entero válido. Intentá de nuevo.")

    # numeros = list(range(limite + 1))
    # print(numeros)

    suma = 0
    for i in range(limite + 1):
        suma += i

    print(f"La suma de los números entre 0 y {limite} es: {suma}")

def actividad8():
    while True:
        try:
            cantidad_numeros = int(input("¿Cuántos números querés ingresar?: "))
            if cantidad_numeros <= 0:
                print("Por favor ingresá un número entero positivo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Ingresá un número entero.")

    pares = 0
    impares = 0
    positivos = 0
    negativos = 0

    print(f"\nIngresá {cantidad_numeros} números enteros:")

    for i in range(1, cantidad_numeros + 1):
        while True:
            try:
                numero = int(input(f"Número {i}: "))
                break
            except ValueError:
                print("Entrada inválida. Por favor ingresá un número entero.")

        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1

    print("\n📊 Resultados:")
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
    print(f"Números positivos: {positivos}")
    print(f"Números negativos: {negativos}")

def actividad9():
    while True:
        try:
            cantidad_numeros = int(input("¿Cuántos números querés ingresar?: "))
            if cantidad_numeros <= 0:
                print("Por favor, ingresá un número positivo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Ingresá un número entero.")

    suma_total = 0

    print(f"\nIngresá {cantidad_numeros} números enteros")

    for i in range(1, cantidad_numeros + 1):
        while True:
            try:
                numero = int(input(f"Número {i}: "))
                break
            except ValueError:
                print("Por favor ingresá un número entero válido.")
        
        suma_total += numero

    media = suma_total / cantidad_numeros

    print(f"\nLa media de los {cantidad_numeros} números ingresados es: {media}")

def actividad10():
    while True:
        numero = input("Ingresá un número entero: ")
        
        if numero.lstrip('-').isdigit():
            break
        else:
            print("Eso no es un número entero válido. Intentá de nuevo.")

    if numero.startswith('-'):
        numero_invertido = '-' + numero[:0:-1]
    else:
        numero_invertido = numero[::-1]

    print(f"Número invertido: {numero_invertido}")

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