class Conta:
    def __init__(self, nro_agencia):
        self._saldo = 0
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # Quando tiver "_" no começo significa que ele é privado(Encapsulado)
        self._saldo += valor
        print(f"Depósito de R$: {valor:.2f} realizado com sucesso!")

    def sacar(self, valor):
        # Quando tiver "_" no começo significa que ele é privado(Encapsulado)
        self._saldo -= valor
        print(f"Saque de R$: {valor:.2f} realizado com sucesso!")

    def mostrar_saldo(self):
        # Quando tiver "_" no começo significa que ele é privado(Encapsulado)
        return f"Saldo disponível: R$ {self._saldo:.2f}"


conta = Conta("0001")
print(conta.nro_agencia)
conta.depositar(100)
conta.sacar(80)
print(conta.mostrar_saldo())
