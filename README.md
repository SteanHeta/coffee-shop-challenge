# coffee-shop-challenge# Coffee Shop Domain Model

A Python implementation of a coffee shop domain model demonstrating object relationships, including one-to-many and many-to-many associations between Customers, Coffees, and Orders.

## Features

- **Customer Management**:
  - Create customers with validated names (1-15 characters)
  - Track all orders made by each customer
  - View unique coffees ordered by each customer

- **Coffee Management**:
  - Create coffee items with validated names (minimum 3 characters)
  - Track all orders for each coffee
  - Calculate average price and total orders per coffee

- **Order System**:
  - Create orders linking customers and coffees
  - Validate order prices (1.0-10.0 range)
  - Maintain immutable properties where required

- **Bonus Feature**:
  - Identify the customer who spent the most on a specific coffee

## Class Diagram


classDiagram
    class Customer {
        +name: str
        +orders() List[Order]
        +coffees() List[Coffee]
        +create_order(coffee, price) Order
        +most_aficionado(coffee) Customer
    }

    class Coffee {
        +name: str
        +orders() List[Order]
        +customers() List[Customer]
        +num_orders() int
        +average_price() float
    }

    class Order {
        +customer: Customer
        +coffee: Coffee
        +price: float
        +all: List[Order]
    }

   