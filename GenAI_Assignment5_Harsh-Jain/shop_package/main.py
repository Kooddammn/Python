#Task 4: Importing the packge in main.py
import shop_package.discount as disc
from shop_package.billing import calculate_total
from shop_package import billing

print(disc.apply_discount(1000,10))
print(disc.flat_discount(1000))

print(calculate_total([100,200,300]))
print(billing.apply_tax(3000))