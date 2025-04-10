
# 📘 Documentación del Código

Este documento explica las clases, funciones y actividades definidas en el código.

---

## 🍌 Diccionario de precios de frutas

```python
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}
```

Se define un diccionario con los precios de diferentes frutas.

---

## 👤 Clase `Persona`

```python
class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")
```

Representa a una persona con nombre, país y edad. Incluye un método `saludar` que imprime una presentación amigable.

---

## 🔵 Clase `Circulo`

```python
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * self.radio ** 2
        return area

    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro
```

Permite calcular el área y perímetro de un círculo a partir de su radio, usando constantes matemáticas de `math`.

---

## 🏦 Clase `Banco`

```python
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
```

Simula una fila de clientes en un banco utilizando una cola (`deque`).

---

## 🔗 Clase `Nodo` y `ListaEnlazada`

```python
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
```

Estructura de datos tipo lista enlazada. Permite insertar elementos, recorrer la lista e invertirla.

---

## 🔠 Actividades

### 🥭 `actividad1()`
Agrega frutas al diccionario original y muestra el nuevo contenido.

### 🍎 `actividad2()`
Modifica algunos precios del diccionario y los muestra actualizados.

### 🍇 `actividad3()`
Imprime una lista con solo los nombres de las frutas, sin sus precios.

### 👋 `actividad4()`
Crea una persona y muestra su saludo.

### 🔵 `actividad5()`
Crea un círculo, calcula su área y perímetro.

### 🧮 `actividad6(cadena)`
Verifica si los paréntesis, corchetes y llaves están balanceados en una cadena. Usa una pila y validaciones de tipo.

### 🏦 `actividad7()`
Simula el funcionamiento de una fila de banco.

### 🔗 `actividad8()`
Crea y recorre una lista enlazada con tres nodos.

### 🔁 `actividad9()`
Crea, recorre e invierte una lista enlazada.
