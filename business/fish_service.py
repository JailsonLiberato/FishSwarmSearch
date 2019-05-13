class FishService(object):

    def __init__(self):
        self.__fishes = []
        self.__fitness_values = []

    def execute_fss(self):
        self.__initialize_position()
        self.initialize_weight()

    def __initialize_position(self):
        pass

    def __initialize_weight(self):
        pass

    @property
    def fitness_values(self):
        return self.__fitness_values

    @fitness_values.setter
    def fitness_values(self, fitness_values):
        self.__fitness_values = fitness_values
