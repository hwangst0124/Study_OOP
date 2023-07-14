class FoodException(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class FoodNotFoundException(FoodException):
    def __init__(self, msg):
        super().__init__(msg)

class InvalidFoodException(FoodException):
    def __init__(self, msg):
        super().__init__(msg)