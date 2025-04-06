import math

def actividad1():
    print('Hola Mundo!')

def actividad2():
    nombre = input("Ingresa tu nombre: ")
    print(f"Hola {nombre}!")

def actividad3():
    def contiene_numeros(texto):
        return any(caracter.isdigit() for caracter in texto)

    while True:
        nombre = input("Ingresa tu nombre: ")
        if nombre.strip() and not contiene_numeros(nombre):
            break
        elif not nombre.strip():
            print("El nombre no puede estar vacío. Inténtalo de nuevo.")
        else:
            print("El nombre no puede contener números. Inténtalo de nuevo.")

    while True:
        apellido = input("Ingresa tu apellido: ")
        if apellido.strip() and not contiene_numeros(apellido):
            break
        elif not apellido.strip():
            print("El apellido no puede estar vacío. Inténtalo de nuevo.")
        else:
            print("El apellido no puede contener números. Inténtalo de nuevo.")

    while True:
        edad_str = input("Ingresa tu edad: ")
        if edad_str.isdigit():
            edad = int(edad_str)
            if edad > 0:
                break
            else:
                print("La edad debe ser un número positivo. Inténtalo de nuevo.")
        else:
            print("Por favor, ingresa una edad numérica válida.")

    while True:
        residencia = input("Ingresa tu lugar de residencia: ")
        if residencia.strip():
            break
        else:
            print("El lugar de residencia no puede estar vacío. Inténtalo de nuevo.")

    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

def actividad4():
    while True:
        try:
            radio = float(input("Ingresa el radio del círculo (debe ser un número positivo): "))
            if radio >= 0:
                break
            else:
                print("El radio debe ser un número positivo. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número válido.")

    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio

    print(f"El área del círculo es {area:.2f} y el perímetro del círculo es: {perimetro:.2f}")

def actividad5():
    while True:
        try:
            segundos = int(input("Ingresa una cantidad de segundos (debe ser un número entero no negativo): "))
            if segundos >= 0:
                break
            else:
                print("La cantidad de segundos debe ser un número entero no negativo. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero.")

    horas = segundos // 3600
    minutos = (segundos % 3600) // 60 
    segundos_restantes = segundos % 60

    print(f"{segundos} segundos equivalen a {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")

def actividad6():
    while True:
        try:
            numero = int(input("Ingresa un número entero para ver su tabla de multiplicar: "))
            break
        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero. Inténtalo de nuevo.")

    print(f"Tabla de multiplicar del {numero}:")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def actividad7():
    while True:
        try:
            a = int(input("Ingresa el primer número entero (distinto de 0): "))
            if a != 0:
                break
            else:
                print("El primer número no puede ser 0. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero. Inténtalo de nuevo.")

    while True:
        try:
            b = int(input("Ingresa el segundo número entero (distinto de 0): "))
            if b != 0:
                break
            else:
                print("El segundo número no puede ser 0. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero. Inténtalo de nuevo.")

    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b

    print(f"La suma de {a} y {b} es: {suma}")
    print(f"La resta de {a} y {b} es: {resta}")
    print(f"La multiplicación de {a} y {b} es: {multiplicacion}")
    print(f"La división de {a} y {b} es: {division}")

def actividad8():
    while True:
        try:
            peso = float(input("Ingresa tu peso en kilogramos (kg): "))
            if peso > 0: 
                break
            else:
                print("El peso debe ser un valor positivo. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número. Inténtalo de nuevo.")

    while True:
        try:
            altura = float(input("Ingresa tu altura en metros (m): "))
            if altura > 0:
                break
            else:
                print("La altura debe ser un valor positivo. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número. Inténtalo de nuevo.")

    imc = peso / (altura ** 2)
    print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

def actividad9():
    while True:
        try:
            celsius = float(input("Ingresa una temperatura en grados Celsius: "))
            break
        except ValueError:
            print("Entrada inválida. Debes ingresar un número. Inténtalo de nuevo.")

    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} grados Celsius equivalen a {fahrenheit:.2f} grados Fahrenheit.")

def actividad10():
    numeros = [] 

    for i in range(1, 4):
        while True:
            try:
                numero = float(input(f"Ingresa el número {i}: "))
                numeros.append(numero)
                break 
            except ValueError:
                print("Entrada inválida. Debes ingresar un número. Inténtalo de nuevo.")

    promedio = sum(numeros) / len(numeros)
    print(f"El promedio de los tres números es: {promedio:.2f}")

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
        10: actividad10
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