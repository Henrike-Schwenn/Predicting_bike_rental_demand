import os
import numpy
import pandas

class CsvObject:

    def __init__(self, pathCsvDataset="Directory leading to a csv file", csvDataset="Csv file to be read"):
        self.pathCsvDataset = pathCsvDataset
        self.csvDataset = csvDataset

    def GetPath(self):
        return self.pathCsvDataset

    def SetPath(self, pathCsvDataset):
        self.pathCsvDataset = pathCsvDataset

    def GetDataset(self):
        return self.csvDataset

    def SetDataset(self, csvDataset):
        self.csvDataset = csvDataset


    def CreateDataframe(self):
        # Change to the directory which contains the csv file
        os.chdir(self.pathCsvDataset)
        # TODO Verify if the format is actually csv
        '''name, extension = os.path.splitext(self.pathCsvDataset)
           # If yes, proceed by creating a data frame with pd.readcsv()
           if extension == ".csv":
               pandas.read_csv(pathCsvDataset)
           else:
               print("Please select a .csv file")
           # If no, print error message: "Please select a .csv file"'''
        pandas.read_csv(self.csvDataset)

    # TODO Check further requirements to the class
    # TODO





TestDataframe = CsvObject("C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie/Predicting_Bike_Rental_Demand/CsvDataset", "Test_csv_file.csv")
TestDataframe.CreateDataframe()

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
