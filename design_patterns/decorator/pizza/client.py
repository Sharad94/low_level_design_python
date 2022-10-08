from bbq_chicken import BBQChicken
from cheese import Cheese
from farmhouse import FarmHouse
from margherita import Margherita
from olive import Olive
from paneer import Paneer
from pepperoni import Pepperoni
from tomato import Tomato

new_pizza = Paneer(Cheese(Tomato(BBQChicken())))
print(new_pizza.get_description())
print(new_pizza.get_cost())

new_pizza_2 = Olive(Cheese(Olive(FarmHouse())))
print(new_pizza_2.get_description())
print(new_pizza_2.get_cost())