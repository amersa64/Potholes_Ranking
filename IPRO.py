# Python 3
# coding: utf-8


import pandas as pd
import numpy as np
import googlemaps
import keys
import json
from sodapy import Socrata
import pprint as pp

#this is mock algorithmm we probably gotta redefine it.
def the_almighty_algorithm(row):
    return 10*row['width']+5*row['length']+20*row['depth']+40*row['traffic density']

#finds exact formatted street name based on gps longitude and latitude data
def geocode(latitude, longitude):
    gmaps = googlemaps.Client(key=keys.keys['binbin_gmap_api'])
    reversed_data = gmaps.reverse_geocode((latitude,longitude),result_type='street_address')
    #print(reversed_data)
    address_dump = json.dumps(reversed_data)
    #print(formatted_address)
    formatted_address = json.loads(address_dump)[0]
    return pp.pprint(formatted_address)

def location_to_traffic_density():
    reloaded_address['formatted_address']
    pass

def socrata():
    from sodapy import Socrata
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
    #results_df = pd.DataFrame.from_records(results)
    #results_df = results_df.convert_objects(convert_numeric=True)
    return results

def main():
    #generate Synthatic Data
    # np.random.rand(x,y) produces x rows and y columns of values from 0~1
    df2 = pd.DataFrame(np.random.rand(100, 6)*5,columns=['width', 'length', 'depth','longitude','latitude','traffic density'])

    df2['traffic density'] = np.random.randint(1,2000,(100,1))
    df2['longitude'] = np.random.uniform(-180,180,(100,1))
    df2['latitude'] = np.random.uniform(-90,90,(100,1))
    #save generic data to csv file
    df2.to_csv('synthetic_data.csv',sep=',',header=True,index=False)

    #load data from csv file
    data = pd.read_csv('synthetic_data.csv',index_col=False)

    #remove duplicates, may want to do something else with this
    data.drop_duplicates(inplace=True)

    #apply algorithm on dat
    data['score'] = data.apply(lambda row: the_almighty_algorithm(row), axis=1)

    #output filtered data to csv file
    #data.to_csv('filtered_data.csv',sep=',',header=True,index=False)
 
    #rank the data based on score by algorithm
    sorted_data = data.sort_values(by ='score',axis=0,ascending=False)

    #output sorted data to csv file
    sorted_data.to_csv('sorted_data.csv',sep=',',header=True,index=False)

    #get the dataset about street density from socrata into a csv file called socrata_street_density
    street_density_socrata = socrata()
    
    results_df = pd.DataFrame.from_records(street_density_socrata)
    results_df = results_df.convert_objects(convert_numeric=True)
    results_df.to_csv('socrata_street_density.csv', sep=',', header = True, index = False)
    return print('Success')

main()
#socrata()