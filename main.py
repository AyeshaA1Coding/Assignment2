from ebook import EBook
from customer import Customer
from shopping_cart import ShoppingCart
from order import Order
from invoice import Invoice
from discount_policy import DiscountPolicy

def main():
    # Sample usage
    ebook1 = EBook("Python Programming", "John Doe", "2021-01-01", "Programming", 29.99)
    ebook2 = EBook("Machine Learning", "Jane Smith", "2020-06-15", "AI", 39.99)

    customer = Customer("Alice", "alice@example.com", True)

    cart = ShoppingCart()
    cart.add_item(ebook1)
    cart.add_item(ebook2)

    order = Order(1, customer)
    order.add_ebook(ebook1)
    order.add_ebook(ebook2)

    print(order.generate_invoice())

if __name__ == "__main__":
    main()
