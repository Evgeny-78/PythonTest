import random


class Integer:
    'Дескриптор для значений типа Integer'
    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if isinstance(value, int):
            instance.__dict__[self.name] = value
        else:
            raise ValueError(f'Ошибка значения. Значение {self.name} должно быть Int')

class ListClass(Integer):
    'Дескриптор для значений типа List'
    def __set__(self, instance, value):
        if isinstance(value, list) and not hasattr(instance, self.name):
            instance.__dict__[self.name] = value
        # elif isinstance(value, list) and hasattr(instance, self.name):
        #     raise Warning('Родословную нельзя изменить после назначения')
        elif not isinstance(value, list):
            raise ValueError(f'Ошибка значения. Значение {self.name} должно быть List')
        else:
            raise Warning('Родословную нельзя изменить после назначения')

class String(Integer):
    'Дескриптор для значений типа String'
    def __set__(self, instance, value):
        if isinstance(value, str):
            instance.__dict__[self.name] = value
        else:
            raise ValueError(f'Ошибка значения. Значение {self.name} должно быть Str')

class Float(Integer):
    'Дескриптор для значений типа Float'
    def __set__(self, instance, value):
        if isinstance(value, float):
            instance.__dict__[self.name] = value
        else:
            raise ValueError(f'Ошибка значения. Значение {self.name} должно быть Float')

class Animals:

    _listObj = []      # список объектов класса
    _number = 0
    _iter_index = 0
    age = Integer()
    weight = Float()
    name = String()
    height = Integer()
    sex = String()
    rod = ListClass()

    def __str__(self):
        return f'Животное по кличке: {self.name} - весом: {self.weight} кг - возрастом: {self.age} лет - высотой: {self.height} см'

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        cls._number += 1
        cls._listObj.append(self)
        return self

    def __init__(self, name: str, age: int, weight: float, height: int, sex: str, rod: list):
        self.age = age
        self.weight = weight
        self.name = name
        self.height = height
        self.sex = sex
        self.rod = rod

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)

    @classmethod
    def get_num(cls):
        # геттер параметра NUMBER
        return cls._number

    @classmethod
    def get_listObj(cls):
        # геттер списка объектов класса
        return cls._listObj

    def __iter__(self):
        # итератор объекта
        self.index_iter('iter')
        return self

    def __next__(self):
        # next итератора
        id = self.index_iter('now')
        if len(self._listObj) != id:
            self.index_iter('next')
            return self._listObj[id]
        else:
            raise StopIteration

    @classmethod
    def index_iter(cls, command):
        # изменение/получение индекса итератора как атрибута класса а не экземпляра
        match command:
            case 'iter':
                cls._iter_index = 0
            case 'next':
                cls._iter_index += 1
            case 'now':
                return cls._iter_index

class Cat(Animals):
    'Класс кошек'
    _listObj = []  # список объектов класса
    breed = String()
    def __str__(self):
        return f'Киса по кличке: {self.name} - весом: {self.weight} кг - возрастом: {self.age} лет - высотой: {self.height} см'

    def __init__(self, name: str, breed: str, age: int, weight: float, height: int, sex: str, rod: list):
        super().__init__(name, age, weight, height, sex, rod)
        self.breed = breed

    def action_mymy(self):
        print(f'Киса {self.name} говорит мяу мяу')

    def action_myrmyr(self):
        print(f'Киса {self.name} мурлыкает')

    def __add__(self, other):
        if isinstance(other, Cat):
            if self.sex != other.sex:
                rod = self.rod + other.rod + [self.name, other.name]
                breed = self.breed if self.sex == 'мужской' else other.breed
                name_cat = input('Введите имя котёнка: ')
                return Cat(name_cat, breed, 0, 0.5,
                       int((self.height + other.height) / 4), random.choice(['мужской', 'женский']), rod)
            else:
                raise ValueError('Пол котиков должен быть разным')
        elif isinstance(other, Corm):
            if other.weight > 0:
                self.weight += 0.1
                other.weight -= 0.1
            else:
                raise ValueError('Корм закончился')
        else:
            raise ArithmeticError("Правый операнд должен быть типом Cat или Corm")

    def __eq__(self, other):
        if (self.sex == other.sex and -2 <= self.weight - other.weight <= 2 and -5 <= self.height - other.height <= 5
                and -1 <= self.age - other.age <= 1 and -2 <= len(self.rod) - len(other.rod) <= 2 and isinstance(other, Cat)):
            return True
        else:
            return False



class Dog(Animals):
    'Класс собак'
    _listObj = []  # список объектов класса
    def __str__(self):
        return f'Собака по кличке: {self.name} - весом: {self.weight} кг - возрастом: {self.age} лет - высотой: {self.height} см'

    def action_gafgaf(self):
        print(f'Собака {self.name} говорит гаф гаф')

    def action_wooo(self):
        print(f'Собака {self.name} воет')

class Corm:
    type_corm = String()
    animal = String()
    weight = Float()
    def __str__(self):
        return f'{self.type_corm} корм {self.animal}, {self.weight} кг'

    def __init__(self, animal: str, type_corm: str, weight: float):
        self.animal = animal
        self.type_corm = type_corm
        self.weight = weight


