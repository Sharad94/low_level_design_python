from pizza_constituents import PizzaConstituents

class Cheese(PizzaConstituents):
    def __init__(self, base_pizza):
        self._base_pizza = base_pizza

    def get_description(self):
        return self._base_pizza.get_description() + " + Cheese"

    def get_cost(self):
        return self._base_pizza.get_cost() + 80
