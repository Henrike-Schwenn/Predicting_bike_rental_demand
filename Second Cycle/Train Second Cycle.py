# Imports

import pandas
import numpy
import torch
import fastai
from fastai.data.transforms import RandomSplitter
from fastai.tabular.core import add_datepart, \
    FillMissing, Normalize, Categorify, TabularPandas
from fastcore.basics import range_of

# Dataframe Training Set

train_path = "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie"
    "/Predicting_Bike_Rental_Demand/Datasets/train.csv"

train_second_cycle = pandas.read_csv(
    train_path, low_memory=False, parse_dates=["datetime"])

train_second_cycle = add_datepart(train_second_cycle, "datetime", drop=True)

train_second_cycle.rent_count = numpy.log(train_second_cycle.rent_count)

cat_names = ['season', 'holiday', 'workingday', 'weather',
             'datetimeIs_month_end', 'datetimeIs_month_start',
             'datetimeIs_quarter_end', 'datetimeIs_quarter_start',
             'datetimeIs_year_end', 'datetimeIs_year_start']

cont_names = ['temp', 'atemp', 'humidity', 'windspeed', 'casual', 'registered',
              'rent_count']

procs = [Categorify, FillMissing, Normalize]


# Train Random Forest Regressor
# Save RF
# Measure Performance
