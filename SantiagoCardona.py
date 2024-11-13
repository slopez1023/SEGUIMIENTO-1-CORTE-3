# ------------------------------------------------------------
# Taller de listas en Python
# Nombre: Santiago Cardona López
# Fecha de creación: 13/11/2024
# Descripción: Este archivo contiene ejercicios para practicar
# el manejo de listas en Python mediante operaciones de acceso,
# modificación, eliminación, y métodos integrados de listas.
# ------------------------------------------------------------

# Ejercicio 1
print("\n# Ejercicio 1: Crear lista de frutas favoritas y mostrarla")
frutas_favoritas = ["Mango", "Guanábana", "Lulo", "Maracuyá", "Guayaba"]
print("Lista de frutas favoritas:", frutas_favoritas)

# Ejercicio 2
print("\n# Ejercicio 2: Acceder al segundo y cuarto elemento de la lista de frutas")
print("Segundo elemento:", frutas_favoritas[1])
print("Cuarto elemento:", frutas_favoritas[3])

# Ejercicio 3
print("\n# Ejercicio 3: Crear lista de números y mostrar su longitud")
numeros = list(range(1, 11))
print("Longitud de la lista de números:", len(numeros))

# Ejercicio 4
print("\n# Ejercicio 4: Concatenar listas de frutas y números")
lista_concatenada = frutas_favoritas + numeros
print("Lista concatenada:", lista_concatenada)

# Ejercicio 5
print("\n# Ejercicio 5: Modificar el tercer elemento de la lista concatenada")
lista_concatenada[2] = 100
print("Lista después de modificar el tercer elemento:", lista_concatenada)

# Ejercicio 6
print("\n# Ejercicio 6: Borrar el último elemento de la lista concatenada")
lista_concatenada.pop()
print("Lista después de borrar el último elemento:", lista_concatenada)

# Ejercicio 7
print("\n# Ejercicio 7: Crear lista de números y multiplicar cada elemento por 5")
lista_numeros = [3, 7, 9]
multiplicados_por_cinco = [x * 5 for x in lista_numeros]
print("Lista después de multiplicar cada elemento por 5:", multiplicados_por_cinco)

# Ejercicio 8
print("\n# Ejercicio 8: Multiplicar elementos correspondientes de dos listas")
lista1 = [2, 4, 6, 8, 10]
lista2 = [1, 3, 5, 7, 9]
multiplicacion_elementos = [a * b for a, b in zip(lista1, lista2)]
print("Multiplicación de elementos correspondientes:", multiplicacion_elementos)

# Ejercicio 9
print("\n# Ejercicio 9: Acceder al segundo elemento de la segunda lista anidada")
listas_anidadas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Segundo elemento de la segunda lista:", listas_anidadas[1][1])

# Ejercicio 10
print("\n# Ejercicio 10: Crear sublista desde la lista de números")
sublista = numeros[2:7]
print("Sublista de la lista de números (índice 2 al 6):", sublista)

# Ejercicio 11
print("\n# Ejercicio 11: Agregar elemento al final de la lista de frutas")
frutas_favoritas.append("Uchuva")
print("Lista de frutas después de .append():", frutas_favoritas)

# Ejercicio 12
print("\n# Ejercicio 12: Insertar elemento en la posición 2 de la lista de números")
numeros.insert(2, 15)
print("Lista de números después de .insert() en la posición 2:", numeros)

# Ejercicio 13
print("\n# Ejercicio 13: Eliminar un elemento específico de la lista de números")
lista_numeros.remove(9)
print("Lista después de .remove(9):", lista_numeros)

# Ejercicio 14
print("\n# Ejercicio 14: Invertir el orden de la lista concatenada")
lista_concatenada.reverse()
print("Lista concatenada invertida:", lista_concatenada)

# Ejercicio 15
print("\n# Ejercicio 15: Ordenar la lista de números en orden ascendente")
lista_numeros.sort()
print("Lista después de .sort() en orden ascendente:", lista_numeros)

# Ejercicio 16
print("\n# Ejercicio 16: Eliminar y obtener el último elemento de la lista concatenada")
ultimo_elemento = lista_concatenada.pop()
print("Elemento eliminado con .pop():", ultimo_elemento)
print("Lista después de .pop():", lista_concatenada)

# Ejercicio 17
print("\n# Ejercicio 17: Contar cuántas veces aparece un elemento específico en la lista")
conteo = lista_numeros.count(7)
print("Cantidad de veces que aparece 7 en la lista:", conteo)

