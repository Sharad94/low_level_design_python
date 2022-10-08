from rainwater_trapping_solution_strategy import RainWaterTrappingSolutionStrategy
from rainwater_trapping_solution_factory import RainWaterTrappingSolutionFactory

height_list = [1, 2, 3]
algo_complexity = input("Enter the algo you want to use: n1/nn/n21\n")

strategy = RainWaterTrappingSolutionFactory.get_rainwater_trapping_solution(algo_complexity)

strategy.find_max_water(height_list)