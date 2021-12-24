class Item:
    pay_rate = 0.8  # Intance classified as a class atributte or magic method
    all = []  # List that stores all instances

    # For validation of parameters a data type must be especified
    # in the function; ex: parameter_name: datatype
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater than or equal to zero'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to Execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.pay_rate  # As best practice, the discount is applied in the instance level instead of the
        # class level

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)

print(item1.calculate_total_price()), print('---')

# Exemple of class atribute global presence propriety
print(Item.pay_rate, item1.pay_rate), print('---')

# For viewing class atributes use magic atributte __dict__
print('', Item.__dict__), print('---')  # All the attributes for Class level
print(item1.__dict__), print('---')  # All the attributes for instance level

# * Exemple of magic method level presence *

# Discount aplied without instance level overwrite
item1.apply_discount()
print(item1.price), print('---')

# Discount aplied with instance level overwrite
item2.pay_rate = 0.7  # Overwrite the discount value
item2.apply_discount()  # Aply the discount from the pay_rate instance
print('Price supposedly changed:', item2.price), print('---')  # Print the new price

item3 = Item("Cable", 10, 5)
Item4 = Item("Mouse", 50, 5)
Item5 = Item("Keyboard", 75, 5)

# To print the objects stored in the class, a for loop can be used
for intance in Item.all:
    print('Instance:', intance)

    # To print a class attribute such as name simply use a method
    print('Instance name:', intance.name), print('---')

# Printing all instances at once with __repr__ magic attribute
print(Item.all)
