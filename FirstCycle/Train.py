# Train Random Forest Regressor on dataframe trainingFirstCycle
import os
import psutil
import math
import time
import matplotlib.pyplot
import pandas
import sklearn
import fastai
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error
from sklearn.tree import export_graphviz
import plotly.express
import feather
import unittest

# Get the sum of the system and user CPU time of the current process in nanoseconds
# Nanoseconds since the epoch, which is 1 January 1601, 00:00:00 for Windows
# At the beginning of the process
start = time.process_time_ns()

# Read feather formatted trainingFirstCycle and define as array X_train.
# This is the training set
X_train = pandas.read_feather(
    "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/"
    "Sprachtechnologie/Predicting_Bike_Rental_Demand/FirstCycle/trainingFirstCycle.feather")
# Define X_train.rent_count as dependent variable Y_train.
# This is the dependent variable of the training set, the column to be predicted.
Y_train = X_train.rent_count
# Visualize X_train and Y_train in a scatterplot
# Some examples
# Season=X_train.plot.scatter(x="season", y="rent_count")
# Windspeed=X_train.plot.scatter(x="windspeed", y="rent_count")
# Humidity=X_train.plot.scatter(x="humidity", y="rent_count")
# Temperature=X_train.plot.scatter(x="temp", y="rent_count")

# Read csv formatted validateFirstCycle and define as array X_validate.
# This is the name of the validation set.
X_validate = pandas.read_csv(
    "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie"
    "/Predicting_Bike_Rental_Demand/FirstCycle/validateFirstCycle.csv")
# Read y_name_validation.csv and define as Y_validate.
# This is the dependent variable of the validation set, the column to be predicted.
Y_validate = pandas.read_csv(
    "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie"
    "/Predicting_Bike_Rental_Demand/FirstCycle/y_name_validation.csv")

# Create sklearn.ensemble.RandomForestRegressor() object
RF1 = sklearn.ensemble.RandomForestRegressor()
# Run fit method on training set
RF1.fit(X_train, Y_train)
# Visualize RF1.fit using export_graphviz
# https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html
# Extract a single tree from the forest
estimator = RF1.estimators_[5]
RF1_sample = sklearn.tree.export_graphviz(estimator,
                                          out_file="C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie"
                                                   "/Predicting_Bike_Rental_Demand/FirstCycle/RF1.dot")

# Predict y variable in test set.
y_pred = RF1.predict(X_validate)
# TODO Visualize prediction?
y_true = Y_validate.rent_count.to_numpy()

# Evaluate prediction using root mean squared log error
scoreRMSLE = math.sqrt(sklearn.metrics.mean_squared_log_error(y_true, y_pred))
# TODO Visualize score
# DataFrame.plot.scatter()
# matplotlib.scatter(x,y)

# Return further parameters

# Nanoseconds since the epoch
# At the end of the process
end = time.process_time_ns()
runtime = end - start

# Code runs fine up to this point.


print("Score RMSLE:", scoreRMSLE)
print("Time elapsed:", runtime, "nanoseconds")
print("RAM memory used:", psutil.virtual_memory()[2], "%")
# TODO Visualize parameters
# TODO Save all prints into a file
# Dashboard

if __name__ == '__main__':
    unittest.main(verbosity=2)
