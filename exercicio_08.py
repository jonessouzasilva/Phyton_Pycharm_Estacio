def multiplicador(numero):
    global a  # todas as referências á variável a são pra a global
    a = 2     # a global será alterado
    print(f"Dentro da função, a variável a vale: {a}")
    return a * numero


a = 3 # esta variável tem escopo global
b = multiplicador(5)
print(f"A variável b vale: {b}")
print(f"Fora da função, a variável a vale: {a}")