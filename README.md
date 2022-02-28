# GRUN_reader
GRUN NetCDF dataset to excel

## Background
This project is developed as a course project for the course "Python Programming for Water Resources Engineering and Research" taught by [Dr.Sebastian Schwindt](https://www.iws.uni-stuttgart.de/institut/team/Schwindt/) at the [University of Stuttgart](https://www.warem.uni-stuttgart.de/).

## Objective
GRUN_reader is designed to read through a very large dataset for global runoff and produce an output in the form of Excel workbook for a set of points.
GRUN_reader also calculates annual averages and annual maximum values along with their scatter plots for the given monthly runoffs.

## What is GRUN dataset?

GRUN is a global gridded monthly reconstruction of runoff covering the period from 1902 to 2014. In situ streamflow observations are used to train a machine learning algorithm that predicts monthly runoff rates based on antecedent precipitation and temperature from an atmospheric reanalysis. The accuracy of this reconstruction is assessed with cross-validation and compared with an independent set of discharge observations for large river basins. The presented dataset agrees on average better with the streamflow observations than an ensemble of 13 state-of-the art global hydrological model runoff simulations. We estimate a global long-term mean runoff of 38 452 km3 yr−1 in agreement with previous assessments. The temporal coverage of the reconstruction offers an unprecedented view on large-scale features of runoff variability in regions with limited data coverage, making it an ideal candidate for large-scale hydro-climatic process studies, water resource assessments, and evaluating and refining existing hydrological models.

The [Data description paper](https://essd.copernicus.org/articles/11/1655/2019/) can be read for details regarding GRUN dataset.

## What is NetCDF?
NetCDF (network Common Data Form) is a file format for storing multidimensional scientific data (variables) such as temperature, humidity, pressure, wind speed, and direction.

For more information about netCDF, explore the resources hosted by the [UCAR Unidata project](https://www.unidata.ucar.edu/software/netcdf/)      

## Code Overview
The object-oriented code uses custom classes that call within a **main.py** script. Additional scripts are created, which contain the custom classes and functions.

* **netcdf_reader.py** Contains a *Data* class to read netCDF dataset class information as structured objects.
* **points_reader.py** Contains a *PointsSet* to read points in Excel workbook information as structured objects.
* **fun_sqr_dist.py** contains function to calculating the index of the nearest point in dataset
* **fun_file_save.py** contains function to save dataframe to Workbook with point's name
* **fun_analysis.py** Contains functions for calculating annual average runoff, annual maximum runoff and plot scatter plots
* **fun_logger.py** Contains logging function

The following UML diagram shows the flow of the programme:
![git](https://github.com/areebanwer/GRUN_reader/blob/53c638c22df7659ac28128d37475f12648cfa658/uml.jpg)

## Getting Started

### Download Repository

To get the programme script the repository for the GRUN_reader needs to downloaded.

Cloning the exercise repository:

```
git clone https://github.com/areebanwer/GRUN_reader.git
```                                 
### Input Data

#### GRUN netCDF Dataset

1. Dowload the GRUN dataset from the [ETH Zürich Reseach Collection Page](https://www.research-collection.ethz.ch/handle/20.500.11850/324386)
2. Unzip the file in the same **GRUN_reader** repository folder
3. Make sure name of the file is "GRUN_v1_GSWP3_WGS84_05_1902_2014.nc"

#### Points Excel Workbook
1. Open the  given file **points.xlsx** in the same **GRUN_reader** folder
2. Enter the points for which runoff data is to retrieved in worksheet, Latitude and Longitude in the respective colums
3. Make sure only number values are entered.

### Dependencies
Following libraries are used by the programme:
* os
* numpy
* pandas
* datetime
* netCDF4
* matplotlib
* openpyxl
* logging

#### Installing netCDF4
Once you have installed Anaconda, open an Anaconda Prompt (e.g.Terminal/CMD) and enter the following command:
```
conda install -c anaconda netcdf4
```
To pip-install netCDF4 in any other virtual environment tap:
```
pip install netCDF4
```

## Running the Script

Run the **main.py** in terminal (e.g., Linux Terminal, PyCharm’s Terminal tab at the bottom of the window, or in Atom using platformio-ide-terminal).
Make sure to change the directory to **GRUN_reader** folder directory.

```
C:\GRUN_reader\ python main.py
```

## Output

The programme stores the Excel workbooks for each point in the **output** folder with in the **GRUN_reader**.
With in the workbooks there are three sheets, namely:
1. Monthly: Monthly Runoff from the GRUN Dataset for the given coordinate.
2. Annual_avg: Annual average runoff along with scatter plot is calculated
3. Annual_max: Annual maximum runoff along with scatter plot is calculated

**Note:** When the output workbooks are opened it gives an error and asks to repair the file. Press **Yes** to access the workbook.


## GUI

Orignaly GUI was planned to be used for running the programme but we were unable to connect the GUI with the main script.
The GUI file is part of the repository as **gui.py**


## Contributors

* **Tlanezi Martinez**  
* **Mohammad Areeb Anwer**



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
