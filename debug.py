from customer import Customer
from coffee import Coffee
from order import Order 

# Customer
customer1 = Customer("Lina")
customer2 = Customer("John")
coffee1 = Coffee("Frappe")
coffee2 = Coffee("Macchiato")

# Orders
order1 = Order(customer1, coffee1, 5.0)
order2 = Order(customer1, coffee2, 4.5)
order3 = Order(customer2, coffee2, 8.0)
order4 = Order(customer2, coffee1, 9.9)

# Tests
print(f"{customer1.name}'s orders: {len(customer1.orders())}")  
print(f"{coffee1.name} customers: {len(coffee1.customers())}")  
print(f"Latte average price: {coffee1.average_price():.2f}")
print(f"{customer1.name}'s favourite order is {coffee1.name}")  
print(f"Most aficionado for Latte: {Customer.most_aficionado(coffee1).name}") 
print(f"{customer2.name}'s orders: {len(customer2.orders())}") 