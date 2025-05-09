contatos = {"rafael@gmail.com": {"nome": "Rafael", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["rafael@gmail.com"] = {"nome": "Rafa"}

print(contatos["rafael@gmail.com"])  # {"nome": "Rafael", "telefone": "3333-2221"}

print(copia["rafael@gmail.com"])  # {"nome": "Gui"}
