print(" Verifica existencia de chave ".center(50, "="))

contatos = {"rafael@gmail.com": {"nome": "Rafael", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get("rafael@gmail.com", {})  # {"rafael@gmail.com": {"nome": "Rafael", "telefone": "3333-2221"}
print(resultado)

resultado = contatos["rafael@gmail.com"].get("idade","Não encontrado")
print(resultado)

print("=" * 50)
