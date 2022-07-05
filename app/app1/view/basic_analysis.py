from basic_analysis.exp import ExpDistributionAnalyser
from basic_analysis.uniform import UniformDistributionAnalyser
from basic_analysis.error import Errors
from basic_analysis.type import DistributionType as distribution_type

class BasicAnalyser :
    def __init__(self, params, distr_type = None ) -> None:
        self.params = params

        if (distribution_type.get(params) == "exp") or (distr_type == "exp"):
            self.analyser = ExpDistributionAnalyser(params)
        if (distribution_type.get(params) == "uniform") or (distr_type == "uniform"):
            self.analyser = UniformDistributionAnalyser(params)  

        self.errors = Errors(self.analyser)

    def display (self) :
        theory, practice = self.analyser.get_expected_value_theory(), self.analyser.get_expected_value_practice()
        error = self.errors.get_expected_value_err()
        print(f"Мат ожидание \n Теория: {theory:.4f}; практика: {practice:.4f}; отклонение: {error:.4f}%")

        theory, practice = self.analyser.get_dispersion_theory(), self.analyser.get_dispersion_practice()
        error = self.errors.get_dispersion_err()
        print(f"Дисперсия \n Теория: {theory:.4f}; практика: {practice:.4f}; отклонение: {error:.4f}%")

        theory, practice = self.analyser.get_distribution_theory(self.params.x0), self.analyser.get_distribution_practice(self.params.x0)
        error = self.errors.get_distribution_err(self.params.x0)
        print(f"Функция распределения \n Теория: {theory:.4f}; практика: {practice:.4f}; отклонение: {error:.4f}")