import unittest
from ebook import EBook
from customer import Customer
from shopping_cart import ShoppingCart
from order import Order
from discount_policy import DiscountPolicy

class TestEBookstore(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.ebook1 = EBook("Python Programming", "John Doe", "2021-01-01", "Programming", 29.99)
        self.ebook2 = EBook("Machine Learning", "Jane Smith", "2020-06-15", "AI", 39.99)
        self.customer = Customer("Alice", "alice@example.com", True)
        self.cart = ShoppingCart()
        self.discount_policy = DiscountPolicy()

    def test_add_ebook(self):
        """Test adding an e-book to the cart."""
        self.cart.add_item(self.ebook1)
        self.assertEqual(len(self.cart._ShoppingCart__cart_items), 1)
        self.assertEqual(self.cart._ShoppingCart__total_price, 29.99)

    def test_remove_ebook(self):
        """Test removing an e-book from the cart."""
        self.cart.add_item(self.ebook1)
        self.cart.remove_item(self.ebook1)
        self.assertEqual(len(self.cart._ShoppingCart__cart_items), 0)
        self.assertEqual(self.cart._ShoppingCart__total_price, 0)

    def test_loyalty_discount(self):
        """Test applying loyalty discount for the customer."""
        order = Order(1, self.customer)
        order.add_ebook(self.ebook1)
        order.add_ebook(self.ebook2)
        discounted_total = self.discount_policy.apply_loyalty_discount(order)
        self.assertAlmostEqual(discounted_total, 62.0784, places=2)  # 10% discount with VAT

    def test_bulk_discount(self):
        """Test applying bulk discount for 5 or more e-books."""
        order = Order(2, self.customer)
        for _ in range(5):
            order.add_ebook(self.ebook1)
        bulk_discounted_total = self.discount_policy.apply_bulk_discount(order)
        self.assertAlmostEqual(bulk_discounted_total, 127.992, places=2)  # 20% discount with VAT

    def test_generate_invoice(self):
        """Test generating an invoice with discounts and VAT."""
        order = Order(3, self.customer)
        order.add_ebook(self.ebook1)
        order.add_ebook(self.ebook2)
        invoice = order.generate_invoice()
        self.assertIn("Order ID: 3", invoice)
        self.assertIn("Total Price (with VAT):", invoice)

if __name__ == '__main__':
    unittest.main()
