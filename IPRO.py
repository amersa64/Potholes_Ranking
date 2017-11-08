# Python 3
# coding: utf-8


import pandas as pd
import numpy as np
import googlemaps
import keys.py 

#this is mock algorithmm we probably gotta redefine it.
def the_almighty_algorithm(row):
    return 10*row['width']+5*row['length']+20*row['depth']+np.log(row['Traffic Density'])

def geocode():
    gmaps = googlemaps.Client(key=keys['binbin_gmap_api'])
    address = gmaps.reverse_geocode(('-87.629','41.878'))
    return print(address)

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

#main()
geocode()