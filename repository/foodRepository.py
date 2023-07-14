import json
import traceback
from Exception.FoodException import FoodNotFoundException, InvalidFoodException
from model.food import Food




class FoodRepository:
    _instance = None

    @staticmethod
    def get_instance():
        if not FoodRepository._instance:
            FoodRepository._instance = FoodRepository()
        return FoodRepository._instance

    def __init__(self):
        self._foods = []
        self._load_data()

    def _load_data(self):
        try:
            with open('data/foods.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                foods = data['foods']
                for food_data in foods:
                    food_id = int(food_data['food_id'])
                    name = food_data['name']
                    price = int(food_data['price'])
                    food = Food(food_id, name, price)
                    self._foods.append(food)
        except FileNotFoundError:
            print("파일을 찾지 못했습니다.")
            traceback.print_exc()
            self._foods = []
        except Exception:
            print("알 수 없는 오류로 에러가 발생했습니다.")
            traceback.print_exc()
            self._foods = []

    def commit(self):
        data = []
        for food in self._foods:
            data.append({
                'id': food.get_food_id(),
                'name': food.get_name(),
                'price': food.get_price()
            })
        with open('data/foods.json', 'w') as f:
            json.dump(data, f, indent=2)

    def add_food(self, food):
        for existing_food in self._foods:
            if existing_food.get_food_id() == food.get_food_id():
                raise InvalidFoodException("Food with the same ID already exists.")
        self._foods.append(food)
        self.commit()

    def find_food_by_id(self, food_id):
        for food in self._foods:
            if food.get_food_id() == food_id:
                return food
        raise FoodNotFoundException(f"음식을 찾지 못했습니다. id : {food_id}")

    def find_all(self):
        return self._foods

    def update_food(self, food_id, new_name, new_price):
        food = self.find_food_by_id(food_id)
        if food:
            food.set_name(new_name)
            food.set_price(new_price)
            self.commit()
        else:
            raise FoodNotFoundException(f"음식을 찾지 못했습니다. id : {food_id}")

    def delete_food(self, food):
        if food in self._foods:
            self._foods.remove(food)
            self.commit()
        else:
            raise FoodNotFoundException(f"음식을 찾지 못했습니다. id : {food.get_food_id()}")

