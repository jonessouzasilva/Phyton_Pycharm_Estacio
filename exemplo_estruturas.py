""" exercicio 1

for numero in range(1,11,1):
    if numero%2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é ímpar')

"""

""" exercicio 2

soma_pares = 0
cont_pares = 0

for numero in range(1,11,1):
    if numero%2 == 0:
        soma_pares = soma_pares + numero
        cont_pares += 1
    else:
        continue

print(f'A soma acumulada foi {soma_pares} e a quantidade de pares foi {cont_pares}')
print(f'A média dos números pares foi {soma_pares/cont_pares}')

"""

s = 0
a = 1
while s < 5:
    s = 3*a
    a += 1
    print(s)






