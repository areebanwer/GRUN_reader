# Function for Square Distance
# Mohammad Areeb Anwer
from points_reader import PointsSet
from netcdf_reader import Data


def sqr_dist_lat(data_file_name, points_file_name, ix):
    """
        Function for calculating index of nearest latitude in Data to our point.
        :param data_file_name: STR - file name of Data netcdf file
        :param points_file_name: STR - file name of points excel file
        :param ix: INT- index of the point
        :return: Float - index of nearest lat in Data
    """

    # calling classes
    data_lat = Data(data_file_name)
    points_lat = PointsSet(points_file_name)

    # Squared difference of lat
    sq_dist_lat = (data_lat.get_lat_data_all() - points_lat.get_lat_search(ix)) ** 2

    # identifying the index of the minimum value for lat
    nearest_index_lat = sq_dist_lat.argmin()
    return float(nearest_index_lat)


def sqr_dist_lon(data_file_name, points_file_name, ix):
    """
        Function for calculating index of nearest longitude in Data to our point.
        :param data_file_name: STR - file name of Data netcdf file
        :param points_file_name: STR - file name of points excel file
        :param ix: INT- index of the point
        :return: Float - index of nearest lon in Data
    """
    # calling classes
    data_lon = Data(data_file_name)
    points_lon = PointsSet(points_file_name)

    # Squared difference of lon
    sq_dist_lon = (data_lon.get_lon_data_all() - points_lon.get_lon_search(ix)) ** 2

    # identifying the index of the minimum value for lon
    nearest_index_lon = sq_dist_lon.argmin()
    return nearest_index_lon



