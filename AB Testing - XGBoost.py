#!/usr/bin/env python
# coding: utf-8

# In[136]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

from xgboost import XGBRegressor

import xgboost as xgb
from sklearn.metrics import accuracy_score
 


# In[137]:


control_path ="C:/Users/lenovo/Desktop/Data/Personal projects/A-B Testing/Data/control_data.csv"
experiment_path="C:/Users/lenovo/Desktop/Data/Personal projects/A-B Testing/Data/experiment_data.csv"

control_data = pd.read_csv(control_path)
experiment_data = pd.read_csv(experiment_path)

control_data.info()
# In[138]:


control_data.head()


# In[139]:


experiment_data.info()


# In[140]:


experiment_data.head()


# In[141]:


#Missing Values
control_data.isnull().sum()


# In[142]:


experiment_data.isnull().sum()


# In[143]:


#We join the two tables(Control and Experiments in one table)
data_total = pd.concat([control_data, experiment_data])
data_total.sample(10)


# In[144]:


np.random.seed(7)

# Create a Day of Week feature
data_total['DOW'] = data_total['Date'].str.slice(start=0, stop=3)

# Remove missing data
data_total.dropna(inplace=True)

# Add a binary column Experiment to denote
# if the data was part of the experiment or not (Random)
data_total['Experiment'] = np.random.randint(2, size=len(data_total))

# Remove missing data
data_total.dropna(inplace=True)

# Remove Date and Payments columns
del data_total['Date'], data_total['Payments']

# Shuffle the data
data_total = sklearn.utils.shuffle(data_total)


# In[145]:


# Reorder the columns 
data_total = data_total[['Experiment', 'Pageviews', 'Clicks', 'DOW', 'Enrollments']]
# Check the new data
data_total.head()


# In[146]:


# Splitting the data
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(data_total.loc[:, data_total.columns != 'Enrollments'],                                                    data_total['Enrollments'], test_size=0.2)


# In[147]:


# Converting strings to numbers
from sklearn.preprocessing import LabelEncoder

lb = LabelEncoder()
X_train['DOW'] = lb.fit_transform(X_train['DOW'])
X_test['DOW'] = lb.transform(X_test['DOW'])


# In[148]:


X_train.head()


# In[149]:


X_test.head()


# In[ ]:





# In[150]:


plt.style.use('ggplot')
get_ipython().run_line_magic('matplotlib', 'inline')

def plot_preds(y_test, y_preds, model_name):
    N = len(y_test)
    plt.figure(figsize=(10,5))
    original = plt.scatter(np.arange(1, N+1), y_test, c='blue')
    prediction = plt.scatter(np.arange(1, N+1), y_preds, c='red')
    plt.xticks(np.arange(1, N+1))
    plt.xlabel('# Oberservation')
    plt.ylabel('Enrollments')
    title = 'True labels vs. Predicted Labels ({})'.format(model_name)
    plt.title(title)
    plt.legend((original, prediction), ('Original', 'Prediction'))
    plt.show()
    
    


# In[152]:


#Model XgBoost
DM_train = xgb.DMatrix(data=X_train,label=y_train)
DM_test = xgb.DMatrix(data=X_test,label=y_test)


# In[153]:


parameters = {
    'max_depth': 6,
    'objective': 'reg:linear',
    'booster': 'gblinear',
    'n_estimators': 1000,
    'learning_rate': 0.2,
    'gamma': 0.01,
    'random_state': 7,
    'subsample': 1.
}


# In[154]:


xg_reg = xgb.train(params = parameters, dtrain=DM_train, num_boost_round=8)
y_preds = xg_reg.predict(DM_test)


# In[155]:


calculate_metrics(y_test, y_preds)


# In[156]:


plot_preds(y_test, y_preds, 'XGBoost')

