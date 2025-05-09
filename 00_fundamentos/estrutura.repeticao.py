print("========= Separa as vogais =========")

## Exemplo utilizando um interável
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

vogais_exibidas = set()

for letra in texto:
    letra_maisculas = letra.upper()
    if letra_maisculas in VOGAIS and letra_maisculas not in vogais_exibidas:
        print(letra_maisculas, end=" ")
    vogais_exibidas.add(letra_maisculas)

print("\n========= Sequência loop FOR =========")

## Função utilizando o built-in range
inicio = 1
fim = 51
passo = 5

for i in range(inicio, fim, passo):
    if i + passo >= fim:
        print(i)
    else:
        print(i, end=", ")

print("\n========= Sequência loop WHILE =========")

op = -1

while op != 0:
    try:
        op = int(input(" [1] Sacar \n [2] Extrato \n [0] Sair \n"))

        if op == 1:
            print("Sacando....")
        elif op == 2:
            print("Exibindo o extrato")
        elif op == 0:
            print("Saindo..")
        else:
            print("Opção inválida")

    except KeyboardInterrupt:
        print("\nSistema fechado pelo usuário")
        break
