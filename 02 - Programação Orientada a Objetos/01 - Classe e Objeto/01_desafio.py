class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta..")
        print("Bicicleta parada!")

    def correr(self):
        print("Vruuummm...")

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("Vermelha", "Caloi", 2025, 525.00)
b1.buzinar()
b1.correr()
b1.parar()

print("=" * 30)

b2 = Bicicleta("Verde", "Monark", 2024, 259.00)
b2.buzinar()

print(b2)
