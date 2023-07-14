
class AccountException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class InvalidAccountException(AccountException):
    def __init__(self, msg):
        super().__init__(msg)

class AccountNotFoundException(AccountException):
    def __init__(self, msg):
        super().__init__(msg)
