'''
Crea un método que obtenga la suma de los números naturales desde 1 hasta N. 
Se debe pasar como parámetro el número N
'''

def suma(n: int):
  # Caso Base
  if n == 1:
    return 1
  # Función recursiva
  return suma(n - 1) + n 

print(suma(3))