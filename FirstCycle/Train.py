# Train Random Forest Regressor on dataframe trainingFirstCycle
import pandas
import sklearn
import fastai
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
import feather
import unittest

# Read feather formatted trainingFirstCycle and define as array X_train. This is the training set
X_train = pandas.read_feather(
    "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie/Predicting_Bike_Rental_Demand/FirstCycle/trainingFirstCycle.feather")
# Define X_train.rent_count as dependent variable Y_train. This is the dependent variable of the training set, the column to be predicted.
Y_train = X_train.rent_count
# Read csv formatted evalidateFirstCycle and define as array X_validate. This is the name of the validation set.
X_validate = pandas.read_csv(
    "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie/Predicting_Bike_Rental_Demand/FirstCycle/validateFirstCycle.csv")
# Read y_name_validation.csv and define as Y_validate. This is the dependent variable of the validation set, the column to be predicted.
Y_validate = pandas.read_csv(
    "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie/Predicting_Bike_Rental_Demand/FirstCycle/y_name_validation.csv")
# Create sklearn.ensemble.RandomForestRegressor() object
RF1 = sklearn.ensemble.RandomForestRegressor()
# TODO Run fit method on training set
RF1.fit(X_train, Y_train)
# TODO Run print_score function on training and validation sets
'''Where does print_score access X_validate and Y_validate, exactly? Or is it this method that takes care of the 
splitting into training and validation sets automatically, so I wouldn't have needed to do that in the first place? '''
x1=RF1.predict(X_validate)
print(x1)
# TODO Return parameters

if __name__ == '__main__':
    unittest.main(verbosity=2)
