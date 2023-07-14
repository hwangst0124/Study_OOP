from repository.accountRepository import AccountRepository
from repository.foodRepository import FoodRepository

if __name__ == "__main__":
    print("시작")
    accountRepository = AccountRepository.get_instance()
    foodRepository = FoodRepository.get_instance()
    print("데이터 로드 완료")
    # for data in accountRepository.find_all():
    #     print(data)
    print(foodRepository.find_all())
    for data in foodRepository.find_all():
        print(data)

