# Funciones de recursividad

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def fibonacci(num):
    if num == 0:
        return 0
    else:
        return 1 if num == 1 else fibonacci(num - 1) + fibonacci(num - 2)

def calcular_potencia_recursiva(base, exponente):
    if exponente < 0:
        return "Error: El exponente debe ser un número entero positivo."
    elif exponente == 0:
        return 1
    else:
        return base * calcular_potencia_recursiva(base, exponente - 1)

def decimal_a_binario_recursivo(numero_decimal):
    if numero_decimal < 0:
        return "Error: El número debe ser un entero positivo."
    elif numero_decimal == 0:
        return "0"
    elif numero_decimal == 1:
        return "1"
    else:
        parte_izquierda = decimal_a_binario_recursivo(numero_decimal // 2)
        parte_derecha = str(numero_decimal % 2)
        return parte_izquierda + parte_derecha

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

def suma_digitos(n):
    if not isinstance(n, int):
        return "Error: La entrada debe ser un número entero."
    if n < 0:
        return "Error: La entrada debe ser un número entero positivo."
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

def contar_bloques(n):
    if not isinstance(n, int):
        return "Error: El número de bloques debe ser un entero."
    if n <= 0:
        return "Error: El número de bloques en el nivel más bajo debe ser un entero positivo."
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

def contar_digito(numero, digito):
    if not isinstance(numero, int) or not isinstance(digito, int):
        return "Error: Ambos argumentos deben ser números enteros."
    if numero < 0:
        return "Error: El número debe ser un entero positivo."
    if not (0 <= digito <= 9):
        return "Error: El dígito a buscar debe estar entre 0 y 9."
    if numero == 0:
        return 0
    conteo_actual = 0
    ultimo_digito = numero % 10
    if ultimo_digito == digito:
        conteo_actual = 1
    return conteo_actual + contar_digito(numero // 10, digito)

def iterar_funcion(cant, funcion_a_iterar):
    for i in range(0, cant + 1):
        resultado = funcion_a_iterar(i)
        print(f"El {funcion_a_iterar.__name__} de {i} es: {resultado}")

# Actividades

def actividad1():
    """Factorial de números del 0 al N"""
    print("\n--- Actividad 1: Factorial ---")
    num_hasta_factorizar = int(input("Ingrese un numero entero: "))
    iterar_funcion(num_hasta_factorizar, factorial)

def actividad2():
    """Fibonacci de números del 0 al N"""
    print("\n--- Actividad 2: Fibonacci ---")
    num_hasta_fibonacci = int(input("Ingrese un numero entero: "))
    iterar_funcion(num_hasta_fibonacci, fibonacci)

def actividad3():
    """Calcular potencia de forma recursiva"""
    print("\n--- Actividad 3: Potencia Recursiva ---")
    base_usuario = float(input("Introduce la base (número real): "))
    exponente_usuario = int(input("Introduce el exponente (entero no negativo): "))
    resultado_potencia = calcular_potencia_recursiva(base_usuario, exponente_usuario)
    print(f"{base_usuario} elevado a la potencia de {exponente_usuario} es: {resultado_potencia}")

def actividad4():
    """Convertir decimal a binario de forma recursiva"""
    print("\n--- Actividad 4: Decimal a Binario ---")
    num_a_binario = int(input("Ingrese un numero entero: "))
    resultado = decimal_a_binario_recursivo(num_a_binario)
    print(f"El número {num_a_binario} en binario es: {resultado}")

def actividad5():
    """Verificar si una palabra es palíndromo"""
    print("\n--- Actividad 5: Palíndromo ---")
    palabra_usuario = input("Ingresa una palabra (sin espacios ni tildes): ").lower()
    resultado = es_palindromo(palabra_usuario)
    print(f"'{palabra_usuario}' es un palíndromo? {resultado}")

def actividad6():
    """Sumar dígitos de un número"""
    print("\n--- Actividad 6: Suma de Dígitos ---")
    num_sum_usuario = int(input("Ingresa un número entero positivo: "))
    resultado = suma_digitos(num_sum_usuario)
    print(f"La suma de los dígitos de {num_sum_usuario} es: {resultado}")

def actividad7():
    """Contar bloques en una pirámide"""
    print("\n--- Actividad 7: Contar Bloques ---")
    bloques_usuario = int(input("Ingresa el número de bloques en el nivel más bajo (entero positivo): "))
    resultado = contar_bloques(bloques_usuario)
    print(f"Para un nivel más bajo de {bloques_usuario} bloques, el total de bloques necesarios es: {resultado}")

def actividad8():
    """Contar ocurrencias de un dígito en un número"""
    print("\n--- Actividad 8: Contar Dígito ---")
    numero_usuario = int(input("Ingresa el número entero positivo: "))
    digito_usuario = int(input("Ingresa el dígito a buscar (0-9): "))
    resultado = contar_digito(numero_usuario, digito_usuario)
    print(f"El dígito {digito_usuario} aparece {resultado} vez(veces) en el número {numero_usuario}.")

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "="*50)
    print("         TRABAJO PRÁCTICO - RECURSIVIDAD")
    print("="*50)
    print("1. Factorial (0 al N)")
    print("2. Fibonacci (0 al N)")
    print("3. Potencia recursiva")
    print("4. Decimal a binario")
    print("5. Verificar palíndromo")
    print("6. Suma de dígitos")
    print("7. Contar bloques en pirámide")
    print("8. Contar dígito en número")
    print("0. Salir")
    print("="*50)

def ejecutar_actividad(numero_actividad):
    """Ejecuta la actividad seleccionada"""
    actividades = {
        1: actividad1,
        2: actividad2,
        3: actividad3,
        4: actividad4,
        5: actividad5,
        6: actividad6,
        7: actividad7,
        8: actividad8,
    }
    
    if numero_actividad == 0:
        print("¡Hasta luego!")
        return False
    elif numero_actividad in actividades:
        try:
            actividades[numero_actividad]()
            input("\nPresiona Enter para continuar...")
            return True
        except ValueError:
            print("Error: Por favor ingrese valores válidos.")
            input("\nPresiona Enter para continuar...")
            return True
        except Exception as e:
            print(f"Error inesperado: {e}")
            input("\nPresiona Enter para continuar...")
            return True
    else:
        print("Número de actividad inválido. Por favor seleccione una opción del 0 al 8.")
        input("\nPresiona Enter para continuar...")
        return True

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        try:
            actividad_a_ejecutar = int(input("Ingrese el número de la actividad que desea ejecutar (0-8): "))
            if not ejecutar_actividad(actividad_a_ejecutar):
                break
        except ValueError:
            print("Por favor ingrese un número entero.")
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()