from abc import abstractmethod, ABC

class PizzaConstituents(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass