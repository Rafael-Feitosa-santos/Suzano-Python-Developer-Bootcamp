from datetime import datetime, timedelta, timezone

data_oslo = datetime.now(timezone(timedelta(hours=2))).strftime("%d/%m/%Y %H:%M:%S")
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3))).strftime("%d/%m/%Y %H:%M:%S")

print(data_oslo)
print(data_sao_paulo)
