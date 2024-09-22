#Ejercicio 1

def factorial(n):
    if n!=0:
        return n*factorial(n-1)
    else:
        return 1

n = int(input("Introduce un numero: "))
print(factorial(n))
print("---------------------------------------")

#Ejercicoi 2

def fibonacci(n):
    if n == 0:
      return 0
    if n == 1:
        return 1
    else:
        return fibonacci (n-1) + fibonacci(n-2) 

n=int(input("Introduce un numero: "))
print(fibonacci(n))
print("---------------------------------------")

#Ejercicio 3

def invertir_cadena(cadena):
    if len(cadena)==0:
        return cadena
    else:
        return invertir_cadena(cadena[1:])+cadena[0]
    
cadena=str(input("Ingrese una cadena de caracteres: "))
print(invertir_cadena(cadena))
print("---------------------------------------")

#Ejercicio 4

def potencia(base, exponente):
    if exponente==0:
        return 1
    else:
        base*potencia(base, exponente-1)
        return base*potencia(base, exponente-1)

base=int(input("Intriduce un valor al numero base: "))
exponente=int(input("Ingtroduce un valor para el exponente: "))
print(potencia(base, exponente))
print("---------------------------------------")

#Ejercicio 5

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)

n=int(input("Introduce el numero: "))
print(suma_digitos(n))
print("---------------------------------------")

#Ejercicio 6
def merge_sort(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

lista = [38, 27, 43, 3, 9, 82, 10]
merge_sort(lista)
print("Lista ordenada:", lista)
print("---------------------------------------")

#Ejercicio 7

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[len(lista) // 2]
        izquierda = [x for x in lista if x < pivote]
        centro = [x for x in lista if x == pivote]
        derecha = [x for x in lista if x > pivote]
        return quick_sort(izquierda) + centro + quick_sort(derecha)

lista = [38, 27, 43, 3, 9, 82, 10]
lista_ordenada = quick_sort(lista)
print("Lista ordenada:", lista_ordenada)
print("---------------------------------------")

#Ejercicio 8

def busqueda_binaria(lista, objetivo, inicio=0, fin=None):
    if fin is None:
        fin = len(lista) - 1

    if inicio > fin:
        return False

    medio = (inicio + fin) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] > objetivo:
        return busqueda_binaria(lista, objetivo, inicio, medio - 1)
    else:
        return busqueda_binaria(lista, objetivo, medio + 1, fin)

lista_ordenada = [3, 9, 10, 27, 38, 43, 82]
objetivo = 27
encontrado = busqueda_binaria(lista_ordenada, objetivo)
print(f"El elemento {objetivo} {'fue encontrado' if encontrado else 'no fue encontrado'} en la lista.")
print("---------------------------------------")

#Ejercicio 9

def dividir_matriz(matriz):
    n = len(matriz)
    mitad = n // 2
    A11 = matriz[:mitad, :mitad]
    A12 = matriz[:mitad, mitad:]
    A21 = matriz[mitad:, :mitad]
    A22 = matriz[mitad:, mitad:]
    return A11, A12, A21, A22

matriz=([[5,6], [7,2]])
print(dividir_matriz(matriz))
print("---------------------------------------")

#Ejercicio 10

def multiplicar_matrices(A, B):
    n = len(A)
    
    if n == 1:
        return A * B
    
    A11, A12, A21, A22 = dividir_matriz(A)
    B11, B12, B21, B22 = dividir_matriz(B)
    
    C11 = multiplicar_matrices(A11, B11) + multiplicar_matrices(A12, B21)
    C12 = multiplicar_matrices(A11, B12) + multiplicar_matrices(A12, B22)
    C21 = multiplicar_matrices(A21, B11) + multiplicar_matrices(A22, B21)
    C22 = multiplicar_matrices(A21, B12) + multiplicar_matrices(A22, B22)
    
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    return C

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = multiplicar_matrices(A, B)
print("Resultado de la multiplicación de matrices:")
print(C)



def dividir_matriz(matriz):
    n = len(matriz)
    mitad = n // 2
    A11 = matriz[:mitad, :mitad]
    A12 = matriz[:mitad, mitad:]
    A21 = matriz[mitad:, :mitad]
    A22 = matriz[mitad:, mitad:]
    return A11, A12, A21, A22

def multiplicar_matrices(A, B):
    n = len(A)
    
    if n == 1:
        return A * B
    
    A11, A12, A21, A22 = dividir_matriz(A)
    B11, B12, B21, B22 = dividir_matriz(B)
    
    C11 = multiplicar_matrices(A11, B11) + multiplicar_matrices(A12, B21)
    C12 = multiplicar_matrices(A11, B12) + multiplicar_matrices(A12, B22)
    C21 = multiplicar_matrices(A21, B11) + multiplicar_matrices(A22, B21)
    C22 = multiplicar_matrices(A21, B12) + multiplicar_matrices(A22, B22)
    
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    return C

def matriz_identidad(n):
    return np.eye(n)

def potencia_matriz(matriz, exponente):
    if exponente == 0:
        return matriz_identidad(len(matriz))
    elif exponente == 1:
        return matriz
    
    mitad = exponente // 2
    mitad_potencia = potencia_matriz(matriz, mitad)
    
    if exponente % 2 == 0:
        return multiplicar_matrices(mitad_potencia, mitad_potencia)
    else:
        return multiplicar_matrices(multiplicar_matrices(mitad_potencia, mitad_potencia), matriz)

A = np.array([[1, 2], [3, 4]])
exponente = 3
resultado = potencia_matriz(A, exponente)
print(f"Resultado de elevar la matriz a la potencia {exponente}:")
print(resultado)