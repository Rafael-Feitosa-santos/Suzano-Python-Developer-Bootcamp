contato = {"nome": "Rafael", "telefone": "3333-2221"}

contato.setdefault("nome", "Rafael")  # "Rafael"
print(contato)  # {'nome': 'Rafael', 'telefone': '3333-2221'}

contato.setdefault("idade", 33)  # 33
print(contato)  # {'nome': 'Rafael', 'telefone': '3333-2221', 'idade': 28}
