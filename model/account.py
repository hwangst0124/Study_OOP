class Account:
    def __init__(self, nickname, user_id, user_password):
        self._nickname = nickname
        self._user_id = user_id
        self._user_password = user_password

    def get_nickname(self):
        return self._nickname

    def set_nickname(self, nickname):
        self._nickname = nickname

    def get_user_id(self):
        return self._user_id

    def set_user_id(self, new_id):
        self._user_id = new_id

    def get_user_password(self):
        return self._user_password

    def set_user_password(self, user_password):
        self._user_password = user_password

    def __str__(self):
        return f"Account(user_id={self._nickname})"
