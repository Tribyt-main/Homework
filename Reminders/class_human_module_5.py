class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}')

    def birthdey(self):
        self.age += 1
        print(f'У меня день рождения, мне {self.age}')


den = Human('Денис', 22)
max = Human('Макс', 22)

den.birthdey()

