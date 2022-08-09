# Train Random Forest Regressor on dataframe trainingFirstCycle
import psutil
import math
import time
import pandas
import sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.tree import export_graphviz
import unittest

'''Get the sum of the system and user CPU time of the current
 process in nanoseconds.
Nanoseconds since the epoch, which is 1 January 1601, 00:00:00 for Windows
at  the beginning of the process'''
start = time.process_time_ns()

# Read feather formatted trainingFirstCycle and define as array x_train.
# This is the training set

train_path = (
    "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/"
    "Sprachtechnologie/Predicting_Bike_Rental_Demand/"
    "FirstCycle/trainingFirstCycle.feather")

test_path = (
    "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie"
    "/Predicting_Bike_Rental_Demand/FirstCycle/testingFirstCycle.csv")

y_test_path = ("C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/"
               "Sprachtechnologie/Predicting_Bike_Rental_Demand/"
               "FirstCycle/y_name_validation.csv")

x_train = pandas.read_feather(train_path)

'''Define x_train.rent_count as dependent variable y_train.
This is the dependent variable of the training set, the column to be 
predicted.'''
y_train = x_train.rent_count

'''Read csv formatted testingFirstCycle and define as array x_test.
This is the name of the test set.'''
x_test = pandas.read_csv(test_path)

'''Read y_name_test.csv and define as y_test.
This is the dependent variable of the test set, the column to be predicted.'''
y_test = pandas.read_csv(y_test_path)

# Create sklearn.ensemble.RandomForestRegressor() object
RF1 = sklearn.ensemble.RandomForestRegressor()

# Run fit method on training set
RF1.fit(x_train, y_train)

# Visualize RF1.fit using export_graphviz
# https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html
# Extract a single tree from the forest
estimator = RF1.estimators_[5]
RF1_sample = sklearn.tree.export_graphviz(estimator,
                                          out_file="C:/Users/henri/OneDrive/"
                                                   "Dokumente/Berufseinstieg/"
                                                   "Sprachtechnologie"
                                                   "/Predicting_Bike_Rental_Demand/"
                                                   "FirstCycle/RF1.dot")

# Predict y variable in test set.
y_pred = RF1.predict(x_test)

y_true = y_test.rent_count.to_numpy()

# Evaluate prediction using root mean squared log error
scoreRMSLE = math.sqrt(sklearn.metrics.mean_squared_log_error(y_true, y_pred))


'''Saving as csv is not worth it: too much effort for a file that I couldn't
upload to Kaggle anyway, because I used the wrong dataset for testing.'''

# Return further parameters

# Nanoseconds since the epoch
# At the end of the process
end = time.process_time_ns()
runtime = end - start

print("Score RMSLE:", scoreRMSLE)
print("Time elapsed:", runtime, "nanoseconds =", runtime*0.000000001, "seconds")
print("RAM memory used:", psutil.virtual_memory()[2], "%")
# TODO Visualize parameters
# TODO Save all prints into a file
# Dashboard

if __name__ == '__main__':
    unittest.main(verbosity=2)
