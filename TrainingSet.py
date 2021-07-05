import sys

sys.path.append(
    "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie/Predicting_Bike_Rental_Demand/CsvDataset")
import CsvDataset.ClassCSVDataset

print("Huch!")
TrainingSet = CsvDataset.ClassCSVDataset.CsvObject(
    "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie/Predicting_Bike_Rental_Demand/Datasets",
    "train.csv", "trainingSet")
print(TrainingSet.__class__)
TrainingSet.CreateDataframe()
