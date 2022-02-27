class ROLE:
    """
    Class for handling roles
    """

    def __init__(self, name: str):
        """Constructor to initialize role name"""
        self.name = name
        self.__parent = None  # private member
        self.__child = list()  # private member

    def __str__(self) -> str:
        return self.name
