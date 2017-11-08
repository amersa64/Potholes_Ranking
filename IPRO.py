# Python 3
# coding: utf-8


import pandas as pd
import numpy as np
import googlemaps
import keys
import json

#this is mock algorithmm we probably gotta redefine it.
def the_almighty_algorithm(row):
    return 10*row['width']+5*row['length']+20*row['depth']+np.log(row['Traffic Density'])

#finds exact formatted street name based on gps longitude and latitude data
def geocode():
    gmaps = googlemaps.Client(key=keys.keys['binbin_gmap_api'])
    reversed_data = gmaps.reverse_geocode((40.714224, -73.961452),result_type='street_address')
    #print(reversed_data)
    formatted_address = json.dumps(reversed_data)
    #print(formatted_address)
    reloaded_address = json.loads(formatted_address)[0]
    return print(reloaded_address['formatted_address'])

def main():
    #generate Synthatic Data
    # np.random.rand(x,y) produces x rows and y columns of values from 0~1
    df2 = pd.DataFrame(np.random.rand(100, 4)*5,columns=['width', 'length', 'depth', 'Traffic Density'])

    df2['Traffic Density'] = np.random.rand(100,1)*2000// 1

    #save generic data to csv file
    df2.to_csv('Synthatic_Data.csv',sep=',',header=True,index=False)

    #load data from csv file
    data = pd.read_csv('Synthatic_Data.csv',index_col=False)

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
    return print('Success')

main()