from item import Item
from phone import Phone


def main():
    item1 = Item("Phone", 100, 5)  # Creating first item
    item2 = Item("Laptop", 1000, 3)  # Creating second item

    print(item1.calculate_total_price(), '\n---')  # Calculating total price with class funcion

    # - Exemple of class atribute global presence propriety -
    print(f'Class Discount: {Item.pay_rate}, item 1 discount: {item1.pay_rate}', '\n---')

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

    item3 = Item("Cable", 10, 5)
    item4 = Item("Mouse", 50, 5)
    item5 = Item("Keyboard", 75, 5)

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

    # Before adding class parameter broken phones
    phone1 = Phone("jscPhone10", 500, 5)
    phone1.broken_phones = 1

    # After adding class parameter broken phones
    phone1 = Phone("jscPhone20", 700, 5, 1)

    # Checking if the class works by printing the return of a master class function
    print(phone1.calculate_total_price())

    # * Setters and Getters *

    # Setting an attribute
    phone1.__name = 'AAA'

    # Getting an attribute
    print(phone1.name)

    '''
    The Setter sets an attribute to be manipulated and the Getter gets it for an specific porpuse.
    '''
