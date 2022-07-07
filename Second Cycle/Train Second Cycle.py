# Imports

import pandas
import numpy
import sklearn
from fastai.tabular.core import add_datepart, \
    FillMissing, Normalize, Categorify, TabularPandas
from sklearn.ensemble import RandomForestRegressor
import psutil
import time
import joblib

start = time.process_time_ns()

# Dataframe Training Set

train_path = ("C:/Users/henri/OneDrive/Dokumente/Berufseinstieg"
              "/Sprachtechnologie/Predicting_Bike_Rental_Demand/Datasets"
              "/train.csv")

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

training_second_cycle = TabularPandas(train_second_cycle, procs, cat_names,
                                      cont_names, y_names="rent_count")

# Train Random Forest Regressor

rf_2 = sklearn.ensemble.RandomForestRegressor()

rf_2.fit(train_second_cycle, train_second_cycle.rent_count)

# Save RF

rf_2_trained_path = ("C:/Users/henri/OneDrive/Dokumente/Berufseinstieg"
                     "/Sprachtechnologie/Predicting_Bike_Rental_Demand"
                     "/Second Cycle/rf_2_trained.joblib")

rf_2_trained = joblib.dump(rf_2, rf_2_trained_path, compress=3)

# Measure Performance

end = time.process_time_ns()
runtime = end - start

print("Time elapsed:", runtime, "nanoseconds")
print("RAM memory used:", psutil.virtual_memory()[2], "%")
