# --------------------------------- работа со списками и кортежами ---------------------------

# spisok = []
# print(type(spisok))
# spisok.append('stroka')
# spisok.append(5)
# spisok.append(('korteg', 56, True))
# print(spisok)
# print(len(spisok))
# spisok.extend(['new list', 23423, False, None])
# print(spisok)
#
# korteg = tuple(spisok)
# print(korteg)
# korteg = 1, 4, 'asdas', 3.23, True
# print(korteg)

# ------------------------------- работа со словарями ----------------------------------------
# NewDict = {2: 'qwqw', 'one': 1, 'two': 'two', 'key1': 'value1'}
# print(NewDict)
# NewDict2 = dict.fromkeys(['key1', 'key2', 'key3'], ['value1', 'value2', 'value3'])
# print(NewDict2)
# print(NewDict.items())
# NewDict['key2'] = 'value2'
# print(NewDict)
# print('key2' in NewDict)

# ----------------------------------- работа с файлами ------------------------------------------

# import datetime
# try:
#     with open('text.txt', 'a+', encoding='utf-8') as file:
#         file.seek(0)
#         for f in file.readlines():
#             print(f)
#         file.write(f'\nНовая строка записана {datetime.datetime.now()}')
#         file.close()
#
# except BaseException:
#     print('Свершилось исключение')
# else:
#     print('try завершилось штатно')
# finally:
#     print('try завершилось')

# ---------------------------------- работа с функциями ------------------------------------------

def same_func(one:int, two:int, three:int=3, *args, **kwargs) -> int:
    sum = one + two + three
    for n in args:
        sum += n
    for k,v in kwargs.items():
        sum += v
    return sum

one = dict.fromkeys(['key1', 'key2', 'key3'], 2)
two = 8
print(same_func(1,2,4, 4, 5, 6, 7, 0, param1 = 4, param2 = 5))

def type_func(list_param:list, type_value) -> bool:
    # проверяет равны ли типы данных переменных в списке list_param заданному типу type_value
    # рекурсивная функция
    if len(list_param) != 1 and isinstance(list_param[0], type_value):
        return type_func(list_param[1:],type_value)
    return isinstance(list_param[0], type_value)

print(type_func(['5','5','7'], float))

func = lambda a,b,c: a+b+c    # лямбда функция
print(func(1,3,5))

def zamik_func(type_value):
    #функция замыкания
    def type_func(list_param: list) -> bool:
        # проверяет равны ли типы данных переменных в списке list_param заданному типу type_value
        # рекурсивная функция
        if len(list_param) != 1 and isinstance(list_param[0], type_value):
            return type_func(list_param[1:])
        return isinstance(list_param[0], type_value)

    return type_func

wtf_type_str = zamik_func(str)
wtf_type_int = zamik_func(int)

print(wtf_type_str(['asdasd','sdfsdfs','3']))
print(wtf_type_int([3,111,8]))

def decorator_func(func_decor):
    # декоратор, функция с одним аргументом
    def wrap(data: str):
        print('Обертка до функции')
        ram = func_decor(data)
        print('Обертка после функции')
        return ram

    return wrap

@decorator_func
def func_from_decor(data: str):
    print(f'Сама функция. data = {data}')

func_from_decor('Параметр')

def func_fr_decor2(data: int) -> int:
    print(f'введенное число: {data}')
    return data

func_fr_decor2 = decorator_func(func_fr_decor2)
print(func_fr_decor2('dasdasd'))

def df_decorator(dx=5):
    # замыкание для создания параметра декоратора
    def decorator_func(func_decor):
        # декоратор, функция с одним аргументом
        def wrap(data: int):
            print(f'Параметр замыкания {dx}')
            ram = func_decor(data*dx)
            print('Обертка после функции')
            return ram

        return wrap
    return decorator_func

@df_decorator(10)
def func_fr_decor2(data: int) -> int:
    print(f'введенное число: {data}')
    return data

print('-------------------------')
print(func_fr_decor2(10))

def func_fr_decor2(data: int) -> int:
    print(f'введенное число: {data}')
    return data

print('-------------------------')
f = df_decorator(5)
func_fr_decor2 = f(func_fr_decor2)
print(func_fr_decor2(5))