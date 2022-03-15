import math

num = float(input('Digite um número: '))
num = math.fabs(num)

print(f'{math.fabs(num)} - Valor absoluto')
print(f'{math.trunc(num)} - Somente a parte inteira')
num1 = math.trunc(num)
print(f'{math.sqrt(num)} - Raíz')
print(f'{math.factorial(num1)} - Factorial')