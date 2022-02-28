# This is main.py
# Mohammad Areeb Anwer
import os
import numpy as np
import pandas as pd
import datetime
from datetime import datetime, timedelta
from points_reader import PointsSet
from netcdf_reader import Data
from fun_sqr_dist import sqr_dist_lat
from fun_sqr_dist import sqr_dist_lon
from fun_file_save import file_save
from fun_analysis import annual_average
from fun_analysis import annual_maximum
from fun_logger import *


@log_actions
def main():
    data_path = os.path.abspath("..") + "\\GRUN_reader" + "\\GRUN_v1_GSWP3_WGS84_05_1902_2014.nc"  # save Netcdf file path
    points_path = os.path.abspath("..") + "\\GRUN_reader" + "\\points.xlsx" # save points file path
    points = PointsSet(points_path)  # Instance of PointSet class
    data = Data(data_path)  # Instance of Data class
    df_points = points.points_data  # Saving points as a DataFrame

    for point in df_points.index:  # loop for each point in index
        logging.info("PROCESSING FOR LAT {0} AND LON {1}"
                     .format(str(df_points["Latitude"][point]), str(df_points["Longitude"][point])))

        nearest_lat_index = sqr_dist_lat(data_path, points_path, point)  # function to get index of nearest lat in data
        nearest_lon_index = sqr_dist_lon(data_path, points_path, point)  # function to get index of nearest lon in dat
        nearest_lat = data.get_nearest_lat(nearest_lat_index)  # function to get nearest lat in Data
        nearest_lon = data.get_nearest_lon(nearest_lon_index)  # function to get nearest lon in Data

        logging.info("FOUND NEAREST POINT IN DATA WITH LAT {0} AND LON {1}"
                     .format(str(nearest_lat), str(nearest_lon)))

        months = data.get_months_data()  # Get array containing number of months
        date_range = []  # empty list
        start_date = datetime.strptime(data.get_start_date_str(), "%Y-%m-%d")
        for month in months:  # loop for adding months to starting date
            date_monthly = start_date + timedelta(days=month)
            date_range.append(date_monthly)

        df_monthly = pd.DataFrame(0, columns=['Runoff'], index=date_range)  # Empty Dataframe for storing runoff with dates

        mons = np.arange(0, months.size)  # array with size equal to the number of months in Data

        for m in mons:  # loop to store runoff values in dataframe
            df_monthly.iloc[m] = data.get_runoff_data(m, nearest_lat_index, nearest_lon_index)

        # filename in Variable according to lat  and lon
        filename = '{}_{}_runoff'.format(nearest_lat, nearest_lon)

        file_save(df_monthly, filename)  # function to save dataframe in excel
        annual_average(df_monthly, filename)  # function to calculate annual average and plot graph
        annual_maximum(df_monthly, filename)   # function to calculate annual maximum and plot graph


if __name__ == '__main__':
    main()
