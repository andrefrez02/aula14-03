num = int(input(f'Digite um número de 3 digitos: '))

d1 = (num//100)
d2 = num%100//10
d3 = num%10
inverso = d3*100 + d2*10 + d1*1
print(f'O inverso de {num} é {inverso}')