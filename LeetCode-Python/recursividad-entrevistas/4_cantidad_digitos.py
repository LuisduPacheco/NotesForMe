'''
Crea un método que obtenga la cantidad de dígitos de un número N. 
Se debe pasar como parámetro el número N
'''

def cantidad_digitos(n: int):
  if n < 1:
    return 0
  n = n / 10
  return 1 + cantidad_digitos(n)

print(cantidad_digitos(200))