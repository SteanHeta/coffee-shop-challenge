import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee:
    def test_name_validation(self):
        coffee = Coffee("Frappe")

        with pytest.raises(AttributeError):
            coffee.name = "Macchiato"

        with pytest.raises(TypeError):
            Coffee(123)
        with pytest.raises(ValueError):
            Coffee("A")

    def test_relationships(self):
        coffee = Coffee("Frappe")
        customer1 = Customer("Lina")
        customer2 = Customer("John")

        Order(customer1, coffee, 5.0)
        Order(customer2, coffee, 8.0)

        assert len(coffee.orders0) == 2
