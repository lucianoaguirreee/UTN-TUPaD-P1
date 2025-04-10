import math

# Calcular radio
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Tabla
def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Operaciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida (división por cero)"
    return (suma, resta, multiplicacion, division)

# Calculo IMC
def calcular_imc(peso, altura):
    if altura <= 0:
        return "La altura debe ser un número positivo mayor que cero."
    return peso / (altura ** 2)

# Temperatura
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Actividades
def actividad1():
    print("Hola Mundo!")

def actividad2(nombre):
    return f"Hola {nombre.title()}!"

def actividad3(nombre, apellido, edad, residencia):
    print(f"Soy {nombre.title()} {apellido.title()}, tengo {edad} años y vivo en {residencia.title()}.")

def actividad4(radio):
    if radio <= 0:
        print("El radio debe ser un número positivo.")
        return

    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)

    print(f"El área del círculo es: {area:.2f}")
    print(f"El perímetro del círculo es: {perimetro:.2f}")

def actividad5(segundos):
    horas = (segundos / 3600) 
    print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

def actividad6(numero):
    print(f"Tabla de multiplicar del {numero}:")
    tabla_multiplicar(numero)

def actividad7(a, b):
    resultados = operaciones_basicas(a, b)

    print(f"\nResultados de las operaciones entre {a} y {b}:")
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]}")

def actividad8(peso, altura):
    imc = calcular_imc(peso, altura)
    
    if isinstance(imc, str):
        print(imc)
    else:
        print(f"Tu IMC es: {imc:.2f}")

def actividad9(celsius):
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius:.2f}°C equivalen a {fahrenheit:.2f}°F")

def actividad10(x, y, z):
    print("Calcularemos el promedio de tres números.")    
    promedio = calcular_promedio(x, y, z)
    print(f"El promedio de los tres números es: {promedio:.2f}")

if __name__ == "__main__":
    print('')

    actividad1()
    print('')

    nombre = input("Ingresá tu nombre: ")
    saludo = actividad2(nombre)
    print(saludo)
    print('')

    apellido = input("Ingresá tu apellido: ")
    edad = input("Ingresá tu edad: ")
    residencia = input("¿Dónde vivís?: ")
    actividad3(nombre, apellido, edad, residencia)
    print('')

    radio = float(input("Ingresá el radio del círculo: "))
    actividad4(radio)
    print('')

    segundos = float(input("Ingresá la cantidad de segundos: "))
    actividad5(segundos)

    print('')
    numero = int(input("Ingresá un número para ver su tabla de multiplicar: "))
    actividad6(numero)

    print('')
    a = float(input("Ingresá el primer número: "))
    b = float(input("Ingresá el segundo número: "))
    actividad7(a, b)
    
    print('')
    peso = float(input("Ingresá tu peso en kilogramos: "))
    altura = float(input("Ingresá tu altura en metros: "))
    actividad8(peso, altura)

    print('')
    celsius = float(input("Ingresá la temperatura en grados Celsius: "))
    actividad9(celsius)
    
    print('')
    x = float(input("Ingresá el primer número: "))
    y = float(input("Ingresá el segundo número: "))
    z = float(input("Ingresá el tercer número: "))
    actividad10(x, y, z)