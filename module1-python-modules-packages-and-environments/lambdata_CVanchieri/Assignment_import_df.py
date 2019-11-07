# import pandas library.
import pandas as pd

# create a version #.
__version__ = "0.0.1"

# create a description.
Title = "read in the 'LPFC' LiverPool Football Club data set."

# read in the data set url.
LPFC = pd.read_csv(
    'https://raw.githubusercontent.com/CVanchieri/LSDS-DataSets/master/EnglishPremierLeagueData/LiverpoolFootballClubData_EPL.csv')

# show the data frame shape.
Shape = LPFC.shape
