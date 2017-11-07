
# coding: utf-8

# In[3]:

import pandas as pd
import numpy as np


# In[33]:

#generate Synthatic Data
df2 = pd.DataFrame(np.random.rand(100, 4)*5,columns=['width', 'length', 'depth', 'Traffic Density'])
df2['Traffic Density'] = np.random.rand(100,4)*2000// 1
#save generic data to csv file
df2.to_csv('Synthatic_Data.csv',sep=',',header=True,index=False)


# In[51]:

#load data from csv file
data = pd.read_csv('Synthatic_Data.csv',index_col=False)
data.drop_duplicates(inplace=True)


# In[53]:

#this is mock algorithmm we probably gotta redefine it.
def the_almighty_algorithm(row):
    return 5*row['width']+0.3*row['length']+20*row['depth']+np.log(row['Traffic Density'])


# In[55]:

#apply algorithm on data
data['score'] = data.apply(lambda row: the_almighty_algorithm(row), axis=1)


# In[69]:

#rank the data based on score by algorithm
print(data.sort_values(by ='score',axis=0,ascending=False).head())


# In[ ]:



