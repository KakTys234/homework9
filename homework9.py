# Задание № 1 Функция с параметрами по умолчанию
# Создание функции, которая принимает три параметра со значениями по умолчанию
print('Задание № 1')
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# Вызоваем функцию print_params с разным количеством аргументов, включая вызов без аргументов

print_params()

print_params(a = 'folse')

print_params(b = 34)

print_params(c = [1, True, 'Yes'])

print_params(a = 0, c = 55)

print_params(a = 'Yes', b = 12345)

print_params(b = 100500, c = [25, 'Hello, world!', {'a': 45}])

print('-------------------------------------------')


# Проверяем работу  вызова print_params(b = 25) и print_params(c = [1,2,3])

print_params(b = 25)

print_params(c = [1,2,3])

print('-------------------------------------------')

# Задание № 2 Распаковка параметров
print('Задание № 2')
def print_params(a, b, c):
    print(a, b, c)

values_list = [5, 'Hello, world!', True]
values_dict = {'a': 1, 'b': 2, 'c': 3}
values_list_2 = [22, 'Yes']
print_params(*values_list)
print_params(**values_dict)

print('-------------------------------------------')

# Задание № 3 Распаковка + отдельные параметры
# Проверяем, работает ли print_params(*values_list_2, 42)
print('Задание № 3')

print_params(*values_list_2, 42)

print('-------------------------------------------')