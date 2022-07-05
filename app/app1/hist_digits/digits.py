import math
import numpy as np
import scipy

from view.basic_analysis import BasicAnalyser as analysers

class Digit:

    def __init__(self, params) -> None:
        self.params = params

    def get_sturges_digit_count (self):
        m = 1.44*math.log(self.params.n) + 1
        return math.ceil(m)

    def get_sturges_digit_length(self):
        m = self.get_sturges_digit_count ()
        mean_length = max(self.params.y)/m
        return mean_length

    def get_digits_by_count (self, count):
        hist = np.histogram(self.params.y, density="true", bins = count, range=(0,max(self.params.y)))
        return list(hist[1])  

    def get_digits_with_equal_length (self, length):    
        m = int(max(self.params.y)/length)
        return self.get_digits_by_count (m)

    def get_digit_length (self, z, i):    
        count = 0
        for y_i in self.params.y:
            if y_i>=z[i] and y_i<z[i+1]:
                count = count + 1
        return count

    def get_digit_count (self, z):
        return len(z)-1

    def get_frequency_density (self, z):       
        frequency_density = []
        for i in range(len(z)-1):
            delta_i = z[i+1]-z[i]
            density = self.get_digit_length(z,i)/(self.params.n*delta_i)
            frequency_density.insert(i,float(density))

        return frequency_density
        
    def get_measure_of_similarity(self, z): 
        deviations = []        
        frequency_density = self.get_frequency_density(z)

        basic_analyser = analysers(self.params).analyser

        for i in range(len(z)-1):
            average_z = (z[i] + z[i+1])/2
            deviation = (basic_analyser.get_density_distribution(average_z) - frequency_density[i])**2
            deviations.append(deviation)

        return sum(deviations)

class SturgesDigits(Digit):

    def __init__(self, params) -> None:
        super().__init__(params) 

    def get(self):
        return self.get_digits_by_count (self.get_sturges_digit_count())

class EqualHeightDigits(Digit):
 
    def __init__(self, params) -> None:
        super().__init__(params) 

    def get(self):
        z = self.get_digits_by_count (self.get_sturges_digit_count())
        
        y_sorted = self.params.y[:]
        y_sorted.sort()
        np_hist = np.histogram(y_sorted, bins = self.get_sturges_digit_count(), range=(0,max(self.params.y)))
        
        height = list(np_hist[0])
        height_median = scipy.median(height)
        
        h_i = 0
        z_i = 1

        while h_i <len(height):
            if height[h_i]>height_median:
                half = (z[z_i]-z[z_i-1])/2
                z.insert(z_i,z[z_i]-half)
                z_i+=2
            elif height[h_i]<height_median:
                if z_i <(len(z)-1):
                    z.pop(z_i)
            else:
                z_i+=1
            h_i+=1
        
        return z

class ApproximatelyEqualHeightDigits(Digit):

    def __init__(self, params) -> None:
        super().__init__(params) 

    def get(self):
        z = [0]
        m = int(input("Введите количество разрядов: " ))
        y_sorted = (self.params.y[:])
        y_sorted.sort()
        
        mean_height = int(len(self.params.y)/m)
        
        for y_i in y_sorted:
            i = y_sorted.index(y_i)
            if (i+1)-((len(z)-1)*mean_height) >= mean_height:
                #print(mean_height,(i+1)-((len(z)-1)*mean_height))
                z.append(y_sorted[i])
            
            if len(z)>m:
                break

        return z

class ManualDigits(Digit):

    def __init__(self, params) -> None:
        super().__init__(params) 

    def get(self):
        z = [0]
        print("max(y)=",max(self.params.y),"z1=0")
        print("Введите границы разрядов.\nВвод будет продолжаться до превышения вводимым числом max(y)")
        
        while z[-1] < max(self.params.y):
            z.append(float(input("Введите следующую границу разряда: " )))        
        return z