# Ejercicio 18
print("\n# Ejercicio 18: Obtener el índice de un elemento específico en la lista concatenada")
indice = lista_concatenada.index(100)
print("Índice del elemento 100 en la lista concatenada:", indice)

# Ejercicio 19
print("\n# Ejercicio 19: Eliminar todos los elementos de la lista de frutas")
frutas_favoritas.clear()
print("Lista de frutas después de .clear():", frutas_favoritas)

# Ejercicio 20
print("\n# Ejercicio 20: Agregar números del 1 al 10 a una lista vacía con bucle for")
lista_vacia = []
for i in range(1, 11):
    lista_vacia.append(i)
print("Lista con números del 1 al 10:", lista_vacia)

# Ejercicio 21
print("\n# Ejercicio 21: Crear lista y eliminar elementos impares con while")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(numeros):
    if numeros[i] % 2 != 0:
        numeros.pop(i)
    else:
        i += 1
print("Lista después de eliminar impares:", numeros)

# Ejercicio 22
print("\n# Ejercicio 22: Ordenar lista de materias favoritas alfabéticamente")
materias = ["Matemáticas", "Física", "Química", "Historia", "Biología"]
materias.sort()
print("Materias ordenadas:", materias)

# Ejercicio 23
print("\n# Ejercicio 23: Mostrar múltiplos de 3 en lista de números")
numeros = list(range(1, 16))
multiplos_de_tres = [num for num in numeros if num % 3 == 0]
print("Múltiplos de 3:", multiplos_de_tres)

# Ejercicio 24
print("\n# Ejercicio 24: Imprimir nombres de artistas en mayúsculas")
artistas = ["Beyoncé", "Drake", "Adele", "Shakira", "Rihanna", "Bad Bunny", "J Balvin", "Maluma", "Karol G", "Juanes"]
for artista in artistas:
    print(artista.upper())

# Ejercicio 25
print("\n# Ejercicio 25: Crear lista con números pares usando comprensión de listas")
numeros = list(range(1, 21))
pares = [num for num in numeros if num % 2 == 0]
print("Números pares:", pares)

# Ejercicio 26
print("\n# Ejercicio 26: Imprimir nombres de municipios en orden inverso")
municipios_arauca = ["Arauca", "Arauquita", "Cravo Norte", "Fortul", "Puerto Rondón", "Saravena", "Tame"]
for municipio in municipios_arauca:
    print(municipio[::-1])

# Ejercicio 27
print("\n# Ejercicio 27: Crear lista de cuadrados de los números del 1 al 12")
numeros = list(range(1, 13))
cuadrados = [num ** 2 for num in numeros]
print("Cuadrados de los números:", cuadrados)

# Ejercicio 28
print("\n# Ejercicio 28: Obtener índice del mes 'Junio'")
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
print("Índice de 'Junio':", meses.index("Junio"))

# Ejercicio 29
print("\n# Ejercicio 29: Eliminar una mascota de la lista")
mascotas = ["Firulais", "Bobby", "Luna", "Max", "Nala", "Simba"]
mascotas.remove("Luna")
print("Lista de mascotas:", mascotas)

# Ejercicio 30
print("\n# Ejercicio 30: Ordenar lista de números en orden descendente")
numeros = list(range(1, 21))
numeros.sort(reverse=True)
print("Lista en orden descendente:", numeros)

# Ejercicio 31
print("\n# Ejercicio 31: Agregar un libro al final de la lista de libros favoritos")
libros = ["1984", "Cien años de soledad", "El Quijote", "Orgullo y prejuicio"]
libros.append("Crimen y castigo")
print("Lista de libros:", libros)

# Ejercicio 32
print("\n# Ejercicio 32: Crear lista de números impares usando comprensión de listas")
numeros = list(range(1, 16))
impares = [num for num in numeros if num % 2 != 0]
print("Números impares:", impares)

# Ejercicio 33
print("\n# Ejercicio 33: Insertar comida en posición específica")
comidas = ["Arepa", "Bandeja Paisa", "Sancocho", "Ajiaco", "Tamales", "Empanadas", "Patacones"]
comidas.insert(3, "Cazuela")
print("Lista de comidas:", comidas)

# Ejercicio 34
print("\n# Ejercicio 34: Extender lista de números con otra lista")
numeros = list(range(1, 11))
numeros.extend(range(11, 16))
print("Lista extendida:", numeros)

# Ejercicio 35
print("\n# Ejercicio 35: Contar ocurrencias de un nombre en lista de compañeros")
companeros = ["Juan", "Pedro", "María", "Juan", "Ana", "Juan"]
print("Cantidad de veces que 'Juan' aparece:", companeros.count("Juan"))

