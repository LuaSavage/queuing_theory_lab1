from basic_analysis.type import DistributionType as distribution_type
from .exp import ExpDistributionTest
from .uniform import UniformDistributionTest

class Tester:
    @staticmethod
    def get_tester(params, z) -> None:
        if (distribution_type.get(params) == "exp"):
            return ExpDistributionTest(params, z)
        if (distribution_type.get(params) == "uniform"):
            return UniformDistributionTest(params, z)  
