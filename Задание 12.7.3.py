# Выводим пустую строку
print("Вариант 1")

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money= float(input("Введите сумму, которую планируете положить под проценты :"))
deposit = [money * per_cent / 100 for per_cent in per_cent.values()]
print(f'Максимальная сумма, которую Вы можете заработать — {max(deposit)}')

# Выводим пустую строку
print("Вариант 2")

# Вводится сумма, которую человек планирует положить под проценты
money = float(input('Введите сумму вклада (рублей): '))

# Даны процентные ставки в банках
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

# Извлечение названий банков из словаря в список
banks = list(per_cent.keys())

# Извлечение процентных ставок из словаря в список
percents = list(per_cent.values())

# Создание списка сумм, которые можно заработать на вкладе в разных банках
deposit = list()
deposit.append(int(money / 100 * float(percents[0])))
deposit.append(int(money / 100 * float(percents[1])))
deposit.append(int(money / 100 * float(percents[2])))
deposit.append(int(money / 100 * float(percents[3])))
print(f'\nДоход по депозиту составит:\n{banks[0]} банк - {deposit[0]} рублей\n{banks[1]} банк - {deposit[1]} '
      f'рублей\n{banks[2]} банк - {deposit[2]} рублей\n{banks[3]} банк - {deposit[3]} рублей\n')

# Максимальная сумма, которую можно заработать
max_deposit = max(deposit)
print('Максимальная сумма, которую Вы можете заработать: {} рублей.'.format(max_deposit))

# Выводим пустую строку
print("Вариант 3")


money = int(input("Введите сумму вклада (рублей): "))

#Имеем словарь со значениями процентных ставок в банках
# Объявляем депозиты в список

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
#Составляем программу с помощью цикла для вычисления процентов
#Оборачиваем результат в целочисленные числа
#Добавляем полученный результат в список deposit

for value in per_cent.values():
   result = int(money / 100 * value)
   deposit.append(result)
print(deposit)

#Выявляем максимальную сумму которую можно вынести


max_deposit = max(deposit)
print('Максимальная сумма, которую Вы можете заработать: {} рублей.'.format(max_deposit))