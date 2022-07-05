class Errors:

    def __init__(self, analyser) -> None:
        self.analyser = analyser

    def get_err (self, theory, practice):
        return (abs(theory-practice)/theory)*100

    def get_distribution_err(self, x):
        theory, practice = self.analyser.get_distribution_theory(x), self.analyser.get_distribution_practice(x)
        return abs(theory-practice)  

    def get_dispersion_err(self):
        theory, practice = self.analyser.get_dispersion_theory(), self.analyser.get_dispersion_practice()
        return self.get_err(theory, practice)

    def get_expected_value_err(self):
        theory, practice = self.analyser.get_expected_value_theory(), self.analyser.get_expected_value_practice()
        return self.get_err(theory, practice)
