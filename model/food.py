class Food:
    def __init__(self, id, name, price):
        self._id = id
        self._name = name
        self._price = price

    def get_food_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def __str__(self):
        return f"Food(name={self._name}, price={self._price})"