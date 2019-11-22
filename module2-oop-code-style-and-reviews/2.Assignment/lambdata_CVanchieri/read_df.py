"""
Helpers - A bit of helper code for pandas dataframe import.
"""
# import pandas library as pd.
import pandas as pd

# create a description title.
title = "A bit of helper code for pandas dataframe import"

# read in the LiverpoolFootballClub_all csv file.
df = pd.read_csv(
    'https://raw.githubusercontent.com/CVanchieri/LSDS-DataSets/master/EnglishPremierLeagueData/LiverpoolFootballClubData_EPL.csv')

# show the data frame shape.
# print('dataframe shape =', df.shape)
shape = df.shape
# show the data frame with headers.
# df.head()
