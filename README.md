Electronic Store Management System
This Python script implements a simple Electronic Store Management System. It allows users to add, modify, remove, list all items, save the data, and recover data from a file.

Class: ElectronicStore
The ElectronicStore class represents an electronic product in the store. It includes attributes such as the name of the product, price, type of electronic, brand, QR code, and the number of items in storage.

Methods
__str__(self): Returns a string representation of the electronic product.
toJSON(self): Converts the electronic product information to a JSON format.
Usage
Run the script, and a menu will be displayed with the following options:

1. Add item: Add a new electronic product to the store.
2. Modify item: Modify the information of an existing electronic product.
3. Remove item: Remove an electronic product from the store.
4. List of all items: Display a list of all electronic products in the store.
5. Exit: Terminate the program.
6. Save: Save the current state of the electronic products to a file.
7. Recover: Recover the electronic product information from a file.
Follow the on-screen instructions to perform the desired actions.

File Handling
The script supports saving and recovering electronic product information from a file (save.txt). The information is stored in JSON format.
