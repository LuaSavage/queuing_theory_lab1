import math
import pandas as pd
from textmenu import *
from storage import Storage

## Part 1
## select distribution type
from view.menu import DistributionSelectorMenu, MainMenu
params = DistributionSelectorMenu().display_selector()

## load or input data
#import os
#storage = Storage(path=os.getcwd())
storage = Storage(path=".")
MainMenu(params, storage)

## Basic analysis be mean values and variance
from view.basic_analysis import BasicAnalyser
BasicAnalyser(params,"exp").display()

## Part 3
## Graph digits choosing methods
import numpy as np
from hist_digits import Digit, ManualDigits, SturgesDigits, EqualHeightDigits, ApproximatelyEqualHeightDigits

digits_class = SturgesDigits
def set_sturges_digits():
    digits_class = SturgesDigits 

def set_digits_with_equal_height():
    digits_class = EqualHeightDigits 
       
def set_digits_with_approximately_equal_height():
    digits_class = ApproximatelyEqualHeightDigits    
            
def set_manual_digits():
    digits_class = ManualDigits      
    
digit_mode_menu=TextMenu(description="Выберите способ определения разрядов гистограммы", items = [
    TextMenuItem(description="Все разряды одинаковой длины. Их количество определяется формулой Стерджесса", todo=[set_sturges_digits,[]]),
    TextMenuItem(description="Разряды выбираются таким образом, чтобы в них состояло примерно одинаковое число значений", todo=[set_digits_with_approximately_equal_height,[]]),
    TextMenuItem(description="Сначала разряды выбираются по формуле Стерджесса, затем наиболее крупные делятся, а менее крупные объединяются.", todo=[set_digits_with_equal_height,[]]),
    TextMenuItem(description="Ввод вручную", todo=[set_manual_digits,[]])
])
digit_mode_menu.display()

## Hist plot

from view.hist import HistPlot as hist_plot
z = digits_class(params).get()
hist_plot(params).plot(z)

## Part 3 Hypothesis test

from hypothesis_testing.tester import Tester as hypothesis_tester
hypo_tester = hypothesis_tester.get_tester(params,z)
hypo_tester.test()

##  Part 4
from basic_analysis.type import DistributionType as distribution_type
if distribution_type.get(params) == "exp":
    import collections
    from hist_digits.digits import Digit
    from basic_analysis.exp import ExpDistributionDTO

    print("Часть 4. Проверка гипотезы о распределении Пуассона")

    tau = [sum(params.y[:i]) for i in range(len(params.y))[1:]]
    print("lambda =",params.lmbd,"N =",params.n,"\n- Значение lambda*t0 желательно в пределах от 3 до 5\n- N должен быть таким, чтобы значение  m  было не меньше 100.")
        
    t0 = float(input("Введите t0: " ))  
    m = math.ceil(tau[-1]/t0)
    mu = params.lmbd*t0

    print("t0 =",t0,"m =",m,"lambda*t0 =",params.lmbd*t0)

    tau_z = []    
    digit_handler = Digit(ExpDistributionDTO(y = tau, lmbd = mu, n = len(tau), x0 = params.x0))
    tau_z = digit_handler.get_digits_with_equal_length (t0)

    count_of_request = []
    for i in range(len(tau_z)-1):
        count_of_request.append(digit_handler.get_digit_length(tau_z,i))

    request_count_per_holders_interval = collections.Counter(count_of_request)
    #print(request_count_per_holders_interval)

    table_data = dict(request_count_per_holders_interval)
    table_index_order = list(table_data)
    table_index_order.sort()
    table_series = pd.Series(table_data, index=table_index_order)
    #print(series)#,series.index,series.values)

    lablels = {'counter': 'Количество заявок', 'counter_freq':'Число интервалов, на которых наблюдалось это число заявок'}
    df_data = {lablels['counter']: table_series.index, lablels['counter_freq']: table_series.values}
    df = pd.DataFrame(data=df_data)
    df=df.set_index(lablels['counter'])
    print(df.T)

    from scipy.stats import poisson
    k = max(count_of_request)
    ni = list(table_series.values)
    mpi = [m*poisson.pmf(ki, mu) for ki in table_series.index]

    from hypothesis_testing.exp import ExpDistributionTest
    tester = ExpDistributionTest(params, tau_z)
    tester.description = "Н0 – с.в. etta(t0) распределена по закону Пуассона с параметром lambda*t0"
    tester.conclude(ni,mpi,k)