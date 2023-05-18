# Создайте словарь: {"city": "Москва", "temperature": "20"}
# Выведите на экран значение ключа city
# Уменьшите значение "temperature" на 5
# Выведите на экран весь словарь

product = {
    "city": "Москва", 
    "temperature": "20"
}
print(product["city"])
product["temeperature"] = 15
print(product)

# Проверьте, есть ли в словаре ключ country
# Выведите значение по-умолчанию "Россия" для ключа country
# Добавьте в словарь элемент date со значением "27.05.2019"
# Выведите на экран длину словаря

print(product.get("country", "Россия"))

dateyear = ['27/05/2019']
product["date"] = dateyear
print(len(product))
