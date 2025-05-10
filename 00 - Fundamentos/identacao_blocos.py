saldo = 500


def sacar(valor):
    global saldo
    if saldo >= valor:
        saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
    else:
        print("Saque não realizado")


def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        print(f"Deposito de R$ {valor:.2f} realizado com sucesso")


def obter_saldo():
    print(f"Saldo atual: R$ {saldo:.2f}")


sacar(100)
obter_saldo()
depositar(1350)
obter_saldo()
