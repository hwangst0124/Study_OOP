import json

from Exception.AccountException import AccountNotFoundException, InvalidAccountException
from model.account import Account




class AccountRepository:
    _instance = None

    @staticmethod
    def get_instance():
        if not AccountRepository._instance:
            AccountRepository._instance = AccountRepository()
        return AccountRepository._instance

    def __init__(self):
        self._accounts = []
        self._load_data()

    def _load_data(self):
        try:
            with open('data/accounts.json', 'r') as f:
                data = json.load(f)
                for account_data in data:
                    account = Account(
                        account_data['nickname'],
                        account_data['user_id'],
                        account_data['user_password']
                    )
                    self._accounts.append(account)
        except FileNotFoundError:
            self._accounts = []
        except Exception:
            self._accounts = []

    def commit(self):
        data = []
        for account in self._accounts:
            data.append({
                'nickname': account.get_nickname(),
                'user_id' : account.get_user_id(),
                'user_password' : account.get_user_password()
            })
        with open('data/accounts.json', 'w') as f:
            json.dump(data, f, indent=2)

    def add_account(self, account):
        for json_account in self._accounts:
            if json_account.get_nickname() == account.get_nickname() or json_account.get_user_id() == account.get_user_id():
                raise InvalidAccountException("Nickname or user ID already exists.")
        self._accounts.append(account)
        self.commit()

    def find_account_by_id(self, user_id):
        for account in self._accounts:
            if account.get_user_id() == user_id:
                return account
        raise AccountNotFoundException(f"Account not found with user_id: {user_id}")

    def find_all(self):
        return self._accounts

    def update_account_nickname(self, user_id, new_nickname):
        account = self.find_account_by_id(user_id)
        if account:
            account.set_nickname(new_nickname)
            self.commit()
        else:
            raise AccountNotFoundException(f"Account not found with user_id: {user_id}")

    def delete_account(self, account):
        if account in self._accounts:
            self._accounts.remove(account)
            self.commit()
        else:
            raise AccountNotFoundException("Account not found.")
