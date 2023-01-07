# -*- coding: utf-8 -*-

# Libraries to help with reading and manipulating data
import pandas as pd
import numpy as np

# Libaries to help with data visualization
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Code to ignore warnings from function usage
import warnings;
import numpy as np
warnings.filterwarnings('ignore')

calgary = pd.read_csv('https://api.apify.com/v2/datasets/a4oH2fbnk6BrH7xEE/items?attachment=true&clean=true&format=csv')
# Copying data to another variable to avoid any changes to original data
data = calgary.copy()

data.head()

data.drop(data.iloc[:, 18:78], inplace=True, axis=1)

data.info()

data.drop(data.columns[[0,1,2,3,5,9,11,12,13,19,21]], inplace=True, axis=1)
data.head()

data.shape

data.rename(columns={'price':'Price','bathrooms':'Bathrooms','bedrooms':'Bedrooms','homeType':'Hometype','address/streetAddress':'Address','address/zipcode':'ZipCode','datePostedString':'DatePosted','livingArea':'Area','yearBuilt':'YearBuilt', 'latitude':'Latitude','longitude':'Longitude'}, inplace=True)
data.head()

data.info()

data['Region'] = data.Address.apply(lambda x: 'North East' if 'NE'or '' in x else('North West' if 'NW' in x else('South East' if 'SE' in x else ('South West' if 'SW' in x else x ))))
data['DatePosted'] = pd.to_datetime(data['DatePosted'], format='%Y-%m-%d')
data['YearBuilt'] = pd.to_datetime(data['YearBuilt'], format='%Y')
data.head()

data.to_csv('calgaryre.csv',index=False)

data['Price'].describe().transpose()

# let's plot all the price to look at its distributions
plt.figure(figsize = (7, 4))
sns.histplot(data = data, x = data['Price'], kde = True)
plt.show()