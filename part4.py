class OfficeEquipmentWarehouse:

    def __init__(self, name, price, quantity, number_of_lists):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Model': self.name, 'Price for 1 pcs': self.price, 'Quantity': self.quantity}

    def __str__(self):
        return f'{self.name}. Price is {self.price}. Quantity: {self.quantity}'


class Printer(OfficeEquipmentWarehouse):
    def to_print(self):
        return f'{self.name} can print {self.numb} times'


class Scanner(OfficeEquipmentWarehouse):
    def to_scan(self):
        return f'{self.name} can scan {self.numb} times'


class Copier(OfficeEquipmentWarehouse):
    def to_copier(self):
        return f'{self.name} can copy {self.numb} times'


printer = Printer('Canon LaserJet', 2000, 5, 1000)
scanner = Scanner('Konica Minolta', 1200, 5, 100000)
copier = Copier('Xerox Phaser', 1500, 1, 1500)
print(printer)
print(printer.to_print())
print(scanner)
print(scanner.to_scan())
print(copier)
print(copier.to_copier())