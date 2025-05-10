saldo = 1000
saque = 250
limite = 200
conta_especial = True

ex_1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

print(ex_1)

ex_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(ex_2)

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

ex_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente

print(ex_3)