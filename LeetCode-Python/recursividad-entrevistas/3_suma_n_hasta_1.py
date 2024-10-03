'''
Crea un método que imprima los dígitos desde N hasta 1. 
Se debe pasar como parámetro el número N
'''

def imprimir_n_hasta_uno(n: int):
  print(n)
  if n > 1:
    imprimir_n_hasta_uno(n - 1)

imprimir_n_hasta_uno(4)