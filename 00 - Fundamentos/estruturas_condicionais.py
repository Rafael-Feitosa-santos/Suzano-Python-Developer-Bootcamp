MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a cnh.")
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a cnh.")

print("===========================")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a cnh.")
else:
    print("Ainda não pode tirar a cnh.")

print("===========================")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a cnh.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a cnh.")

