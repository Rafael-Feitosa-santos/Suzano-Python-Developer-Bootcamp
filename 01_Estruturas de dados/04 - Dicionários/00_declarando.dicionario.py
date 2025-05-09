pessoa = {"nome": "Rafael", "idade": 33}
print(pessoa)

pessoa["Naturalidade"] = "São Paulo"
print(pessoa)

pessoa = dict(nome="Rafael", idade=33)
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Rafael", "idade": 33, "telefone": "3333-1234"}
print(pessoa)
