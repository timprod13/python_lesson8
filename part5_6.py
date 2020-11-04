class OfficeEquipmentWarehouse:
    my_store = []

    def __init__(self, name, price, quantity, warranty_operating_time):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.warranty = warranty_operating_time
        self.my_store_full = []
        self.my_store = [[], [], []]

    def __str__(self):
        return f'{self.name}. Price is {self.price}. Quantity: {self.quantity}. Warranty: {self.warranty}'

    def reception(self):
        flag = int(input(f'Input type: 1 for printer, 2 for scanner, 3 for copier ')) - 1
        try:
            unit = input(f'Input model ')
            unit_p = int(input(f'Input price for 1 pcs '))
            unit_q = int(input(f'Input quantity '))
            unit_w = int(input('Input warranty operating time '))
            unique = {'Model': unit, 'Price for 1 pcs': unit_p, 'Quantity': unit_q, 'Warranty': unit_w}
            self.my_store[flag].append(unique)
            print(f'Current list: \n {self.my_store[flag]}')
        except ValueError:
            return f'!!!!!!!!!!Input error!!!!!!!!!!'

        if input('q for exit ') == 'q':
            self.my_store_full.append(self.my_store)
            print(f'All warehouse\n {self.my_store_full}')
            quit()
        else:
            return OfficeEquipmentWarehouse.reception(self)


class Printer(OfficeEquipmentWarehouse):
    def to_print(self):
        return f'{self.name} can print {self.warranty} times'


class Scanner(OfficeEquipmentWarehouse):
    def to_scan(self):
        return f'{self.name} can scan {self.warranty} times'


class Copier(OfficeEquipmentWarehouse):
    def to_copier(self):
        return f'{self.name} can copy {self.warranty} times'


printer = Printer('Canon LaserJet', 2000, 5, 1000)
scanner = Scanner('Konica Minolta', 1200, 5, 100000)
copier = Copier('Xerox Phaser', 1500, 1, 1500)
print(printer.reception())
print(scanner.reception())
print(copier.reception())
print(printer.to_print())
print(copier.to_copier())
