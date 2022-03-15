import math

num = float(input('Digite um número: '))
num = math.fabs(num)
raiz = math.sqrt(num)
raiz2 = num ** 0.5

print(f'A raíz de {num} é {raiz:.2f}')
print(f'A raíz de {num} é {raiz2:.2f}')