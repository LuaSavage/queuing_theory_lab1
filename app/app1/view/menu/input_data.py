from textmenu import *
from storage import Storage
from basic_analysis.type import DistributionType
from random_generator import Generator
from view import ParamView

class InputExpParamsForm:
    def __init__(self, params) -> None:
        self.params = params

    def call_user_input(self):
        self.params.n = int(input("Введите n: " ))
        self.params.lmbd = float(input("Введите lambda: "))
        self.params.x0 = float(input("Введите x0: "))        

class InputUniformParamsForm:
    def __init__(self, params) -> None:
        self.params = params
        
    def call_user_input(self):
        self.params.n = int(input("Введите n: " ))
        self.params.a = float(input("Введите a: "))
        self.params.b = float(input("Введите b: "))        
        self.params.x0 = float(input("Введите x0: "))

class MainMenu:

    def __init__(self, params, storage) -> None:
        self.params, self.storage = params, storage

        self.save_data_menu = TextMenu(description="Сохранить введенные данные?",items = [
            TextMenuItem(description="Да", todo=[self.save_inputed_data,[]]),
            TextMenuItem(description="Нет"),
        ])
        
        self.load_row_menu = TextMenu(description="Выберите действие",items=[
            TextMenuItem(description="Ввести номер записи", todo=[self.enter_row_number,[]]),
            TextMenuItem(description="Назад"),
        ])

        self.main_menu = TextMenu(description="Выберите способ ввода параметров",items = [
            TextMenuItem(description="Ввести самостоятельно x0, n, lambda.", todo=[self.input_data_manually,[]]),
            TextMenuItem(description="Загрузить из файла.", sub_menu = self.load_row_menu, todo=[self.visualise_menu_action,[]],),
        ], default_exit=True)
        
        self.load_row_menu.items[1].sub_menu = self.main_menu
        self.main_menu.display()

    def save_inputed_data (self):
        print("Новое состояние хранилища:\n")
        self.storage.add_data (self.params)    
        self.storage.save()
        self.storage.visualise_data()
        
    def input_data_manually (self):
        distribution_alias = DistributionType.get(self.params)

        if distribution_alias == "exp":
            InputExpParamsForm(self.params).call_user_input()    
        if distribution_alias == "uniform":
            InputUniformParamsForm(self.params).call_user_input()

        Generator.generate(self.params)
        self.save_data_menu.display()

    def enter_row_number(self):
        row_number = int(input("Введите номер записи\n"))
        self.storage.get_data(self.params, row_number)

        if len(self.params.y or []) == 0:
            Generator.generate(self.params)

        print("Загружено из записи " +str(row_number)+ ":")
        print(ParamView.get(vars(self.params)))

    def visualise_menu_action(self):
        self.storage.visualise_data(self.params)
        