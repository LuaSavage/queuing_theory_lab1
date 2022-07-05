from textmenu import *
from basic_analysis.exp import ExpDistributionDTO
from view import ParamView
import scipy.stats as sp

class SaveOrderFlowMenu:
    def __init__(self, input_flow_params, storage, order_flow) -> None:     
        self.storage = storage
        self.order_flow = order_flow       
        self.input_flow_params = input_flow_params 
        self.main_menu = TextMenu(description=f"Выберите способ определения lmbd1:",items = [
            TextMenuItem(description="a) Lambda1 = 1/M*", todo=[self.save_a,[]]),
            TextMenuItem(description="б) Lambda1 = (m1/n)*Lambda", todo=[self.save_b,[]],),
        ], default_exit=True)

    def save(self, lmbd1):
        print(f"Lambda1 = {lmbd1}")                
        new_params = ExpDistributionDTO(y = self.order_flow.intervals, 
                                        lmbd = lmbd1, n = self.order_flow.intervals_len, 
                                        x0 = 1)
        print(ParamView.get(vars(new_params)))                            
        print("Новое состояние хранилища:\n")
        self.storage.add_data (new_params)    
        self.storage.save()
        self.storage.visualise_data()       

    def save_a(self):
        self.order_flow.get_intervals()
        mean = sp.describe(self.order_flow.intervals).mean
        lmbd1 = 1/mean
        self.save(lmbd1)

    def save_b(self):
        self.order_flow.get_intervals()
        m1 = self.order_flow.intervals_len
        lmbd1 = (m1/self.input_flow_params.n)*self.input_flow_params.lmbd
        self.save(lmbd1)

    def display(self):
        self.main_menu.display()

class SaveOrderFlowsMenu:
    def __init__(self, input_flow_params, storage, served_flow, unserved_flow) -> None:     
        self.storage = storage
        self.served_flow = served_flow       
        self.unserved_flow = unserved_flow       
        self.input_flow_params = input_flow_params 

        self.save_served_menu = TextMenu(description=f"Сохранить поток заявок П1 ?",items = [
            TextMenuItem(description="Да", todo=[self.save_served_flow,[]]),
        ], default_exit=True)

        self.save_unserved_menu = TextMenu(description=f"Сохранить поток заявок П2 ?",items = [
            TextMenuItem(description="Да", todo=[self.save_unserved_flow,[]]),
        ], default_exit=True)

    def save_served_flow(self):
        menu = SaveOrderFlowMenu(input_flow_params=self.input_flow_params, storage=self.storage, 
                                order_flow= self.served_flow)
        menu.display()

    def save_unserved_flow(self):
        menu = SaveOrderFlowMenu(input_flow_params=self.input_flow_params, storage=self.storage, 
                                order_flow= self.unserved_flow)
        menu.display()

    def display(self):
        self.save_served_menu.display()
        self.save_unserved_menu.display()

