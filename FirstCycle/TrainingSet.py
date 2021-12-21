import unittest
import pandas
import numpy
import torch
import fastai
from fastai.data.transforms import RandomSplitter
from fastai.tabular.core import add_datepart, FillMissing, Normalize, Categorify, TabularPandas
from fastcore.basics import range_of
import feather

# Create a dataframe
dfFirstCycle = pandas.read_csv(
    "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie/Predicting_Bike_Rental_Demand/Datasets/train.csv",
    low_memory=False, parse_dates=["datetime"])
# Calculate the log for each value in dependent variable "count"
# Each value in "rent_count" is being replaced by its log natural logarithm by defining the column a a variable and performing numpy.log on it
dfFirstCycle.rent_count = numpy.log(dfFirstCycle.rent_count)
# Use fastai function "add_datepart"
dfFirstCycle = add_datepart(dfFirstCycle, "datetime", drop=True)
# Split dfFirstCycle in half. The first 5443 rows are the training set, the second are the validation set.
dfFirstCycle_train, dfFirstCycle_validate = dfFirstCycle.iloc[:5443].copy(), dfFirstCycle.iloc[5443:].copy()
# Save dependent variable into an array
y_name_validation = dfFirstCycle_validate.rent_count
y_name_validation.to_csv(
    "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie/Predicting_Bike_Rental_Demand/FirstCycle/y_name_validation.csv")
# Drop dependent variable from the validation set
dfFirstCycle_validate.drop('rent_count', axis=1, inplace=True)
# Define categorical variables
cat_names = ['season', 'holiday', 'workingday', 'weather', 'datetimeIs_month_end', 'datetimeIs_month_start',
             'datetimeIs_quarter_end', 'datetimeIs_quarter_start', 'datetimeIs_year_end', 'datetimeIs_year_start']
# Define continuous variables
cont_names = ['temp', 'atemp', 'humidity', 'windspeed', 'casual', 'registered', 'rent_count']
# Clean the data: Transform the categorical variables to something similar to pd.Categorical. Fill the missing values in continuous columns. Turn values into normal distribution.
procs = [Categorify, FillMissing, Normalize]
# Define splits
splits = RandomSplitter()(range_of(dfFirstCycle_train))
trainingFirstCycle = TabularPandas(dfFirstCycle_train, procs, cat_names, cont_names, y_names="rent_count",
                                   splits=splits)
# Save dataframes into feather format
dfFirstCycle_train.to_feather(
    "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie/Predicting_Bike_Rental_Demand/FirstCycle/trainingFirstCycle.feather")

dfFirstCycle_validate.to_csv(
    "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie/Predicting_Bike_Rental_Demand/FirstCycle/validateFirstCycle.csv")

if __name__ == '__main__':
    unittest.main(verbosity=2)
