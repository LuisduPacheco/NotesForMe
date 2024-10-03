'''
Crea un método que imprima los dígitos desde 1 hasta N. 
Se debe pasar como parámetro el número N
'''

def imprimir_hasta_n(n: int):
  if n > 0:
    imprimir_hasta_n(n - 1)
    print(n)

imprimir_hasta_n(4)

  