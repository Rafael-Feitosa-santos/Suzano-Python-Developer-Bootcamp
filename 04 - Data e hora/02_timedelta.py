from datetime import date, datetime, timedelta

tipo_carro = "P"  # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual.strftime("%d/%m/%Y %H:%M:%S")} e ficará pronto às {data_estimada.strftime("%d/%m/%Y %H:%M:%S")}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual.strftime("%d/%m/%Y %H:%M:%S")} e ficará pronto às {data_estimada.strftime("%d/%m/%Y %H:%M:%S")}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual.strftime("%d/%m/%Y %H:%M:%S")} e ficará pronto às {data_estimada.strftime("%d/%m/%Y %H:%M:%S")}")


print(date.today() - timedelta(days=1))

resultado = datetime(2025, 5, 9, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())