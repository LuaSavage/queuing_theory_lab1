import numpy as np
import scipy.stats as sp
import math

class ExpDistributionDTO:
    def __init__(self, y = None, lmbd = None, n = None, x0 = None) -> None:
        self.x0 = x0
        self.n = n
        self.y = y
        self.lmbd = lmbd

class ExpDistributionAnalyser :       

    def __init__(self, data) -> None:
        self.params = data

    def get_expected_value_theory(self):
        return 1/self.params.lmbd

    def get_expected_value_practice(self):
        #return (1/n)*sum(y)
        return sp.describe(self.params.y).mean

    def get_dispersion_theory(self):
        return 1/(self.params.lmbd**2) 

    def get_dispersion_practice(self):
        return np.std(self.params.y)**2

    def get_distribution_theory(self, x):
        return 1-math.exp((-1)*self.params.lmbd*x) if x>0 else 0
    
    def get_density_distribution(self, x):
        lmbd = self.params.lmbd
        return lmbd*math.exp((-1)*lmbd*x)

    def get_interval_count_less_x(self, x):
        count = 0
        for yi in self.params.y:
            if (yi < x):
                count += 1
        return count

    def get_distribution_practice(self,x):
        return self.get_interval_count_less_x(x)/self.params.n