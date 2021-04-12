import os
import sys
import numpy
import pandas

class csv_object:

    # Get a csv file from a directory
    #TODO: Check syntax error. Something wrong the name of the variable path-csv-dataset?
    def get_csv_dataset(self, path-csv-dataset = "Insert a directory"):
        print(os.chdir("Insert a directory".format(path-csv-dataset))

TestDataframe=csv_object()
TestDataframe.get_csv_dataset(self, path-csv-dataset="/home/henrike/Dokumente/GitHub/Predicting_bike_rental_demand")


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