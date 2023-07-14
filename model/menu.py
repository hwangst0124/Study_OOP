class Menu:
    def __init__(self, time):
        self._time = time
        self._foods = []

    def get_time(self):
        return self._time

    def set_time(self, time):
        self._time = time

    def add_food(self, food):
        self._foods.append(food)

    def remove_food(self, food_name):
        for food in self._foods:
            if food.get_name() == food_name:
                self._foods.remove(food)
                break
        print(f"[{food_name}] 이름을 가진 음식은 없습니다.")

    def get_foods(self):
        return self._foods

    def get_total_price(self):
        return sum([food.get_price() for food in self._foods])

    def set_foods(self, foods):
        self._foods = foods

    def __str__(self):
        return f"Menu(time={self._time}, foods={self._foods})"