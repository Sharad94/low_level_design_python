import zope.interface


class RainWaterTrappingSolutionStrategy(zope.interface.Interface):

    def find_max_water(self, height_list):
        pass