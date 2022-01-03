import csv


class Item:
    pay_rate = 0.8  # Intance classified as a class atributte or magic method
    all = []  # List that stores all instances

    '''
    The init function initiates the class, reciveing parameters applied for each object.
    For validation of parameters a data type can be especified avoiding type errors in the
    function; ex: parameter_name: datatype.
    '''

    def __init__(self, name: str, price: float, quantity=0):  # Declare initiation function

        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater than or equal to zero'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to Execute
        Item.all.append(self)

    # Defines a class function which calculate the total price of the object
    def calculate_total_price(self):
        return self.price * self.quantity

    # Class function which aply a discount in the object price
    def apply_discount(self):
        self.price *= self.pay_rate

        '''
        As best practice, the discount is applied in the instance level instead of the
        class level.
        '''

    # Class magic method which represent the objects
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    @classmethod  # Makes the function a class method
    def instantiate_from_csv(cls):
        with open('Items.csv', 'r') as f:  # Open the csv arquive
            reader = csv.DictReader(f)
            items = list(reader)  # Makes the csv arquive a0041

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer
        elif isinstance(num, int):
            return True
        else:
            return False


class Phone(Item):
    all = []

    # The base class of the class hierarchy
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater than or equal to zero'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero'
        assert broken_phones >= 0, f'Quantity {quantity} is not greater or equal to zero'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        self.broken_phone = broken_phones

        # Actions to execute
        Phone.all.append(self)

item1 = Item("Phone", 100, 5)  # Creating first item
item2 = Item("Laptop", 1000, 3)  # Creating second item

print(item1.calculate_total_price(), '\n---')  # Calculating total price with class funcion

# - Exemple of class atribute global presence propriety -
print(f'Desconto da classe: {Item.pay_rate}, Desconto do item 1: {item1.pay_rate}', '\n---')

# For viewing class atributes use magic atributte __dict__
print('Class Level Attributes:', Item.__dict__), print('---')  # All the attributes for Class level
print('Instance Level Attributes: ', item1.__dict__), print('---')  # All the attributes for instance level

# * Exemple of magic method level presence *

# Discount aplied without instance level overwrite
item1.apply_discount()
print(item1.price), print('---')

# Discount aplied with instance level overwrite
item2.pay_rate = 0.7  # Overwrite the discount value
item2.apply_discount()  # Aply the discount from the pay_rate instance
print('Price supposedly changed:', item2.price), print('---')  # Print the new price

Item3 = Item("Cable", 10, 5)
Item4 = Item("Mouse", 50, 5)
Item5 = Item("Keyboard", 75, 5)

# - Printing objects stored in the class -
for intance in Item.all:  # To print the objects stored in the class, a for loop can be used
    print('Instance:', intance)

    print('Instance name:', intance.name), print('---')
    '''
    To print a class attribute such as name simply use a method
    '''

# - Printing all instances at once with __repr__ magic attribute -
print(Item.all)

# - Calling static method -
print(Item.is_integer(7.5))  # Verify if the item is an integer

# * Inheritance *
print('\n* Inheritance *')

phone1 = Item("jscPhone10", 500, 5)
phone1.broke_phones = 1
phone2 = Item("jscPhone20", 700, 5)
phone2.broke_phones = 1

print(phone1.calculate_total_price())

