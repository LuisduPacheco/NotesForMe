'''
Problema: Encuentra el número máximo en una lista
Escribe una función que reciba una lista de números y devuelva el número más grande.
'''

def maximo_lista(valores: list[int]):
  temp: int = valores[0]
  for i in range(len(valores)):
    if temp < valores[i]:
      temp = valores[i]
  print(temp)

maximo_lista([4, 2, 5, 0])