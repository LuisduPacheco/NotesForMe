'''
Problema: Ordenamiento por burbuja
Escribe una función que ordene una lista de números utilizando el algoritmo de ordenamiento por burbuja.
'''

def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                # Intercambio usando una variable temporal
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
    return lista

# Prueba
print(ordenamiento_burbuja([64, 34, 25, 12, 22, 11, 90]))  # [11, 12, 22, 25, 34, 64, 90]

