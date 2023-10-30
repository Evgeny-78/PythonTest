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
            raise ValueError('Ошибка значения. Значение должно быть Int')

class String(Integer):
    'Дескриптор для значений типа String'
    def __set__(self, instance, value):
        if isinstance(value, str):
            instance.__dict__[self.name] = value
        else:
            raise ValueError('Ошибка значения. Значение должно быть Str')

class Animals:

    _listObj = []      # список объектов класса
    _number = 0
    age = Integer()
    weight = Integer()
    name = String()
    height = Integer()
    _iter_index = 0

    def __str__(self):
        return f'Животное по кличке: {self.name} - весом: {self.weight} кг - возрастом: {self.age} лет - высотой: {self.height} см'

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        cls._number += 1
        cls._listObj.append(self)
        return self

    def __init__(self, name: str, age: int, weight: int, height: int):
        self.age = age
        self.weight = weight
        self.name = name
        self.height = height

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

    def __init__(self, name: str, breed: str, age: int, weight: int, height: int):
        super().__init__(name, age, weight, height)
        self.breed = breed

    def action_mymy(self):
        print(f'Киса {self.name} говорит мяу мяу')

    def action_myrmyr(self):
        print(f'Киса {self.name} мурлыкает')


class Dog(Animals):
    'Класс собак'
    _listObj = []  # список объектов класса
    def __str__(self):
        return f'Собака по кличке: {self.name} - весом: {self.weight} кг - возрастом: {self.age} лет - высотой: {self.height} см'

    def action_gafgaf(self):
        print(f'Собака {self.name} говорит гаф гаф')

    def action_wooo(self):
        print(f'Собака {self.name} воет')
