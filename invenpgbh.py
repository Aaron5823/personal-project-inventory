import json 

class ElectronicStore:
    def __init__(self, name_of_product, price, type_of_electronic, Brand, QR_code, number_in_storage):
        self.name_of_product = name_of_product
        self.price = price
        self.type_of_electronic = type_of_electronic
        self.Brand = Brand
        self.QR_code = QR_code
        self.number_in_storage = number_in_storage
    
    def __str__(self) -> str:
        return (
            f"name_of_product: {self.name_of_product}, price: {self.price}, type_of_electronic: {self.type_of_electronic},"
            f"Brand: {self.Brand}, QR_code: {self.QR_code}, number_in_storage: {self.number_in_storage}"
        )
    def toJSON(self):
        return {
            'name_of_product': self.name_of_product,
            'price': self.price,
            'type_of_electronic': self.type_of_electronic,
            'Brand': self.Brand,
            'QR_code': self.QR_code,
            'number_in_storage': self.number_in_storage
    }


items_info = []


def menu():
    print("=" * 40)
    print("Item Menu")
    print("1. Add item.")
    print("2. Modify item.")
    print("3. Remove item.")
    print("4. List of all items.")
    print("5. Exit.")
    print("6. Save. ")
    print("7. Recover. ")
    print("=" * 40)


def add_info():
    new_item = ElectronicStore(
        input('Name of product: '),
        float(input('Price: ')),
        input('Type of electronic: '),
        input('Brand: '),
        int(input('QR code: ')),
        int(input('Number in storage: '))
    )
    items_info.append(new_item)
    print(new_item)


def modify_info():
    items = len(items_info)
    print(f'Number in storage: {items}')
    item_number = int(input('The number of the item: '))
    items_info.remove(items_info[item_number])
    new_item = ElectronicStore(
        input('Name of product: '),
        float(input('Price: ')),
        input('Type of electronic: '),
        input('Brand: '),
        int(input('QR code: ')),
        int(input('Number in storage: '))
    )
    items_info.append(new_item)


def del_info(items_info):
    items = len(items_info)
    print(f'Storage amount: {items}')
    del_num = int(input('The item number: '))
    del_num = del_num - 1
    del items_info[del_num]


def show_infos():
    for item in items_info:
        print(item)
        
def save():
    import os
    import json
    file = open('C:/hw/save.txt', 'a')
    json.dump([i.toJSON() for i in items_info], file)
    file.close()


def recover():
    global items_info
    file = open('C:/hw/save.txt')
    content = json.load(file)
    items_info = [ElectronicStore(**i) for i in content]
    file.close()




def main():
    while True:
        menu()
        key = input("Select action: ")
        if key == '1':
            add_info()
        elif key == '2':
            modify_info()
        elif key == '3':
            del_info(items_info)
        elif key == '4':
            show_infos()
        elif key == '5':
            break
        elif key == '6':
            save()
        elif key == '7':
            recover()


print(main())
