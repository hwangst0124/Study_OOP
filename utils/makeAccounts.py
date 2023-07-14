import json
from faker import Faker

fake = Faker()

data = []

for _ in range(20):
    user_name = fake.user_name()
    user_id = fake.user_name()
    password = fake.password()

    account_data = {
        'nickname': user_name,
        'user_id': user_id,
        'user_password': password
    }

    data.append(account_data)

with open('../data/accounts.json', 'w') as f:
    json.dump(data, f, indent=2)
