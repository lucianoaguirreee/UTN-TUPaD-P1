def actividad1():
    multiplos_de_4 = list(range(4, 101, 4))
    print(multiplos_de_4)

def actividad2():
    consolas = ["PS1", "PS2", "PS3", "PS4", "PS5"]
    print(consolas[-2])

def actividad3():
    juegos = []
    juegos.append("Crash Bandicoot")
    juegos.append("Tekken 3")
    juegos.append("Gran Turismo 2")
    print(juegos)

def actividad4():
    animales = ["perro", "gato", "conejo", "pez"]
    print(animales)
    animales[1] = "loro"
    animales[-1] = "oso"
    print(animales)

def actividad5():
    # Crea una lista llamada numeros con los valores
    numeros = [8, 15, 3, 22, 7]

    # Busca el valor maximo en un array/lista de numeros
    maxNum = max(numeros) 

    # Elimina el valor
    numeros.remove(maxNum)

    # Muestro el array/lista modificado
    print(numeros)

def actividad6():
    numeros = list(range(10, 31, 5))
    print(numeros[:2])

def actividad7():
    autos = ["sedan", "polo", "suran", "gol"]
    autos[1:3] = ["golf", "vento"]
    print(autos)

def actividad8():
    valores = range(5, 16, 5)
    dobles = [x * 2 for x in valores]
    print(dobles)

def actividad9():
    # Lista inicial
    compras = [
        ["pan", "leche"], 
        ["arroz", "fideos", "salsa"], 
        ["agua"]
    ]

    print(compras)

    # a) Agregar "jugo" a la lista del tercer cliente usando append.
    compras[2].append("jugo")

    # b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
    compras[1][1] = "tallarines"

    # c) Eliminar "pan" de la lista del primer cliente.
    compras[0].remove("pan")

    # d) Imprimir la lista resultante por pantalla
    print(compras)

def actividad10():
    lista_anidada = [
        15,
        True,
        [25.5, 57.9, 30.6],
        False
    ]
    print(lista_anidada)


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