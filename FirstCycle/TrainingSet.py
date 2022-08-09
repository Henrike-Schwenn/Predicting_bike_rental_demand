import unittest
import pandas
import numpy
from fastai.data.transforms import RandomSplitter
from fastai.tabular.core import add_datepart, \
    FillMissing, Normalize, Categorify, TabularPandas
from fastcore.basics import range_of

# Create a dataframe

df_path = ("C:/Users/henri/OneDrive/Dokumente/Berufseinstieg"
           "/Sprachtechnologie/Predicting_Bike_Rental_Demand/"
           "Datasets/train.csv")

df_first_cycle = pandas.read_csv(
    df_path, low_memory=False, parse_dates=["datetime"])

df_first_cycle = add_datepart(df_first_cycle, "datetime", drop=True)

'''Calculate the log for each value in dependent variable "count"
Each value in "rent_count" is being replaced by its log natural logarithm by
 defining the column a a variable and performing numpy.log on it'''
df_first_cycle.rent_count = numpy.log(df_first_cycle.rent_count)

# Split train_first_cycle in half.
# The first 5443 rows are the training set, the second are the test set.
df_first_cycle_train, df_first_cycle_test = df_first_cycle.iloc[
                                            :5443].copy(), df_first_cycle.iloc[
                                                           5443:].copy()
# Save dependent variable into an array
y_name_test = df_first_cycle_test.rent_count
y_name_test.to_csv(
    "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie"
    "/Predicting_Bike_Rental_Demand/FirstCycle/y_name_test.csv")

# Drop dependent variable from the test set
df_first_cycle_test.drop('rent_count', axis=1, inplace=True)

# Define categorical variables
cat_names = ['season', 'holiday', 'workingday', 'weather',
             'datetimeIs_month_end', 'datetimeIs_month_start',
             'datetimeIs_quarter_end', 'datetimeIs_quarter_start',
             'datetimeIs_year_end', 'datetimeIs_year_start']

# Define continuous variables
cont_names = ['temp', 'atemp', 'humidity', 'windspeed', 'casual', 'registered',
              'rent_count']

'''Clean the data: Transform the categorical variables to something 
similar to pd.Categorical.
Fill the missing values in continuous columns.
Turn values into normal distribution.'''
procs = [Categorify, FillMissing, Normalize]

# Define splits
splits = RandomSplitter()(range_of(df_first_cycle_train))
trainingFirstCycle = TabularPandas(df_first_cycle_train, procs, cat_names,
                                   cont_names, y_names="rent_count",
                                   splits=splits)

# Save dataframes
df_first_cycle_train.to_feather(
    "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/"
    "Sprachtechnologie/Predicting_Bike_Rental_Demand/FirstCycle/"
    "trainingFirstCycle.feather")

df_first_cycle_test.to_csv(
    "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg"
    "/Sprachtechnologie/Predicting_Bike_Rental_Demand/FirstCycle"
    "/testingFirstCycle.csv")

if __name__ == '__main__':
    unittest.main(verbosity=2)
