class Node:
    def __init__(self, data_val=None):
        self.__data_val = data_val
        self.__next_val = None

    @property
    def next_val(self):
        return self.__next_val

    @next_val.setter
    def next_val(self, value):
        self.__next_val = value

    @property
    def data_val(self):
        return self.__data_val


class TicketNumber(Node):
    pass


class Child(Node):
    pass
