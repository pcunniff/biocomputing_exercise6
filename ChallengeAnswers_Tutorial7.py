# Answers for Lecture 13 challenges

# 1
#create a list of 5 names
#always square brackets for lists
my_list=['Brittni','Chissa','Katie','Stuart','Amanda']
print my_list
#look at length of our list
len(my_list)
#indexing starts at 0
my_list[2]
# when range, up to but not including
my_list[0:2]


# 2
#make matrix using numpy, better print structure - looks like matrix
import numpy as np
mat=np.matrix('1,2;3,4')
print mat
#when calling a cell, always rows by columns 3
mat[1,0]
#make dictionary, always curly brackets, key value sep by :, set of key value sep by ,
b={'my_list':my_list,'mat':mat}
#call b want key index then value index
b['my_list'][3:5]
#can't do b[1][3:5] since dictionaries aren't ordered
b['mat'][0,1]

# 3
import pandas as pd
data=pd.read_csv('wages.csv',header=0,sep=",")
#gives rows by columns
data.shape
#gives first 5 rows
data.head()

#gives the 15th row
data.iloc[14,:]
# get a column by name
data.wage
# gives value for each column
data.min()
# get the minimun for only the wage
min(data.wage)

#find the max wage
max(data.wage)

#select the row that has the max wage
data[data.wage==max(data.wage)]
data[data['wage']==max(data.wage)]
