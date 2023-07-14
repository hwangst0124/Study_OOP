from model.mainService import MainService


class Manager:
    def __init__(self, manager_id, manager_pw):
        self._manager_id = manager_id
        self._manager_pw = manager_pw

    def get_manager_id(self):
        return self._manager_id

    def set_manager_id(self, manager_id):
        self._manager_id = manager_id

    def get_manager_pw(self):
        return self._manager_pw

    def set_manager_pw(self, manager_pw):
        self._manager_pw = manager_pw

    def __str__(self):
        return f"Manager(manager_id={self._manager_id})"
