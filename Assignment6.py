# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 11:17:16 2018

@author: Patrick
"""

#NUMBER 1
#usage: head(file_name,number_of_lines_you_want_to_return)
import pandas as pd
def head(file_name,num_lines):
    data = pd.read_csv(file_name, header=0, sep=",")
    x = data.iloc[0:num_lines,:]
    print (x)
    return x
head('wages.csv',5)

#NUMBER 2
#Last two rows of last two columns
data=pd.read_csv("iris.csv", header=0,sep=',')
a = data.T.tail(2)
z=a.T.tail(2)
print(z)

#Number of Observations for each species
b=data.iloc[:,4]
unique = b.unique()
c = b.to_csv()
for x in unique:
    d= c.count(x)
    print (x, ": ", d)
    
#Rows with sepal width >3.5
data.columns = ['Sepal_length', 'Sepal_width', 'Petal_length', 'Petal_width', 'Species']
wide_sepals = data[data.Sepal_width > 3.5]
print (wide_sepals)

#Write data for setosa to CSV file named setosa.csv
setosa = data[data.Species == 'setosa']
save = setosa.to_csv()
saving = open('setosa.csv','w')
saving.write(save)
saving.close()

#Calculate mean, minimum, and maximum of Petal.Length for observations from virginica
virginica = data[data.Species == 'virginica']
petal_lengths = virginica.iloc[:,2]
mean = petal_lengths.mean()
print ('mean: ', mean)
minimum = petal_lengths.min()
print ('minimum: ', minimum)
maximum = petal_lengths.max()
print ('maximum: ', maximum)