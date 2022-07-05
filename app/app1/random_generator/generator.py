import math
import random
from basic_analysis.type import DistributionType as distribution_type
from numpy.random import uniform

class Generator:
    @staticmethod
    def generate(params):
        if distribution_type.get(params) == "exp":
            return ExpGenerator(params).generate()
        if distribution_type.get(params) == "uniform":
            return UniformGenerator(params).generate()

class ExpGenerator:

    def __init__(self, params) -> None:
        self.params = params

    def generate_y (self, x):
        return (-1)*(math.log(1-x)/self.params.lmbd)

    def generate (self):
        x, y = [], []

        for i in range(0,self.params.n):
            rnd_value = random.random()
            x.append(rnd_value)
            y.append( self.generate_y(rnd_value) )
        #return x, y
        self.params.y = y

class UniformGenerator(ExpGenerator):

    def __init__(self, params) -> None:
        super().__init__(params)

    def generate_y (self, x):
        #return self.params.a + (self.params.b-self.params.a)*x
        return uniform(low=self.params.a, high=self.params.b)

