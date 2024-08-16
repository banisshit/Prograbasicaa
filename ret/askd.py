#ejercicio 1|
 
x = int(input("Introduce un numero: "))
y = int(input("Introduce otro numero: "))
 
if x > y:
    print("El numero mayor es: ",x)
else:
    print("El numero mayor es: ",y)
    
print("--------------------------------")

#ejercicio 2
 
a = int(input("Introduce un numero: "))
b = int(input("Introduce otro numero: "))
c = int(input("Introduce otro numero: "))
 
def max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print("El numero maximo es: ",max(a,b,c))
print("--------------------------------")

#ejercicio 3
 
def longitud(elemento):
    contador = 0
    for _ in elemento:
        contador += 1
    return contador

j = int(input("Cuantos elementos tiene la lista: "))
lista = []
for i in range(j):
    lista.append(int(input("Introduce el numero")))
 
print("Tiene una longitud de",longitud(lista), "caracteres")
print("--------------------------------")

 #ejercicio 4

vocal=str(input("introduce una letra por favor: "))
 
if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
        print(True)
 
elif vocal == "A" or vocal == "E" or vocal == "I" or vocal == "O" or vocal == "U":
        print(True)
    
else:
        print(False)

print("--------------------------------")
#Ejercicio 5

# Definir la función longitud para obtener la longitud de una lista
def longitud(lista):
    return len(lista)

# Definir la función suma para sumar todos los elementos de una lista
def suma(lista):
    g = 0
    for num in lista:
        g += num
    return g

# Definir la función multi para multiplicar todos los elementos de una lista
def multi(lista):
    g = 1
    for num in lista:
        g *= num
    return g

# Leer el número de elementos
y = int(input("¿Cuántos elementos tiene la lista? "))
lista = []

# Leer los elementos de la lista
for _ in range(y):
    lista.append(int(input("Introduce el número: ")))

# Imprimir la longitud de la lista
print("Tiene una longitud de", longitud(lista), "elementos")

# Imprimir la suma de los elementos de la lista
print("La suma de los elementos es", suma(lista))

# Imprimir el producto de los elementos de la lista
print("El producto de los elementos es", multi(lista))
print("--------------------------------")

#Ejercicio 6

def inversa(cadena) :
   cadena_inversa = cadena[::-1]
   return cadena_inversa
 
frase = str(input("Ingrese la frase para voltear: "))
print(inversa(frase))
print("--------------------------------")
#Ejercicio 7

def es_palindromo(cadena):
    cadena_limpia = cadena.replace(" ", "").lower()
    cadena_invertida = cadena_limpia[::-1]
    return cadena_limpia == cadena_invertida

igualito = str(input("Ingresa palabra para confirmar si es palindromo: "))
print(es_palindromo(igualito))
print("--------------------------------")


#Ejercicio 8

def superposicion(lista1, lista2):
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True
    return False
print("introduzca la primera lista")
ll1 = int(input("Introduce la longitud de la primera lista: "))
llista1 = []
for md in range (ll1):
    llista1.append(int(input("Introduce el numero")))

print("Introduzca la segunda lista")
ll2 = int(input("Introduce la longitud de la segunda lista: "))
llista2 = []
for mmd in range (ll2):
    llista2.append(int(input("Introduce el numero: ")))

print(superposicion(llista1, llista2))

print("--------------------------------")

#Ejercicio 9 

def generar_n_caracteres(n, caracter):
    if len(caracter) != 1:
        raise ValueError("El segundo argumento debe ser un carácter único.")
    return caracter * n

char = str(input("introduce el caracter a repetir: "))
nv = int(input("Cuantas veces quieres que se repita? "))

print(generar_n_caracteres(nv, char))

print("--------------------------------")

#Ejercicio 10

def histograma(lista):
    for numero in lista:
        print('*' * numero)

print("Introduce una lista de numeros para imprimirlos en histograma: ")

ff = int(input("Introduce la longitud que deseas: "))
hist = []
for emede in range (ff):
    hist.append(int(input("Ingresa el numero: ")))

histograma(hist)