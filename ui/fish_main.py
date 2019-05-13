from business.fish_service import FishService
from util.constants import Constants
from util.chart_util import ChartUtil

class FishMain(object):

    def __init__(self):
        self.__fish_service = FishService()

    def execute(self):
        self.__create_curve_line()
        self.__create_boxplot()

    def __create_curve_line(self):
        self.__fish_service.execute_fss()
        ChartUtil.create_curve_line(self.__fish_service.fitness_values)

    def __create_boxplot(self):
        boxplot_fitness_values = []
        for _ in range(Constants.N_BOXPLOT):
            self.__fish_service.execute_fss()
            fitness_values = self.__fish_service.fitness_values
            boxplot_fitness_values.append(fitness_values[len(fitness_values) - 1])
        ChartUtil.create_boxplot(boxplot_fitness_values)
