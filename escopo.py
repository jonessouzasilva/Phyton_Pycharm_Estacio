def funcao1():
    global a
    a = 20
    print("Dentro da funcao1:")
    print(a)


a = 10
funcao1()

print("Dentro do corpo principal:")
print(a)
