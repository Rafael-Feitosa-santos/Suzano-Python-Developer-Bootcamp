contatos = {"rafael@gmail.com": {"nome": "Rafael", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('rafael@gmail.com', {'nome': 'Rafael', 'telefone': '3333-2221'})
print(resultado)

# contatos.popitem()  # KeyError
