class ShoppingCart:
    """Represents a shopping cart for a customer."""

    def __init__(self):
        self.__cart_items = []
        self.__total_price = 0.0

    def add_item(self, ebook):
        self.__cart_items.append(ebook)
        self.__total_price += ebook.price

    def remove_item(self, ebook):
        if ebook in self.__cart_items:
            self.__cart_items.remove(ebook)
            self.__total_price -= ebook.price

    def calculate_total(self):
        """Calculate the total price of items in the cart."""
        return self.__total_price

    def __str__(self):
        return f"ShoppingCart(total_price={self.__total_price}, items={[str(item) for item in self.__cart_items]})"
