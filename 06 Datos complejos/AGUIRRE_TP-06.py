import math
from collections import deque

precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * self.radio ** 2
        return area

    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro

class Banco:
    def __init__(self):
        self.cola = deque()

    def agregar_cliente(self, nombre):
        self.cola.append(nombre)
        print(f"🟢 Cliente '{nombre}' fue agregado a la fila.")

    def atender_cliente(self):
        if self.cola:
            cliente = self.cola.popleft()
            print(f"🔵 Atendiendo al cliente: {cliente}")
        else:
            print("⚠️ No hay clientes en la fila.")

    def siguiente_cliente(self):
        if self.cola:
            print(f"🕓 El siguiente cliente es: {self.cola[0]}")
        else:
            print("⚠️ No hay clientes en espera.")

    def mostrar_fila(self):
        if self.cola:
            print("📋 Fila actual:", list(self.cola))
        else:
            print("📭 La fila está vacía.")

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def insertar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.head
        self.head = nuevo_nodo
        print(f"🟢 Insertado '{valor}' al inicio.")

    def recorrer(self):
        actual = self.head
        print("📋 Lista enlazada:")
        while actual:
            print(f"🔸 {actual.valor}")
            actual = actual.siguiente

    def invertir(self):
        anterior = None
        actual = self.head
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.head = anterior
        print("🔁 Lista invertida.")

def actividad1():
    print(precios_frutas)

    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300

    print(precios_frutas)
actividad1()

def actividad2():
    print(precios_frutas)

    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón'] = 2800

    print("Después de actualizar precios:")
    print(precios_frutas)
actividad2()

def actividad3():
    frutas = list(precios_frutas.keys())
    print("Lista de frutas sin precios:")
    print(frutas)
actividad3()

def actividad4():
    luciano = Persona("Luciano", "Argentina", 24)
    luciano.saludar()
actividad4()

def actividad5():
    circulo = Circulo(5)
    print("Área del círculo:", circulo.calcular_area())
    print("Perímetro del círculo:", circulo.calcular_perimetro())
actividad5()

def actividad6(cadena):
    print('')
    print('')
    pila = []
    pares = {')': '(', '}': '{', ']': '['}
    valids = '(){}[]'

    if not isinstance(cadena, str):
        print(f"❌ Parámetro no aceptado: '{cadena}' (tipo: {type(cadena).__name__}). Se esperaba un string.")
        return False

    if cadena[0] not in valids:
        return False

    if cadena and cadena[0] in ')}]':
        return False
    
    print(f"Cadena a evaluar: {cadena}")
    print(f"Pila inicial: {pila}\n")

    if cadena and cadena[0] in ')}]':
        return False
    
    for caracter in cadena:
        print(f"Caracter actual: '{caracter}'")

        if caracter in '({[':
            pila.append(caracter)
            print(f"✔️ Es apertura, se apila → Pila: {pila}")

        elif caracter in ')}]':
            if not pila:
                print(f"❌ Error: se encontró '{caracter}' pero la pila está vacía.")
                return False
            if pila[-1] != pares[caracter]:
                print(f"❌ Error: se intentó cerrar '{caracter}', pero el último abierto fue '{pila[-1]}'.")
                return False
            pila.pop()
            print(f"✔️ Se cerró correctamente '{caracter}', se desapila → Pila: {pila}")

        print("---")

    print("\nFin del recorrido.")

    if len(pila) == 0:
        print("✅ Todos los paréntesis están balanceados.")
        return True
    else:
        print(f"❌ Quedaron sin cerrar: {pila}")
        return False

actividad6("({[]})")
actividad6(")(")

def actividad7():
    print('')
    print('')
    print('BANCO\n')
    banco = Banco()
    banco.agregar_cliente("Luciano")
    banco.agregar_cliente("Denisse")
    banco.siguiente_cliente()
    banco.atender_cliente()
    banco.siguiente_cliente()
    banco.mostrar_fila()
    print('')
actividad7()

def actividad8(): 
    lista = ListaEnlazada()
    lista.insertar_al_inicio("Tercer nodo")
    lista.insertar_al_inicio("Segundo nodo")
    lista.insertar_al_inicio("Primer nodo")

    lista.recorrer()
actividad8()

def actividad9():
    lista = ListaEnlazada()
    lista.insertar_al_inicio(3)
    lista.insertar_al_inicio(2)
    lista.insertar_al_inicio(1)
    lista.recorrer()
    lista.invertir()
    lista.recorrer()
actividad9()