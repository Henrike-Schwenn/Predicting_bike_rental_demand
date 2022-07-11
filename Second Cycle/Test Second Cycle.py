# Imports

import time
import joblib
import numpy
import pandas
import psutil
from fastai.tabular.core import add_datepart


start = time.process_time_ns()

# Dataframe Test Set without y

test_path = ("C:/Users/henri/OneDrive/Dokumente/Berufseinstieg"
              "/Sprachtechnologie/Predicting_Bike_Rental_Demand/Datasets"
              "/test.csv")

test_second_cycle = pandas.read_csv(
    test_path, low_memory=False, parse_dates=["datetime"])

test_second_cycle = add_datepart(test_second_cycle, "datetime", drop=True)

# Dataframe Test Set y

test_y_path = ("C:/Users/henri/OneDrive/Dokumente/Berufseinstieg"
              "/Sprachtechnologie/Predicting_Bike_Rental_Demand/Datasets"
              "/test_y.csv")

test_y_second_cycle = pandas.read_csv(
    test_y_path, low_memory=False, parse_dates=["datetime"])

test_y_second_cycle = add_datepart(test_y_second_cycle, "datetime", drop=True)

test_y_second_cycle.rent_count = numpy.log(test_y_second_cycle.rent_count)

# Run Random Forest Regressor

rf_2_trained_path = ("C:/Users/henri/OneDrive/Dokumente/Berufseinstieg"
                     "/Sprachtechnologie/Predicting_Bike_Rental_Demand"
                     "/Second Cycle/rf_2_trained.joblib")

rf_2_trained = joblib.load(rf_2_trained_path)

y_pred = rf_2_trained.predict

# Measure Performance

end = time.process_time_ns()
runtime = end - start

print("Time elapsed:", runtime, "nanoseconds")
print("RAM memory used:", psutil.virtual_memory()[2], "%")