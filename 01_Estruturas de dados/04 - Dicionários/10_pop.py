contatos = {"rafael@gmail.com": {"nome": "Rafael", "telefone": "3333-2221"}}

resultado = contatos.pop("rafael@gmail.com")  # {'nome': 'Rafael', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("rafael@gmail.com", {})  # {}
print(resultado)
