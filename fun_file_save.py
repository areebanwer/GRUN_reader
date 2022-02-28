# Function for saving data frame to excel
# Mohammad Areeb Anwer
import os
import pandas as pd


def file_save(df, filename):
    """
        Function for saving Dataframe to excelworkbook with filename and sheet name.
        :param df: Dataframe - to be saved in excel
        :param filename: STR - file name containing respective coordinates
        :output: save excel workbook with respective name
    """
    filename_xlsx = filename + ".xlsx"  # add extension to name
    writer = pd.ExcelWriter(os.path.abspath("..") + "\\GRUN_reader\\output\\" + filename_xlsx)
    df.to_excel(writer, 'Monthly')  # write sheet name
    writer.save()





