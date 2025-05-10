### 1º forma
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(sorted(pares))

## 2º forma

pares = [numero for numero in numeros if numero % 2 == 0]
print(sorted(pares))

## Elevar os valores ao quadrado

quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)

quadrado = [numero ** 2 for numero in numeros]
print(quadrado)

######

nova = [i ** 2 if i > 6 else i for i in range(10) if i % 2 == 0]
print(nova)
