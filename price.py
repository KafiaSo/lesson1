# Создайте функцию get_summ(one, two, delimiter='&'), которая принимает два параметра, приводит их к строке и отдает объединенными через разделитель delimiter
# Вызовите функцию, передав в нее два аргумента "Learn" и "python", положите результат в переменную и выведите ее значение на экран
# Сделайте так, чтобы результирующая строка выводилась заглавными буквами

def get_summ(one, two, delimiter = '&'):
    two = str(two).upper()
    return str(one) + str(delimiter) + two

a = 'Learn'
b = 'python'
otvet = get_summ(one=a, two=b, delimiter='&')
print(otvet)

# Создайте в редакторе файл price.py
# Создайте функцию format_price, которая принимает один аргумент price
# Приведите price к целому числу (тип int)
# Верните строку "Цена: ЧИСЛО руб."
# Вызовите функцию, передав на вход 56.24 и положите результат в переменную
# Выведите значение переменной с результатом на экран

def format_price(price):
    price = int(price)
    return 'Цена: {} руб.'.format(price)

enter_price = 56.24
enter_price = format_price(enter_price)
print(enter_price)
