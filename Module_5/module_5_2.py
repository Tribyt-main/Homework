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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
print(len(h1))
print(str(h1))
print(len(h2))
print(str(h2))