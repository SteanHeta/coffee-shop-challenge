# Test the implementation
from customer import Customer
from coffee import Coffee
from order import Order

# Create instances
customer = Customer("Alex")
coffee = Coffee("Latte")

# Test order creation
order = Order(customer, coffee, 5.0)

# Test relationships
assert order in customer.orders()
assert coffee in customer.coffees()
assert order in coffee.orders()
assert customer in coffee.customers()

# Test bonus method
assert Customer.most_aficionado(coffee) == customer