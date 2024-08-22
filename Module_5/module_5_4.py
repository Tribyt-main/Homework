class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args)
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    def go_to(self, new_floor):
        for i in range(self.number_of_floors + 1):
            if i >= 1:
                if i == 2:
                    break
                for j in range(new_floor + 1):
                    if j >= 1:
                        if new_floor < 1:
                            print('Такого этажа не существует')
                            break
                        elif new_floor > self.number_of_floors:
                            print('Такого этажа не существует')
                            break
                        else:
                            print(j)

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)

    def __radd__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)

    def __iadd__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(h1.houses_history)
h2 = House('ЖК Акация', 20)
print(h1.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(h1.houses_history)
del h2
del h3
print(House.houses_history)
