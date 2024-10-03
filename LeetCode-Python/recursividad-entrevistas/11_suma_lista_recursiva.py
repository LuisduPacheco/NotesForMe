'''
Problema: Sumar una lista de números utilizando recursión
Escribe una función recursiva que sume todos los números en una lista.
'''

def suma_recursiva(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_recursiva(lista[1:])

# Prueba
print(suma_recursiva([1, 2, 3, 4, 5]))  # 15
