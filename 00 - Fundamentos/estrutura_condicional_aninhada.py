conta_normal = True
conta_universitaria = False

saldo = 2000
cheque_especial = 450

try:
    if not conta_normal and not conta_universitaria:
        print("O sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")
    else:
        saque = float(input("Insira o valor do saque: "))

    if conta_normal:
        if saldo >= saque:
            saldo -= saque
            print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
            print(f"Saldo disponível: R$ {saldo:.2f}")

        elif saque <= (saldo + cheque_especial):
            uso_cheque_especial = saque - saldo
            cheque_especial_restante = cheque_especial - uso_cheque_especial
            print(f"Saque de R$ {saque:.2f} realizado com uso do cheque especial.")
            print(f"Valor utilizado do cheque especial: R$ {uso_cheque_especial:.2f}")
            print(f"Cheque especial restante: R$ {cheque_especial_restante:.2f}")

        else:
            print("Saque não efetuado.")

    elif conta_universitaria:
        if saldo >= saque:
            print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
    else:
        print("Saldo insuficiente.")
except KeyboardInterrupt:
    print("\nPrograma encerrado pelo usuário")
