# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 13:16:28 2022

@author: pc
"""

#step 1: importing all the required libraries and classes


import pandas as pd  #to read csv files

import numpy as np  #used for working with arrays

import matplotlib.pyplot as plt  #for data visualization and graphical plotting library 

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

#step 2: Reading Data
df=pd.read_csv("Apple stock.csv")
df = df[['Total Trade Quantity','Turnover (Lacs)']] 
df.columns=['volume','turnover'] #rename columns

#devide data into dependant and independant features in arrays
x=np.array(df['volume']).reshape(-1,1) #independant variable
y=np.array(df['turnover'])  #dependant variable

#Spliting data into train and test
#30% testing , 70% training
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

#creat Model and fit it
model = LinearRegression()
model.fit(X_train, y_train)

#other way in one line

#model = LinearRegression().fit(X_train, y_train)


#The Actual vs Predicted Values
y_pred =model.predict(X_test) #predict response 

result = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

print(result)


#get the accuracy

print('The Accuracy of the Model: ', model.score(X_test, y_test))



#Visulization
plt.scatter(X_test,y_test,color='r')

plt.plot(X_test, y_pred ,color='k')
plt.title('volume vs turnover')
plt.xlabel('volume')
plt.ylabel('turnover')
plt.show()