# with open("text.txt","r") as file:
#     content = file.read()
#     print(content)

# with open ("data.csv", "r") as file:
#     c = file.read()
#     print(c)

#     ##add new roww
#     with open("data.csv", "a") as obj:
#         obj.write("\nOla,50,Delta")

# import numpy as np
# data = np.genfromtxt("loan.csv", delimiter=",", usecols=8, filling_values=0)
# print(data)

# import numpy as np
# data = np.genfromtxt("data.csv", dtype=str, delimiter=",", usecols=[0])
#  ##TO print only names
# print(data)

with open("loan.csv","r") as file:
     data = file.read()
     

import numpy as np
data = np.genfromtxt("loan.csv", delimiter=",", usecols=8, filling_values=0)


#create1d
array = np.array(data)
#print(array)

#calculate mean
mean = np.mean(array)
#print(mean)

#calculate
median = np.median(array)
##print(median)

##std
std = np.std(array)
##print(std)

##max
max = np.max(array)
##print(max)

##min
min = np.min(array)
##print(array)

variance = np.var(array)
##print(variance)