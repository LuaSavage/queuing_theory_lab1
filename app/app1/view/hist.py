from matplotlib import pyplot as plt
import numpy as np
from view.basic_analysis import BasicAnalyser
from hist_digits.digits import Digit

class HistPlot:

    def __init__(self, params) -> None:
        self.digit_handler = Digit(params)
        self.params = params
        self.analyser = BasicAnalyser(params).analyser

    def plot (self, z):

        y_sorted= self.params.y[:]
        y_sorted.sort()

        frequency_density = self.digit_handler.get_frequency_density(z)

        #new_z = z[1:]
        #sns.barplot(x = new_z, y = frequency_density)
        #plt.figure()

        fig, ax = plt.subplots()
        #plt.hist(y_sorted, density="true", bins = z, range=(min(self.params.y),max(self.params.y)), label=('Гистограмма f(x)'))
        plt.hist(y_sorted, density="true", bins = z, range = (min(self.params.y),max(self.params.y)), label=('Гистограмма f(x)'))
                      
        plot_range = np.arange(z[0],z[-1], 0.01)
        plot_y = [self.analyser.get_density_distribution(x) for x in plot_range]
        plt.plot(plot_range, plot_y, color='purple', linewidth=2, label=('f(x)'))

        fz = [(z[i+1]+z[i])/2 for i in range(len(z)-1)]
        plt.plot(fz, frequency_density, color="red",marker = "o",linewidth=0, markersize=3, label=('Плотности частоты f*'))
        ax.legend()
        plt.show()

        print("Мера похожести: ", self.digit_handler.get_measure_of_similarity(z))
