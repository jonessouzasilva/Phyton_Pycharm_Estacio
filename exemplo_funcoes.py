""" Exercicio 1

def calculaDelta(coef1, coef2, coef3):
    #delta da eg 2° grau = b^2 - 4.a.c
    global delta
    delta = coef2*coef2 - 4*coef1*coef3

delta = 0

a = eval(input("Entre com o coeficiente a da equação: "))
b = eval(input("Entre com o coeficiente b da equação: "))
c = eval(input("Entre com o coeficiente c da equação: "))

calculaDelta(a, b, c)


print(f'O valor calculado do delta foi {delta}')

#delta > 0 : equação tem 2 raízes reais
#delta > 0 : equação tem 1 raíz real
#delta > 0 : equação não tem raíz real

if delta > 0:
    print("A equação tem 2 raízes reais.")
elif delta == 0:
    print("A equação tem 1 raíz real.")
else:
    print("A equação não tem raíz real.")

"""

def func1(x):
    x = 10
    print(x)


x = 0
print(x)
func1(x)
print(x)



