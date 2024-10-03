def fibonacci(n: int):
  if n>200:
    return n
  return fibonacci(n+1)

print(fibonacci(2))