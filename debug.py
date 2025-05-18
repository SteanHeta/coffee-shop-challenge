from customer import Customer
from coffee import Coffee
from order import Order

# Test data setup
customer1 = Customer("Alice")
customer2 = Customer("Bob")
coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

# Create orders
order1 = Order(customer1, coffee1, 5.0)
order2 = Order(customer1, coffee2, 4.5)
order3 = Order(customer2, coffee1, 6.0)

# Test relationships
print(f"{customer1.name}'s orders: {len(customer1.orders())}")  # Should be 2
print(f"{coffee1.name} customers: {len(coffee1.customers())}")  # Should be 2
print(f"Latte average price: {coffee1.average_price():.2f}")  # Should be 5.5
print(f"Most aficionado for Latte: {Customer.most_aficionado(coffee1).name}")  # Should be Bob