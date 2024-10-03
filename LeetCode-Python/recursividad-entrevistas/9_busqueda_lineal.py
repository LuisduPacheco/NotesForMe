'''
Problema: Búsqueda lineal
Escribe una función que busque un número en una lista y devuelva su índice, o -1 si no está presente.
'''

def busqueda_lineal(valores: list[int], objetivo: int) -> int:
  for i in range(len(valores)):
    if valores[i] == objetivo:
      return i
  return -1

print(busqueda_lineal([4,5,67,0], 0))