# Ejercicio 36
print("\n# Ejercicio 36: Crear lista de números divisibles por 3 usando comprensión de listas")
numeros = list(range(1, 13))
divisibles_por_tres = [num for num in numeros if num % 3 == 0]
print("Números divisibles por 3:", divisibles_por_tres)

# Ejercicio 37
print("\n# Ejercicio 37: Invertir orden de lista de artistas favoritos")
artistas = ["Shakira", "Juanes", "Maluma", "Karol G", "J Balvin"]
artistas.reverse()
print("Lista de artistas invertida:", artistas)

# Ejercicio 38
print("\n# Ejercicio 38: Ordenar lista de números en orden descendente con lambda")
numeros = list(range(1, 21))
numeros.sort(key=lambda x: -x)
print("Lista en orden descendente:", numeros)

# Ejercicio 39
print("\n# Ejercicio 39: Eliminar último elemento de lista de materias universitarias con pop()")
materias_uni = ["Álgebra", "Cálculo", "Programación", "Física", "Historia"]
ultimo = materias_uni.pop()
print("Última materia eliminada:", ultimo)
print("Lista de materias:", materias_uni)

# Ejercicio 40
print("\n# Ejercicio 40: Crear lista de múltiplos de 5 usando comprensión de listas")
numeros = list(range(1, 26))
multiplos_de_cinco = [num for num in numeros if num % 5 == 0]
print("Múltiplos de 5:", multiplos_de_cinco)

# Ejercicio 41
print("\n# Ejercicio 41: Ordenar lista de deportes alfabéticamente usando lambda")
deportes = ["Fútbol", "Baloncesto", "Natación", "Ciclismo", "Atletismo", "Voleibol", "Tennis", "Rugby"]
deportes.sort(key=lambda x: x)
print("Lista de deportes:", deportes)

# Ejercicio 42
print("\n# Ejercicio 42: Limpiar lista de números con clear()")
numeros = list(range(1, 16))
numeros.clear()
print("Lista después de clear:", numeros)

# Ejercicio 43
print("\n# Ejercicio 43: Imprimir nombres de países en minúsculas")
paises = ["Colombia", "Argentina", "Brasil", "Chile", "Ecuador", "Perú"]
for pais in paises:
    print(pais.lower())

# Ejercicio 44
print("\n# Ejercicio 44: Crear lista de cuadrados de números pares usando comprensión de listas")
numeros = list(range(1, 21))
cuadrados_pares = [num ** 2 for num in numeros if num % 2 == 0]
print("Cuadrados de números pares:", cuadrados_pares)

# Ejercicio 45
print("\n# Ejercicio 45: Obtener índice de un videojuego específico")
videojuegos = ["Mario", "Zelda", "Tetris", "Metroid", "Halo", "Minecraft", "Fortnite", "Pacman", "Pokemon", "Overwatch"]
print("Índice de 'Minecraft':", videojuegos.index("Minecraft"))

# Ejercicio 46
print("\n# Ejercicio 46: Eliminar número específico de la lista")
numeros = list(range(1, 13))
numeros.remove(7)
print("Lista después de remove(7):", numeros)

# Ejercicio 47
print("\n# Ejercicio 47: Ordenar lista de monumentos colombianos por longitud de nombre")
monumentos = ["La Candelaria", "El Peñol", "Ciudad Perdida", "San Agustín", "Parque Tayrona", "Catedral de Sal", "Monserrate"]
monumentos.sort(key=lambda x: len(x))
print("Monumentos ordenados por longitud:", monumentos)

# Ejercicio 48
print("\n# Ejercicio 48: Crear lista de múltiplos de 3 y 5 usando comprensión de listas")
numeros = list(range(1, 19))
multiplos_de_tres_y_cinco = [num for num in numeros if num % 3 == 0 and num % 5 == 0]
print("Múltiplos de 3 y 5:", multiplos_de_tres_y_cinco)

# Ejercicio 49
print("\n# Ejercicio 49: Agregar asignatura al final de la lista de asignaturas interesantes")
asignaturas_interesantes = ["Matemáticas", "Física", "Química", "Historia", "Biología", "Programación"]
asignaturas_interesantes.append("Estadística")
print("Lista de asignaturas:", asignaturas_interesantes)

# Ejercicio 50
print("\n# Ejercicio 50: Eliminar y obtener elemento en posición 7 de la lista de números")
numeros = list(range(1, 26))
elemento_pos_7 = numeros.pop(7)
print("Elemento eliminado en posición 7:", elemento_pos_7)
print("Lista después de pop(7):", numeros)
