from .exp import ExpDistributionDTO
from .uniform import UniformDistributionDTO

class DistributionType:

    @classmethod
    def get(cls, distribution_dto):
        if type(distribution_dto) == ExpDistributionDTO:
            return "exp"
        if type(distribution_dto) == UniformDistributionDTO:
            return "uniform"        
