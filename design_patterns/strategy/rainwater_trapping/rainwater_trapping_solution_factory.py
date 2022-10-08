
from rainwater_trapping_solution_n1 import RainWaterTrappingSolutionN1
from rainwater_trapping_solution_n21 import RainWaterTrappingSolutionN21
from rainwater_trapping_solution_nn import RainWaterTrappingSolutionNN

class RainWaterTrappingSolutionFactory:
    @staticmethod
    def get_rainwater_trapping_solution(algo_complexity):
        """
        Gives a rainwater trapping solution based on complexity

        :return:
        """
        if algo_complexity == "n21":
            rainwater_trapping_solution = RainWaterTrappingSolutionN21()
        elif algo_complexity == "n1":
            rainwater_trapping_solution = RainWaterTrappingSolutionN1()
        elif algo_complexity == "nn":
            rainwater_trapping_solution = RainWaterTrappingSolutionNN()
        else:
            raise Exception("Unexpected input")

        return rainwater_trapping_solution

