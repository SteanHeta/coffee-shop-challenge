class Coffee:
    def __init__(self, name):
        self.name = name  # This will use the property setter

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters")
        if hasattr(self, '_name'):
            raise AttributeError("Coffee name cannot be changed after initialization")
        self._name = value

    def orders(self):
        """Returns all orders for this coffee"""
        from order import Order  # Local import to avoid circular dependency
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        """Returns unique customers who ordered this coffee"""
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        """Returns count of orders for this coffee"""
        return len(self.orders())
    
    def average_price(self):
        """Calculates average price of orders for this coffee"""
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)