import numpy as np
data = np.genfromtxt("loan.csv", delimiter=",", usecols=8, filling_values=0)
print(data)

#create1d
array = np.array(data)
print(array)

#calculate mean
mean = np.mean(array)
print(mean)

#calculate
median = np.median(array)
print(median)

##std
std = np.std(array)
print(std)

