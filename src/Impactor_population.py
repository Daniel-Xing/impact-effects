import random

class Distribution:
    def __init__(self):
        return

class nomal_distribution(Distribution):
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std
        return
    
    def get_value(self):
        return random.normalvariate(self.mean, self.std)

class Impactor_population:
    def __init__():
        return
