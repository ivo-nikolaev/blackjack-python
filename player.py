class Player(object):
    def __init__(self, p_name=None, p_cash=0):
        self.name = p_name
        self.cash = p_cash

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if type(new_name) == str: #type checking for name property
            self._name = new_name
        else:
            raise Exception("Invalid value for name - should be a string!")

    @property
    def cash(self):
        return self._cash

    @cash.setter
    def cash(self, new_cash):
        if type(new_cash) == int:
            self._cash = new_cash
        else:
            raise Exception("Invalid value for cash - should be an integer!")

    def __str__(self):
        return f"Name: {self.name} \nCash: {self.cash}"
