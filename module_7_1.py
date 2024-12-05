# Задача "Учёт товаров":

class Product:

    def __init__(self, name: str, weight: float, category: str):
        # обладать следующими свойствами:
        self.name = name # - название продукта (строка).
        self.weight = weight # - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
        self.category = category # - категория товара (строка).

    def __str__(self):
        # Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
        # Все данные в строке разделены запятой с пробелами.
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:

    # Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
    def __init__(self):
        self.__file_name = 'products.txt' # Инкапсулированный атрибут

    def get_products(self):
        # считывает всю информацию из файла __file_name, закрывает его и возвращает
        # единую строку со всеми товарами из файла __file_name.
        file = open(self.__file_name, 'r')
        line = file.read()
        file.close()
        return f'{line}'

    def add(self, *products: Product):
        new_products = products # принимает неограниченное количество объектов класса Product.
        file = open(self.__file_name, 'a')
        line_from_file = Shop.get_products(self)
        for product in products:
            if not product.name in line_from_file:
                # Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
                file.write(f'{product.__str__()}\n')
            else:
                # Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .
                print(f'Продукт {product.name} уже есть в магазине')
        file.close()

s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
