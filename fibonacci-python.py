num = int(input("Digite o valor de n: "))
fib0 = 0
fib1 = 1
print(fib0)

while (num > 0):
  temp = fib0
  fib0 = fib1
  fib1 = fib1 + temp
  num = num -1
  print(fib0)