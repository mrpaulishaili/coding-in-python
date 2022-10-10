from product import Product
from phone import Phone
from laptop import Laptop

phone1 = Phone('jscPhonev10', 500, 5, 1)
phone1.apply_increment(0.2)

laptop1 = Laptop('HPMini', 75000, 12)

print(phone1.name)
print(phone1.calculate_total_price())

print(laptop1)

print(Product.all)

phone1.send_email()
