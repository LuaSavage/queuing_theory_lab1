from scipy.stats import chi2
from textmenu.menu import TextMenu 
from textmenu.item import TextMenuItem
from basic_analysis.uniform import UniformDistributionAnalyser
from hist_digits.digits import Digit as digit_handler

from .exp import ExpDistributionTest 

class UniformDistributionTest(ExpDistributionTest):
    
    def __init__(self, params, z) -> None:
        super().__init__(params, z)

    def set_description(self):
        self.description = f"H0 – с.в. распределена равномерно с параметрами a = {self.params.a}  b = {self.params.b}"

    def set_basic_analyser(self):
        self.analyser = UniformDistributionAnalyser(self.params)