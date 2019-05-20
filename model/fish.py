import numpy as np
from util.constants import Constants


class Fish(object):

    def __init__(self, position):
        self.__position = position
        self.__weight = 0.0
        self.__fitness = 0.0
        self.__neighborhood = np.zeros(Constants.N_DIMENSIONS)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def fitness(self):
        return self.__fitness

    @fitness.setter
    def fitness(self, fitness):
        self.__fitness = fitness

    @property
    def neighborhood(self):
        return self.__neighborhood

    @neighborhood.setter
    def neighborhood(self, neighborhood):
        self.__neighborhood = neighborhood
