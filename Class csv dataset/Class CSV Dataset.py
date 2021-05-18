import os


class CsvObject:
    import os
    import sys
    import numpy
    import pandas

    def __init__(self, pathCsvDataset=r"Please insert a directory leading to a csv file. :)"):
        self.pathCsvDataset = pathCsvDataset

    def GetPath(self):
        return self.pathCsvDataset

    def SetPath(self, pathCsvDataset):
        self.pathCsvDataset = pathCsvDataset

    def __str__(self):
        return "{0}".format(self.pathCsvDataset)

    def CreateDataframe(self):
        os.chdir(self.pathCsvDataset)

        # Change to the directory which contains the csv file
        # Print directory
        # TODO AttributeError: 'set' object has no attribute 'format'
        # Verify if the format is actually csv
        name, extension = os.path.splitext(self.pathCsvDataset)
        # If yes, proceed by creating a data frame with pd.readcsv()
        if extension == ".csv":
            pandas.read_csv(pathCsvDataset)
        else:
            print("Please select a .csv file")
        # If no, print error message: "Please select a .csv file"


TestDataframe = CsvObject(r"C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie/Prediciting_Bike_Rental_Demand/Class csv dataset/Test_csv_file.csv")
# TODO Make Python accept the directory!
    # TODO Try deleting the blanks, rename folder "Class csv dataset"
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
