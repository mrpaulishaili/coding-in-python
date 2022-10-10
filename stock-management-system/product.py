import csv


class Product:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Product.all.append(self)

    @property
    # Property Decorator = Read Only Attribute for Name
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    # Property Decorator = Read Only Attribute for Price
    def price(self):
        return self.__price

    def calculate_total_price(self):
        return self.__price * self.quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @price.setter
    def price(self, value):
        self.__price = value

    @classmethod
    def instantiate_from_csv(cls):
        with open('products_data.csv', 'r') as f:
            reader = csv.DictReader(f)
            products = list(reader)

        for product in products:
            Product(name=product.get('name'), price=float(product.get('__price')),
                    quantity=int(product.get('quantity')))

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.__price}', '{self.quantity}' )"

    # Email Abstraction
    def __connect(self, smtp_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello Someone.
        We have {self.__name} {self.quantity} times.
        Regards, PaulIshaili
        """

    def __send(self):
        print(self.__prepare_body())

    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()
