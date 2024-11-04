class Invoice:
    """Represents an invoice for an order."""

    def __init__(self, invoice_id, order_details, total_amount, discount, vat):
        self.__invoice_id = invoice_id
        self.__order_details = order_details
        self.__total_amount = total_amount
        self.__discount = discount
        self.__vat = vat

    def calculate_final_amount(self):
        return self.__total_amount * (1 - self.__discount) * (1 + self.__vat)

    def __str__(self):
        return f"Invoice(invoice_id={self.__invoice_id}, final_amount={self.calculate_final_amount()})"
