import zope.interface
from rainwater_trapping_solution_strategy import RainWaterTrappingSolutionStrategy

@zope.interface.implementer(RainWaterTrappingSolutionStrategy)
class RainWaterTrappingSolutionNN:
    def find_max_water(self, height_list):
        """

        :param height_list: height of buildings
        :return:
        """
        print("RainWaterTrappingSolutionNN")


    def compute_left_max(self, height_list):
        """
        Gets index on left having max height

        :param height_list:
        :return:
        """
        left_max_list = [-1] * len(height_list)

        for i in range(1, len(height_list)):
            pass