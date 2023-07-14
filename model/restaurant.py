class Restaurant:
    def __init__(self, name, restaurant_code):
        self._name = name
        self._restaurant_code = restaurant_code
        self._menu = []

    def get_restaurant_code(self):
        return self._restaurant_code

    def set_restaurant_code(self, restaurant_code):
        self._restaurant_code = restaurant_code

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def add_menu(self, menu):
        self._menu.append(menu)
        menu.set_restaurant(self)

    def remove_menu(self, menu):
        if menu in self._menu:
            self._menu.remove(menu)
            menu.set_restaurant(None)

    def get_menu(self):
        return self._menu

    def set_menu(self, menus):
        self._menu = menus

    def __str__(self):
        return f"Restaurant(name={self._name}, restaurant_code={self._restaurant_code}, menus={self._menu})"