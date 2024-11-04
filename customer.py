class Customer:
    """Represents a customer in the e-bookstore."""

    def __init__(self, name, contact_info, loyalty_member=False):
        self.__name = name
        self.__contact_info = contact_info
        self.__loyalty_member = loyalty_member

    @property
    def loyalty_member(self):
        return self.__loyalty_member

    @loyalty_member.setter
    def loyalty_member(self, value):
        self.__loyalty_member = value

    def __str__(self):
        return f"Customer(name={self.__name}, loyalty_member={self.__loyalty_member})"
