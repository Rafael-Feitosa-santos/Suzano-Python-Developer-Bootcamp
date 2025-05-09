contatos = {"rafael@gmail.com": {"nome": "Rafael", "telefone": "3333-2221"}}

contatos.update({"rafael@gmail.com": {"nome": "Rafa"}})
print(contatos)  # {'rafael@gmail.com': {'nome': 'Rafar'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'rafael@gmail.com': {'nome': 'Rafa'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)
