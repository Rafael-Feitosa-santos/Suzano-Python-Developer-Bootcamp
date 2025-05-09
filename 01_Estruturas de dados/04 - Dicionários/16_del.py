contatos = {
    "rafael@gmail.com": {"nome": "Rafael", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["rafael@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

# {'rafael@gmail.com': {'nome': 'Rafael'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}  # noqa
print(contatos)

for chave, valor in contatos.items():
    print(f"nome: {valor["nome"]} - telefone:{valor.get("telefone", " Não encontrado")}")
