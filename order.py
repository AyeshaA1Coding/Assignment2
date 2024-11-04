class Order:
    """Represents an order made by a customer."""

    def __init__(self, order_id, customer):
        self.__order_id = order_id
        self.__customer = customer
        self.__ebooks = []
        self.__total_price = 0.0

    def add_ebook(self, ebook):
        self.__ebooks.append(ebook)
        self.__total_price += ebook.price

    def apply_vat(self, vat_rate=0.08):
        return self.__total_price * (1 + vat_rate)

    def generate_invoice(self):
        return f"Order ID: {self.__order_id}, Total Price (with VAT): {self.apply_vat()}"

    def __str__(self):
        return f"Order(order_id={self.__order_id}, total_price={self.__total_price}, customer={str(self.__customer)})"
