# ---------------------------- Вложенные тернарные условия ----------------------------
# value = input('Введите число: ')
# value = int(value)
# res = (('меньше 50') if value < 50 else ('больше 50 меньше 100')) if value < 100 else (
#     ('больше 100 меньше 150') if value < 150 else ('больше 150'))
# print(f'Значение value = {value} -> {res}')

# --------------------------- сравнение case --------------------------------------

# match res:
#     case 'меньше 50' | 'больше 50 меньше 100':
#         print(f'переменная value меньше 100')
#     case 'больше 100 меньше 150' | 'больше 150':
#         print(f'переменная value больше 100')
#     case _:
#         print('конец case')
#
# match value:
#     case 70 | 80 | 90:
#         print('value равно 70, 80 или 90')
#     case param:
#         print(f'value = param = {param}')

# value = ()
#
# match value:
#     case str() as param:
#         print(f'Данные - строка. Значение: {param}')
#     case bool() as param:
#         print(f'Данные - булево. Значение: {param}')
#     case int() as param:
#         print(f'Данные - число. Значение: {param}')
#     case param:
#         print(f'Данные - {type(value)}. Значение: {param}')

# --------------------------- обработка исключений try/except --------------------------------------

# try:
#     2/2
# except ZeroDivisionError as error:
#     print(f'Произошла ошибка выполнения кода, деление на 0. {error}')
# except ValueError:
#     print('Произошла ошибка выполнения кода, ошибка значения')
# except:
#     print('Произошла ошибка выполнения кода')
# else:
#     print('Ошибка не произошла, выполнение блока else')
# finally:
#     print('Выполнение блока finnaly')

# # --------------------------- итераторы --------------------------------------

# listA = {1: 2, 2: 434, 'wqaw': 'sdfsdf',3: 3.3,False: True}
# itA = iter(listA)
# print(itA)
# print(listA[next(itA)])
# print(listA[next(itA)])
# print(listA[next(itA)])
# print(listA[next(itA)])
# print(listA[next(itA)])


# --------------------------- Генераторы --------------------------------------

# num = range(1,6,2)
# print(list(num))
# for n in range(1,12,3):
#     print(n)
#
# num = range(5)
# print(list(num))
# print(tuple(num))
# print(set(num))

# listA = [2*n+3 for n in range(2,15,3)]                  # генератор списка
# setA = {2*n+3 for n in range(2,15,3)}                   # генератор множества
# dictA = {f'Key {n}':2*n+3 for n in range(2,15,3)}       # генератор словаря
# print(listA)
# print(setA)
# print(dictA)
#
# listA = [2*n+3 for n in range(2,35,3) if 1 == n%2]      # генератор списка с условием
# print(listA)
#
# listA = [2*n+3 if n%3 == 0 else 2*n-3 for n in range(2,35) if 1 == n%2] # генератор списка с условием и тернарным условием
# print(listA)
#
# listB =[]
# listA = [n*m for n in range(2,15,3) for m in range(2,15,4)]     # вложенный генератор списка
# print(listA)