import os

class Product():
    def __init__(self, name:str, weight:float, category:str) -> None:
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self) -> str:
        return f'{self.name}, {self.weight}, {self.category}'
    

class Shop():
    def __init__(self, file_name:str = 'products.txt') -> None:
        self.__file_name = file_name
        if not os.path.exists(file_name):
            file = open(file_name, 'x')
            file.close()


    def get_products(self) -> str:
        file = open(self.__file_name, 'r')
        string = file.read()
        file.close()
        return string
    
    def add(self, *products) -> None:
        products_in_file = self.get_products()
        file = open(self.__file_name, 'a')
        for product in products:
            name = str(product.name + ', ')
            if name in products_in_file:
                print(f"Продукт {product.name} уже есть в магазине")
            else:
                file.write(str(product) + "\n")
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())