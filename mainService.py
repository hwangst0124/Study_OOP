import json
import time
from Study_OOP import mode
from Study_OOP.model.account import Account
from Study_OOP.model.food import Food
from Study_OOP.model.manager import Manager
from Study_OOP.model.menu import Menu
from Study_OOP.model.restaurant import Restaurant

class MainService:
    def __init__(self, program_flag, json_data):
        self.program_flag = program_flag
        self.json_data = json_data

    def load_data(self):
        data = json.loads(self.json_data)

        # Account 객체 생성
        accounts = {}
        for account_data in data['accounts']:
            username = account_data['user_id']
            account = Account(username)
            accounts[username] = account

        # Manager 객체 생성
        manager_data = data['manager']
        manager_time = manager_data['time']
        manager_id = manager_data['manager_id']
        manager = Manager(manager_time, manager_id)

        # Restaurant 객체 생성
        restaurants = []
        for restaurant_data in data['restaurants']:
            name = restaurant_data['name']
            restaurant_code = restaurant_data['restaurant_code']

            menus = []
            for menu_data in restaurant_data['menu']:
                menu_name = menu_data['name']
                foods = []
                for food_data in menu_data['foods']:
                    food_name = food_data['name']
                    food_price = food_data['price']
                    food = Food(food_name, food_price)
                    foods.append(food)
                menu = Menu(menu_name)
                menu.set_foods(foods)
                menus.append(menu)

            restaurant = Restaurant(name, restaurant_code)
            restaurant.set_menu(menus)
            restaurants.append(restaurant)
        return accounts, manager, restaurants

    def service_start(self, program_flag = True):
        program_flag = program_flag
        accounts, manager, restaurants = self.load_data()

        while program_flag:

            print("""
            
                                                           /\      /\\
                                                           ||______||
                                                           || ^  ^ ||
                                                           \| |  | |/
                                                            |______|
                          __                                |  __  |
                         /  \       ________________________|_/  \_|__
                        / ^^ \     /=========================/ ^^ \===|
                       /  []  \   /=========================/  []  \==|
                      /________\ /=========================/________\=|
                   *  |        |/==========================|        |=|
                  *** | ^^  ^^ |---------------------------| ^^  ^^ |--
                 *****| []  [] |           _____           | []  [] | |
                *******        |          /_____\          |      * | |
               *********^^  ^^ |  ^^  ^^  |  |  |  ^^  ^^  |     ***| |
              ***********]  [] |  []  []  |  |  |  []  []  | ===***** |
             *************     |         @|__|__|@         |/ |*******|
            ***************   ***********--=====--**********| *********
            ***************___*********** |=====| **********|***********
             *************     ********* /=======\ ******** | *********
        
                 ************어서오세요 여기는 행복한 식권대장입니다~~~~******
                     ************ 현재는 [%s] 메뉴가 나옵니다 **********
            """ % (manager.get_time()))

            mode = mode.USERMODE
            while True:
                user_id = input("아이디를 입력하세요: ")

                if user_id == manager.get_manager_id():
                    print(f"환영합니다 관리자님")
                    mode = mode.ADMINMODE
                    break
                elif user_id in accounts:
                    print(f"환영합니다 {user_id}")
                    mode = mode.USERMODE
                    break
                else:
                    print("아이디가 틀렸습니다. 다시 입력해주세요!")

            if mode == mode.ADMINMODE:
                while True:
                        print("관리자 모드 입니다\n")
                        print("1. 시간대 변경\n")
                        print("2. 초기 화면으로 돌아가기\n")
                        print("3. 프로그램 종료")
                        manager_input = int(input())
                        if manager_input == 1:
                            print("원하는 시간대를 선택해주세요")
                            print("1. 아침")
                            print("2. 점심")
                            print("3. 저녁")
                            manager.set_time(mode.time[int(input())])
                            print(f"시간이 {manager.get_time()}로 변경되었습니다. ")
                        elif manager_input == 2:
                            mode = mode.USERMODE
                            break
                        elif manager_input == 3:
                            program_flag = False
                            break
                        else:
                            print("잘못 입력하셨습니다.")

            if mode == mode.USERMODE:
                print("식당을 선택하세요\n")
                for index, store in enumerate(restaurants):
                    print(f"{index + 1}. {store.get_name()}")
                select_restaurant_index = int(input()) - 1

                print(f"{restaurants[select_restaurant_index].get_name()}을 선택하셨습니다.\n")


                selected_restaurant = restaurants[select_restaurant_index]
                selected_time = manager.get_time()  # 관리자가 설정한 시간

                selected_menu = None
                # 관리자가 설정한 시간에 따른 메뉴를 찾아줌
                for menu in selected_restaurant.get_menu():
                    if menu.get_time() == selected_time:
                        selected_menu = menu
                        break

                selected_food = None
                if selected_menu:
                    print(f"{selected_menu.get_time()} 메뉴의 음식 목록:")
                    for index, food in enumerate(selected_menu.get_foods()):
                        print(f"{index + 1}. {food.get_name()} ({food.get_price()}원)")
                    print("메뉴의 음식을 선택해주세요.")
                    selected_food = selected_menu.get_foods()[int(input()) - 1]
                    print(f"메뉴의 총 가격은 {selected_food.get_price()} 입니다.")
                    print("결제 하시겠습니까?")
                    print("1. yes")
                    print("2. no")
                    payment = input()
                    if payment == "1":
                        print(f"{selected_food.get_price()}이 결제 되었습니다.")
                    if payment == "2":
                        print(f"안녕히 가십쇼.")
                else:
                    print("메뉴가 제공되지 않는 가게입니다.")
                    print(f"{selected_restaurant.get_name()}에서의 오늘의 추천 음식은:")
                    recommended_food = selected_restaurant.get_menu()[0].get_foods()[0]
                    print(f"- {recommended_food.get_name()} ({recommended_food.get_price()}원)")
                    print("결제 하시겠습니까?")
                    print("1. yes")
                    print("2. no")
                    payment = input()
                    if payment == "1":
                        print(f"{recommended_food.get_price()}이 결제 되었습니다.")
                    if payment == "2":
                        print(f"안녕히 가십쇼.")
            time.sleep(2)





