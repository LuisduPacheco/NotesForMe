'''
Crea un método que obtenga el factorial de un número N. 
Se debe pasar como parámetro el número N
'''

def factorial(n: int):
  if n == 1 :
    return 1
  return n * factorial(n - 1)

print(factorial(3))