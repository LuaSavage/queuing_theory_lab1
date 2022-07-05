from textmenu import *
from basic_analysis.exp import ExpDistributionDTO
from basic_analysis.uniform import UniformDistributionDTO

class DistributionSelectorMenu:
    def __init__(self) -> None:        
        self.main_menu = TextMenu(description="Выберите тип распределения",items = [
            TextMenuItem(description="Показательное", todo=[self.create_params_by_class,[ExpDistributionDTO]]),
            TextMenuItem(description="Равномерное", todo=[self.create_params_by_class,[UniformDistributionDTO]],),
        ])

    def create_params_by_class(self, params_dto_class):
        self.params = params_dto_class()

    def display_selector(self):
        self.main_menu.display()
        return self.params
