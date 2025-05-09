contatos = {
    "rafael@gmail.com": {"nome": "Rafael", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "extra": {"a": 1}},
}
email = "giovanna@gmail.com"
nome = contatos[email]["nome"]
telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(f"""Nome: {nome} 
telefone: {telefone}""")

extra = contatos["melaine@gmail.com"]["extra"]["a"]
print(extra)
