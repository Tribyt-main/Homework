class User:
    __instance = None

    def __new__(cls, *args, **kwargs):  # Упаковывает все user_main, user_main2, 3 ,4 .... в одно место в памяти
        print('i in new')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        print('i in init')
        self.args = args
        # self.name = kwargs.get('name') # Достаёт по одному указанному атрибуту
        # self.age = kwargs.get('age')
        for key, values in kwargs.items(): # достаёт сразу все атрибуты
            setattr(self, key, values)


other = [1, 2, 3]
user = {'name': 'Den', 'age': 25}

user_main = User(*other, **user)

print(user_main.args)
print(user_main.name)
print(user_main.age)
