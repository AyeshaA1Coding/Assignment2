class DiscountPolicy:
    """Handles discount logic for orders."""

    def __init__(self, discount_rate=0.10, min_items_for_bulk_discount=5):
        self.__discount_rate = discount_rate
        self.__min_items_for_bulk_discount = min_items_for_bulk_discount

    def apply_loyalty_discount(self, order):
        return order.apply_vat() * (1 - self.__discount_rate)

    def apply_bulk_discount(self, order):
        if len(order.__ebooks) >= self.__min_items_for_bulk_discount:
            return order.apply_vat() * 0.8
        return order.apply_vat()
