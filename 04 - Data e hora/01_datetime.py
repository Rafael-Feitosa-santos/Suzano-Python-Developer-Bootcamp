from datetime import date, datetime, time

data = date(2023, 7, 10)
print(data)
print(data.today())
print(date.today().strftime("%d/%m/%Y"))

data_hora = datetime(2023, 7, 10)
print(data_hora)
print(datetime.today())
print(datetime.today().strftime("%d/%m/%Y %H:%M:%S"))

hora = time(10, 20, 0)
print(hora)
