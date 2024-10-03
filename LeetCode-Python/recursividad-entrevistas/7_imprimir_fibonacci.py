'''
Problema: Imprimir los primeros N números de la serie de Fibonacci
Escribe una función que imprima los primeros N números de la serie de Fibonacci.

0 1 1 2 3 5 8 
'''

def numeros_fibonacci(n):
  a: int = 0
  b: int = 1
  temp: int = 0

  for _ in range(n):
    print(a, end= " ")
    temp = a
    a = b
    b = temp + b

numeros_fibonacci(10)
  