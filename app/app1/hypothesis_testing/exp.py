from scipy.stats import chi2
from textmenu import * 
from basic_analysis.exp import ExpDistributionAnalyser
from hist_digits.digits import Digit as digit_handler

class ExpDistributionTest:

    alpha = 0.08
    
    def __init__(self, params, z) -> None:
        self.z = z
        self.params = params
        self.digit_handler = digit_handler(self.params)
        self.set_basic_analyser()
        self.set_description()

    def set_description(self):
        self.description = f"H0 – с.в. распределена показательно с параметром lambda = {self.params.lmbd}"

    def set_basic_analyser(self):
        self.analyser = ExpDistributionAnalyser(self.params)

    def enter_alpha(self):
        self.alpha = float(input("Введите alpha: " ))  

    # R0
    def get_measure_of_discrepancy(self, observed, expected):
        elements = [] 

        for i in range(len(observed)-1):
            r_0_i = ((observed[i] - expected[i])**2)/expected[i]
            elements.append(r_0_i)
            
        return sum(elements)

    def conclude (self, observed,expected,degrees_of_freedom):
        print("Проверим гипотезу: \n ",self.description)
        
        alpha_menu = TextMenu(description="Уровень значимости равен "+str(self.alpha)+". Изменить?", items = [
            TextMenuItem(description="Да", todo=[self.enter_alpha,[]]),
        ], default_exit=True)
        alpha_menu.display()  
        
        r = degrees_of_freedom        
        quantil_chi2 = chi2.ppf(1-self.alpha, r)        
        R0 = self.get_measure_of_discrepancy(observed,expected)
        
        print("r степеней свободы: ",r)    
        print("R0, alpha, r = ",R0,",",self.alpha,",",r)
        
        if R0 >= quantil_chi2:
            print("Гипотеза H0 отклоняется \n",R0,">=",quantil_chi2)
        else:
            print("Гипотеза H0 подтверждается \n",R0,"<",quantil_chi2)

    def test (self):
        digit_count = self.digit_handler.get_digit_count(self.z)
        observed = [self.digit_handler.get_digit_length(self.z,i) for i in range(digit_count)]

        n = self.params.n
        expected = [n*(self.analyser.get_distribution_theory(self.z[i+1])-self.analyser.get_distribution_theory(self.z[i])) for i in range(digit_count)]
        
        # zero division problem
        first_non_zero_index = 0
        for index, value in enumerate(expected):
            if value > 0: 
                first_non_zero_index = index
                break
        print("first_non_zero_index: ",first_non_zero_index)                        
        digit_count -= first_non_zero_index 
        self.conclude (observed[first_non_zero_index:], expected[first_non_zero_index:], digit_count-1)
