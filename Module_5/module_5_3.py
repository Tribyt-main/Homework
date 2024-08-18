class House:
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
        return self.number_of_floors == self.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < self.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= self.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > self.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= self.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != self.number_of_floors

    def __add__(self, other):
        return self.number_of_floors + 10


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
