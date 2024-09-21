class Human:
    def __init__(self, name, group):
        self.name = name
        super().__init__(group)  # Добавление метода супер для доступа к следущему классу в наследовании
        super().about()  # Добавление метода супер для доступа к следущему классу в наследовании

    def info(self):
        print(f'Привет меня зовут {self.name}')


class Students_group:  # Не относиться ни к студенту ни к хуману
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f'{self.name} учиться в группе {self.group}')


# class Student(Human): # Не совсем верное(нежелательное) обращение к родительскому классу
#     def __init__(self, name, place):
#         Human.__init__(self, name)
#         self.place = place


class Student(Human, Students_group):  # Обращение к родительскому классу через метод "Super"
    # может наследоваться от нескольких классов, но нужно проверять цепочку снаследований!
    def __init__(self, name, place, group):
        super().__init__(name, group)
        self.place = place
        super().info()
        print(f'Я живу в {self.place}')



# human = Human('Лёлик','python one')
student = Student('Лелик', 'Общага', 'python one')
print(Student.mro())  # Проверка цепочки наследования,
