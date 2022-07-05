from textmenu import *
from random_generator import Generator
from view import ParamView

class MainMenu:

    def __init__(self, params, storage) -> None:
        self.params, self.storage = params, storage
 
        self.load_row_menu = TextMenu(description="Выберите действие",items=[
            TextMenuItem(description="Ввести номер записи", todo=[self.enter_row_number,[]]),
            TextMenuItem(description="Назад"),
        ])

        self.main_menu = TextMenu(description="Выберите способ ввода параметров",items = [
            TextMenuItem(description="Загрузить из файла.", sub_menu = self.load_row_menu, todo=[self.visualise_menu_action,[]],),
        ], default_exit=True)
        
        self.load_row_menu.items[1].sub_menu = self.main_menu
        self.main_menu.display()

    def enter_row_number(self):
        row_number = int(input("Введите номер записи\n"))
        self.storage.get_data(self.params, row_number)

        if len(self.params.y or []) == 0:
            Generator.generate(self.params)

        print("Загружено из записи " +str(row_number)+ ":")
        print(ParamView.get(vars(self.params)))

    def visualise_menu_action(self):
        self.storage.visualise_data(self.params)
        