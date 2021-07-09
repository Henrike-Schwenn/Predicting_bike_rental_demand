import os
from typing import Any, Union

import numpy
import pandas

class CsvObject:

    def __init__(self, pathCsvDataset="Directory leading to a csv file", csvDataset="Csv file to be read", csvDataframe="Name of Dataframe"):
        self.pathCsvDataset = pathCsvDataset
        self.csvDataset = csvDataset
        self.csvDataframe = csvDataframe
        self.CreateDataframe()

    def CreateDataframe(self):
        os.chdir(self.pathCsvDataset)
        #TODO: Verify data format csv
        return self.csvDataframe == pandas.read_csv(self.csvDataset, low_memory=False)

    def GetPath(self):
        return self.pathCsvDataset

    def SetPath(self, pathCsvDataset):
        self.pathCsvDataset = pathCsvDataset

    def GetDataset(self):
        return self.csvDataset

    def SetDataset(self, csvDataset):
        self.csvDataset = csvDataset

    def GetDataframe(self):
        return self.csvDataframe

    def SetDataframe(self, csvDataframe):
        self.csvDataframe = csvDataframe


    # TODO Check further requirements to the class
    # TODO

TestTrainSet=CsvObject("C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie/Predicting_Bike_Rental_Demand/Datasets", "train.csv","testTrainingSet")
print(TestTrainSet.CreateDataframe())

"""Creates a dataset object from a csv file


What it's gonna do


- Get a csv file from a directory
        - Instance variable: "path-csv-dataset"
        - Instance variable: "csv-dataset-object"
        - get_dataset():
            os.chdir(path-csv-dataset)
    - Verify if the format is actually csv
        - If yes, proceed
        - If no, print error message: "Please select a .csv file"
- Return a file object
        - csv_object = get_dataset()
            - Name the object via raw input
            
- Display the object
    - display_dataset = read_csv()

**Needs:**

- os
- numpy
- pandas

**Instance variables:**

- path to data file
- name of data file

**Methods:**

- get_dataset = os.chdir(path)
- display_dataset = read_csv()"""

