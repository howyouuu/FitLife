WATER_PER_KG = 30
IN_LITERS = 1000
line = '-' * 40
error = 'Ошибка! Вы ввели некорректное число. Попробуйте ещё раз.'
print('Привет! Я твой помощник, расскажи немного о себе.')
user_name = input('Как тебя зовут: ')
while True:
    try:
        user_age = int(input('Сколько тебе лет: '))
        break #ИИ подсказал куда лучше всего поставить break
    except ValueError:
        print(error)
while True:
    try:
        user_weight = float(input('Твой вес в кг(например, 65.5): '))
        break
    except ValueError:
        print(error)
while True:
    try:
        user_height = float(input('Твой рост в метрах(например, 1.75): '))
        break
    except ValueError:
        print(error)
bmi = user_weight / (user_height ** 2)  # расчёт индекса массы тела
# расчёт рекомендуемой нормы воды в день и перевод из мл в л
water_l = user_weight * WATER_PER_KG / IN_LITERS
print(line)
print(f'Отчет для пользователя: {user_name} ({user_age} лет)')
print(f'Твой Индекс Массы Тела: {round(bmi, 1)}')
print(f'Рекомендуемая норма воды: {round(water_l, 2)} л. в день')
print(line)
print('Расчет окончен. Будьте здоровы!')
