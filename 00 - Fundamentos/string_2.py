nome = "Rafael"
idade = 33
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Rafael", "idade": 33}

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {0} Idade: {1}".format(nome, idade))
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
