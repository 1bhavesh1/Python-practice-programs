# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:11:09 2020

@author: bhavesh
"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

#preparing dataset
dataset = pd.read_csv('C:\\Users\\bhavesh\\Documents\\datasets\\houseprices.csv')

reg = LinearRegression()
reg.fit(dataset[['Living Area','Bathrooms','Bedrooms','Age']],dataset.Price)

#regression_model_mse = mean_squared_error(dataset[['Living Area','Bathrooms','Bedrooms','Age']],dataset.Price)
#print('MSE : ', math.sqrt(regression_model_mse))
print('R squared value : ',reg.score(dataset[['Living Area','Bathrooms','Bedrooms','Age']],dataset.Price))

#plt.scatter(dataset[['Living Area','Bathrooms','Bedrooms','Age']],dataset.Price,color='green')
#plt.plot(dataset[['Living Area','Bathrooms','Bedrooms','Age']],reg.predict(dataset[['Living Area','Bathrooms','Bedrooms','Age']]),color='black')
#plt.show()

print(reg.predict([[3000,4,4,5]]))
