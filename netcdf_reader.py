# Data Class
# Mohammad Areeb Anwer
import os
from netCDF4 import Dataset


class Data:
    def __init__(self, netcdf_file_name="GRUN_v1_GSWP3_WGS84_05_1902_2014.nc"):
        self.netcdf_data = Dataset(netcdf_file_name)
        self.lat_data_all = []
        self.lon_data_all = []
        self.nearest_lat = float
        self.nearest_lon = float
        self.monthly_runoff = float
        self.start_date_str = str
        self.months_data = []

    def get_lat_data_all(self):
        """
            method for getting array containing latitudes in netcdf file
            :return: Array - of latitudes
        """
        self.lat_data_all = self.netcdf_data.variables['lat'][:]
        return self.lat_data_all

    def get_lon_data_all(self):
        """
            method for getting array containing longitudes in netcdf file
            :return: Array - of longitudes
        """
        self.lon_data_all = self.netcdf_data.variables['lon'][:]
        return self.lon_data_all

    def get_nearest_lat(self, nearest_index_lat):
        """
            method for latitude of the respective index in netcdf file
            :param nearest_index_lat: INT - index of the latitude
            :return: Float - nearest lat in Data
        """
        self.nearest_lat = self.netcdf_data.variables['lat'][nearest_index_lat]
        return self.nearest_lat

    def get_nearest_lon(self, nearest_index_lon):
        """
            method for longitude of the respective index in netcdf file
            :param nearest_index_lon: INT - index of the latitude
            :return: Float - nearest lat in Data
        """
        self.nearest_lon = self.netcdf_data.variables['lon'][nearest_index_lon]
        return self.nearest_lon

    def get_runoff_data(self, month_index, nearest_index_lat, nearest_index_lon):
        """
            method for longitude of the respective index in netcdf file
            :param nearest_index_lon: INT - index of the latitude
            :return: Float - index of nearest lat in Data
        """
        self.monthly_runoff = self.netcdf_data.variables['Runoff'][month_index, nearest_index_lat, nearest_index_lon]
        return self.monthly_runoff

    def get_months_data(self):
        """
            method for getting the array of months
            :return: Array - containing number of months in netcdf
        """
        self.months_data = self.netcdf_data.variables['time'][:]
        return self.months_data

    def get_start_date_str(self):
        """
            method for getting starting date of netcdf data
            :return: STR - start date
        """
        self.start_date_str = self.netcdf_data.variables['time'].units[11:21]
        return self.start_date_str

    def __add__(self, value):
        """
            magic method for offsetting  the coordinates by a given value
            :param value: INT- amount of offset
            :return: Float - new lat and lon coordinates
        """
        self.nearest_lat += value
        self.nearest_lon += value
        return self.nearest_lat, self.nearest_lon



    def __call__(self, *args, **kwargs):
        # prints class structure information to console
        print("Class Info: <type> = Data (%s)" % os.path.dirname(__file__))
        print(dir(self))
