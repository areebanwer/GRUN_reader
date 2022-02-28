# PointSet Class
# Mohammad Areeb Anwer

import os
import pandas as pd


class PointsSet:
    def __init__(self, file_name="points.xlsx"):
        self.file_name = file_name
        self.points_data = pd.read_excel(self.file_name)
        self.lat_search = float
        self.lon_search = float

    def get_lat_search(self, index=int):
        """
            method for getting latitude of point to be searched
            :param index: INT - index of the dataframe
            :return: Float -  lat in dataframe
        """
        self.lat_search = self.points_data['Latitude'][index]
        return self.lat_search

    def get_lon_search(self, index=int):
        """
             method for getting longitude of point to be searched
             :param index: INT - index of the dataframe
             :return: Float - lon in dataframe
         """
        self.lon_search = self.points_data['Longitude'][index]
        return self.lon_search

    def __add__(self, value):
        """
            magic method for offsetting  the coordinates by a given value
            :param value: INT- amount of offset
            :return: Float - new lat and lon coordinates
        """
        self.lat_search += value
        self.lon_search += value
        return self.lat_search, self.lon_search

    def __call__(self, *args, **kwargs):
        # prints class structure information to console
        print("Class Info: <type> = PointsSet (%s)" % os.path.dirname(__file__))
        print(dir(self))

