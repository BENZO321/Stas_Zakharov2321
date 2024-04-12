deposit =[]
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму: "))
deposit.append(per_cent['ТКБ'] * money / 5600)
deposit.append(per_cent['СКБ'] * money / 5900)
deposit.append(per_cent['ВТБ'] * money / 4280)
deposit.append(per_cent['СБЕР'] * money / 4000)
print(deposit)
print("Максиммальная сумма, которую вы можете заработать:"),max(deposit)


