import os


class CsvObject:
    import os
    import sys
    import numpy
    import pandas

    path_csv_dataset = ""

    def __init__(self):
        self.path_csv_dataset = "Please insert a directory leading to a csv file. :)"

    def get_path_csv_dataset(self):
        print(os.chdir({0}.format(self.path_csv_dataset)))
        #TODO AttributeError: 'set' object has no attribute 'format'
        #Change to the directory which contains the csv file
        #Print directory
        #Verify if the format is actually csv
        #TODO Insert splitext() to check if file extension is .csv
        #If yes, proceed by creating a data frame with pd.readcsv()
        #TODO Insert pd.readcsv()
        #If no, print error message: "Please select a .csv file"


TestDataframe = CsvObject()
TestDataframe.path_csv_dataset = "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie/Prediciting_Bike_Rental_Demand/Class csv dataset/Test_csv_file.csv"
TestDataframe.get_path_csv_dataset()

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
