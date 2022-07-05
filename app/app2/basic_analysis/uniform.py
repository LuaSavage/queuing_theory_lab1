from basic_analysis.exp import ExpDistributionAnalyser 

class UniformDistributionDTO:
    def __init__(self, y = None, a  = None, b = None, n = None, x0 = None) -> None:
        self.x0 = x0
        self.n = n
        self.y = y
        self.a = a
        self.b = b

class UniformDistributionAnalyser(ExpDistributionAnalyser):

    def __init__(self, data) -> None:
        super().__init__(data)

    def get_expected_value_theory(self):
        return (self.params.a + self.params.b)/2

    def get_dispersion_theory(self):
        return ((self.params.b-self.params.a)**2)/12

    def get_density_distribution(self, x):
        if ((x > self.params.a) and (x < self.params.b)):
            return 1/(self.params.b-self.params.a)
            
        return 0        

    def get_distribution_theory(self, x):
        if ((x > self.params.a) and (x <= self.params.b)):
            return (x-self.params.a)/(self.params.b-self.params.a)

        if x <= self.params.a:
            return 0

        if x > self.params.b:
            return 1           


