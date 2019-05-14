from business.fish_service import FishService
from util.constants import Constants
from util.chart_util import ChartUtil
from business.functions.sphere_function import SphereFunction
from business.functions.rastringin_function import RastringinFunction
from business.functions.rosenbrock_function import RosenbrockFunction


class FishMain(object):

    def execute(self):
        sphere_function = SphereFunction()
        fish_service = FishService(sphere_function)
        self.__create_curve_line(fish_service)
        self.__create_boxplot(fish_service)

        rastringin_function = RastringinFunction()
        fish_service = FishService(rastringin_function)
        self.__create_curve_line(fish_service)
        self.__create_boxplot(fish_service)

        rosenbrock_function = RosenbrockFunction()
        fish_service = FishService(rosenbrock_function)
        self.__create_curve_line(fish_service)
        self.__create_boxplot(fish_service)

    @staticmethod
    def __create_curve_line(fish_service: FishService):
        fish_service.execute_fss()
        ChartUtil.create_curve_line(fish_service.fitness_values)

    @staticmethod
    def __create_boxplot(fish_service: FishService):
        boxplot_fitness_values = []
        for _ in range(Constants.N_BOXPLOT):
            fish_service.execute_fss()
            fitness_values = fish_service.fitness_values
            boxplot_fitness_values.append(fitness_values[len(fitness_values) - 1])
        ChartUtil.create_boxplot(boxplot_fitness_values)
