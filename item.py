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
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to Execute
        Item.all.append(self)

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        print('You are trying to get an attribute!')
        return self.__name

    '''
    Adding one more underline befone name, turns it into a private attribute, preventing it 
    from being seen in the instance level.
    '''

    @name.setter
    def name(self, value):
        print('You are trying to set an attribute!')
        self.__name = value

    '''
    A Setter allows the object property to be changed.
    '''

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
