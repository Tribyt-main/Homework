class Product:
    def __init__(self, name, weigh, category):
        self.name = name
        self.weigh = float(weigh)
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weigh}, {self.category}'


class Shop():
    def __init__(self, *products):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        text = file.read()
        file.close()
        return text

    def add(self, *products):
        product = self.get_products()
        file = open(self.__file_name, 'a')
        for item in products:
            if str(item) not in product:
                file.write(str(item) + '\n')
                product += str(item) + "\n"
            else:
                print(f'Продукт уже есть на складе  ')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
