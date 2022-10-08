from pizza_constituents import PizzaConstituents

class Paneer(PizzaConstituents):
    def __init__(self, base_pizza):
        self._base_pizza = base_pizza

    def get_description(self):
        return self._base_pizza.get_description() + " + Paneer"

    def get_cost(self):
        return self._base_pizza.get_cost() + 60
