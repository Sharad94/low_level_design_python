import zope.interface
from rainwater_trapping_solution_strategy import RainWaterTrappingSolutionStrategy

@zope.interface.implementer(RainWaterTrappingSolutionStrategy)
class RainWaterTrappingSolutionN21:
    def find_max_water(self, height_list):
        """

        :param height_list: height of buildings
        :return:
        """
        print("RainWaterTrappingSolutionN21")