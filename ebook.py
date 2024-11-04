class EBook:
    """Represents an e-book in the catalog."""

    def __init__(self, title, author, publication_date, genre, price):
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    # Getter and setter methods
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def apply_discount(self, discount_rate):
        """Apply a discount to the price."""
        self.__price *= (1 - discount_rate)

    def __str__(self):
        return f"EBook(title={self.__title}, author={self.__author}, price={self.__price})"
