
# coding: utf-8

# In[239]:

import pandas as pd
import numpy as np
from sodapy import Socrata


# ## DON'T RUN BELOW CELL

# In[253]:

#generate Synthatic Data
df2 = pd.DataFrame(np.random.rand(100, 3)*5,
                   columns=['width', 'length', 'depth'])
#save generic data to csv file
df2.to_csv('Synthetic_Data.csv',sep=',',header=True,index=False)


# In[240]:

#load data from csv file
pd.options.mode.chained_assignment = None  # default='warn' turn off warnings
data = pd.DataFrame()
def load_input_data():
    global data
    data = pd.read_csv('Input_data_Synthetic.csv',index_col=False)
    data.drop_duplicates(inplace=True)


# In[254]:

def get_traffic_density():
   

    global data
    
    # Unauthenticated client only works with public data sets. Note 'None'
    # in place of application token, and no username or password:
    client = Socrata("data.cityofchicago.org", None)

    # Example authenticated client (needed for non-public datasets):
    # client = Socrata(data.cityofchicago.org,
    #                  MyAppToken,
    #                  userame="user@example.com",
    #                  password="AFakePassword")

    # First 2000 results, returned as JSON from API / converted to Python list of
    # dictionaries by sodapy.
    results = client.get("u77m-8jgp", limit=10000)

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)
    results_df = results_df.convert_objects(convert_numeric=True)

    data = pd.merge(data, results_df, how='left', on=['latitude', 'longitude'])


# In[255]:

#this is mock algorithmm we probably gotta redefine it.
def the_almighty_algorithm(row):
    res = 5*row['width']+0.3*row['length']+ 20*row['depth']+np.log(row['total_passing_vehicle_volume'])
    return res


# In[262]:

#apply algorithm on data
def score():
    global data
    data['score'] = data.apply(lambda row: the_almighty_algorithm(row), axis=1)
    data['binned_score']= 'Urgent'
    data['binned_score'][data['score']<data['score'].quantile(q=0.80)]='Required'
    data['binned_score'][data.score<data.score.quantile(q=0.60)]='Priority'
    data['binned_score'][data.score<data.score.quantile(q=0.350)]='Recommended'
    data = data[['width', 'length', 'depth', 'latitude','longitude', 'score','binned_score', 'date_of_count', 'id', 'location', 'street','total_passing_vehicle_volume','traffic_volume_count_location_address','vehicle_volume_by_each_direction_of_traffic']]


# In[263]:

def __main():
    global data
    print("loading data....")
    load_input_data()
    data.head()
    print("Density Traffic info is being generated...")
    get_traffic_density()
    data.head()
    print("scoring....")
    score()
    #data = data.sort_values(by ='score',axis=0,ascending=False)
    data.head()


# In[264]:

__main()


# In[265]:

data.head(n=100)


# In[ ]:



