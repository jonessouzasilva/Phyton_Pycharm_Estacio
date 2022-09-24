class Carro(object):
    def FaleComigo(self):
        print("Sou um carro")


class Fusca(Carro):
    def FaleComUmFusca(self):
        print("Sou um Fusca")


x = Carro()
y = Fusca()

x.FaleComigo()
y.FaleComigo()