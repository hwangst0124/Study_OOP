class MainService:
    _instance = None

    @staticmethod
    def get_instance():
        if not MainService._instance:
            MainService._instance = MainService()
        return MainService._instance

    def __init__(self):
        self._time = None
        self._restaurants = []

    def get_time(self):
        return self._time

    def set_time(self, time):
        self._time = time

    def get_restaurants(self):
        return self._restaurants

    def add_restaurant(self, restaurant):
        self._restaurants.append(restaurant)

    def remove_restaurant(self, restaurant_code):
        for restaurant in self._restaurants:
            if restaurant.get_restaurant_code() == restaurant_code:
                self._restaurants.remove(restaurant)
                break
        else:
            print(f"[{restaurant_code}]를 가진 식당은 없습니다.")

    def __str__(self):
        return f"MainService(time={self._time})"