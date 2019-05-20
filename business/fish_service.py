from business.functions.fitness_function import FitnessFunction
from model.fish import Fish
from util.constants import Constants
import numpy as np


class FishService(object):

    def __init__(self, fitness_function: FitnessFunction):
        self.__fishes = []
        self.__fitness_values = []
        self.__fitness_function: FitnessFunction = fitness_function
        self.__movement = []

    def execute_fss(self):
        self.__initialize_position()
        self.__initialize_weight()
        count_fitness: int = 0
        while self.__stop_criterion(count_fitness) or count_fitness == 0:
            school_weight_1 = sum(map(lambda x: x.weight, self.__fishes))
            for fish in self.__fishes:
                self.__find_neighbor_position(fish)
                self.__evaluate_fitness(fish)
                self.__feed_fish(fish)
            count_fitness += Constants.N_EVALUATES
            school_weight_2 = sum(map(lambda x: x.weight, self.__fishes))
            drift = self.__evaluate_drift()
            for fish in self.__fishes:
                self.__execute_movement(fish, drift)
            barycenter = self.__calculate_barycenter()
            success = school_weight_2 > school_weight_1
            for fish in self.__fishes:
                self.__execute_volitive_movement(fish, barycenter, success)

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

    @staticmethod
    def __find_neighbor_position(fish):
        fish.neighborhood = fish.position + (fish.neighborhood * np.random.uniform(-1, 1,
                                                                                   size=(1, Constants.N_DIMENSIONS)))

    def __evaluate_fitness(self, fish):
        fish.fitness = self.__fitness_function.run(fish.neighborhood) - self.__fitness_function.run(fish.position)
        self.__fitness_values.append(fish.fitness)

    def __feed_fish(self, fish):
        max_fitness = max(f.fitness for f in self.__fishes)
        fish.weight += (fish.fitness / max_fitness)

    def __get_min_fitness(self):
        return min(f.fitness for f in self.__fishes)

    def __evaluate_drift(self):
        a = sum(map(lambda x: x.position * x.fitness, self.__fishes))
        b = sum(map(lambda x: x.fitness, self.__fishes))

        if b > 0:
            return a / b
        return np.zeros(self.__fishes[0].position.shape)

    @staticmethod
    def __execute_movement(fish, drift):
        fish.position += drift

    def __calculate_barycenter(self):
        a = sum(map(lambda x: x.position * x.weight, self.__fishes))
        b = sum(map(lambda x: x.weight, self.__fishes))
        return a / b

    @staticmethod
    def __execute_volitive_movement(fish, barycenter, success):
        a = fish.position - barycenter
        random_step = np.random.uniform(0, 1, fish.position.shape)
        v = Constants.VOLITIVE_MIN * (a / np.linalg.norm(a)) * random_step
        if success:
            fish.position -= v
        else:
            fish.position += v

    @property
    def fitness_values(self):
        return self.__fitness_values

    @fitness_values.setter
    def fitness_values(self, fitness_values):
        self.__fitness_values = fitness_values


