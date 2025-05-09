salario = 2751


def salario_bonus(bonus, lista):
    global salario
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux = {lista_aux}")
    salario += bonus
    return salario


lista = [1]
salario_com_bonus = salario_bonus(500, lista)
print(f"{salario_com_bonus:.2f}")
print(lista)
