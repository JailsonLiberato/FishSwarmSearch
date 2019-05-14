from business.functions.fitness_function import FitnessFunction
from model.fish import Fish
from util.constants import Constants
import numpy as np


class FishService(object):

    def __init__(self, fitness_function: FitnessFunction):
        self.__fishes = []
        self.__fitness_values = []
        self.__fitness_function: FitnessFunction = fitness_function

    def execute_fss(self):
        self.__initialize_position()
        self.initialize_weight()
        count_fitness: int = 0
        while self.__stop_criterion(count_fitness):
            for fish in self.__fishes:
                self.__find_neighbor_position(fish)
                self.__evaluate_fitness(fish)
                count_fitness += 1
                self.__feed_fish(fish)
            self.__evaluate_drift()
            for fish in self.__fishes:
                self.__execute_movement(fish)
            self.__calculate_barycenter()
            for fish in self.__fishes:
                self.__execute_volitive_movement(fish)
            self.__update_individual_evolution()

    def __initialize_position(self):
        for _ in range(Constants.N_FISHS):
            position = self.__generate_initial_position()
            fish = Fish(position)
            self.__fishes.append(fish)

    def __generate_initial_position(self):
        min_value = self.__fitness_function.min_initialization
        max_value = self.__fitness_function.max_initialization
        return np.random.uniform(min_value, max_value, size=(1, Constants.N_DIMENSIONS))

    def __initialize_weight(self):
        for fish in self.__fishes:
            fish.weight = self.__generate_initial_weight()

    @staticmethod
    def __generate_initial_weight():
        min_value = Constants.MIN_INITIAL_WEIGHT
        max_value = Constants.MAX_INITIAL_WEIGHT
        return np.random.uniform(min_value, max_value, size=(1, 1))

    @staticmethod
    def __stop_criterion(count_fitness):
        return count_fitness == Constants.MAX_FITNESS

    def __find_neighbor_position(self, fish):
        pass

    def __evaluate_fitness(self, fish):
        fish.fitness = self.__fitness_function.run(fish)

    def __feed_fish(self, fish):
        pass

    def __evaluate_drift(self):
        pass

    def __execute_movement(self, fish):
        pass

    def __calculate_barycenter(self):
        pass

    def __execute_volitive_movement(self, fish):
        pass

    def __update_individual_evolution(self):
        pass

    @property
    def fitness_values(self):
        return self.__fitness_values

    @fitness_values.setter
    def fitness_values(self, fitness_values):
        self.__fitness_values = fitness_values


