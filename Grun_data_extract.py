# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 10:08:27 2021

@author: AnwerM
"""

import netCDF4
from netCDF4 import Dataset
import numpy as np
import pandas as pd
import datetime 
from datetime import datetime, timedelta
import array 

# Reading in the netCDF file
data = Dataset(r'C:\Study\w21\python\GRUN_reader\GRUN_v1_GSWP3_WGS84_05_1902_2014.nc')

# Diplaying the name of the variables
# =============================================================================
# print(data.variables.keys())
# =============================================================================

# Accessing the variables
#lon = data.variables['lon']
# =============================================================================
# print(lon)
# =============================================================================


#lat = data.variables['lat']
# =============================================================================
# print(lat)
# 
# =============================================================================
#time = data.variables['time']
# =============================================================================
# print(time)
# =============================================================================

#Runoff = data.variables['Runoff']
# =============================================================================
# print(Runoff)
# =============================================================================

# Accessing the data from the varibles
#time_data = data.variables['time'][:]

#
lon_data = data.variables['lon'][:]
# =============================================================================
# print(lon_data)
# =============================================================================

lat_data = data.variables['lat'][:]
# =============================================================================
# print(lat_data)
# =============================================================================
#

#saving points in csv as df
points_df = pd.read_csv('points.csv')#name of file

for point in points_df.index:
    
    #Storing the lat and lon of required point into varialbes
    lat_required =  points_df['Latitude'][point]
    lon_required =  points_df['Longitude'][point]
    
    
    
    
    #Squared difference of lat and lon
    sq_dist_lat = (lat_data - lat_required)**2
    sq_dist_lon = (lon_data - lon_required)**2
    
    # identifying the index of the minimum value for lat and lon
    min_index_lat = sq_dist_lat.argmin()
    min_index_lon = sq_dist_lon.argmin()
    
    #Getthing the coordinates of the pont from with the value is retrieved
    lat_in_data = data.variables['lat'][min_index_lat]
    lon_in_data = data.variables['lon'][min_index_lon]
    
    print(lat_data.dtype)
    print(lat_required.dtype)
    #Runoff variable
    monthly_runoff = data.variables['Runoff']
    
    
    
    # Creating an empty pandas dataframe
    starting_date = data.variables['time'].units[11:21] #14 and 24 represent the index of date in time varaible
    starting_date_temp = datetime.strptime(starting_date, "%Y-%m-%d") #to convert string to date format

    #array of time
    time_data = data.variables['time'][:]

    #empty list
    date_range = []
    date_correct  =[]

    for d in time_data: #for adding the numbers of the days to the starting date
        date_correct = starting_date_temp + \
                             timedelta(days = d)
        date_range.append(date_correct)
        
    df = pd.DataFrame(0, columns = ['Monthly_Runoff'], index = date_range)
    
    dt = np.arange(0,data.variables['time'].size)


    for time_index in dt:
        print(time_index)
        print(min_index_lat)
        print(min_index_lon)
        df.iloc[time_index] = monthly_runoff[time_index,min_index_lat,min_index_lon]
        print(monthly_runoff[time_index,min_index_lat,min_index_lon])

        #print(monthly_runoff[time_index,min_index_lat,min_index_lon])
    # #file name
    #
    # filename = '{}_{}_monthly_runoff'.format(lat_in_data, lon_in_data)
    #
    # #saving time series into csv
    # df.to_csv(filename +'.csv')



