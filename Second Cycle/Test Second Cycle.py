# Imports

import time
import joblib
import pandas
import numpy
import psutil
from fastai.tabular.core import add_datepart
from pandas import Series

start = time.process_time_ns()

# Dataframe Test Set without y

test_path = ("C:/Users/henri/OneDrive/Dokumente/Berufseinstieg"
              "/Sprachtechnologie/Predicting_Bike_Rental_Demand/Datasets"
              "/test.csv")

test_second_cycle = pandas.read_csv(
    test_path, low_memory=False)


# Save column "datetime" for submission

datetime=Series.to_numpy(test_second_cycle.datetime)


test_second_cycle = add_datepart(test_second_cycle, "datetime", drop=True)

# Run Random Forest Regressor

rf_2_trained_path = ("C:/Users/henri/OneDrive/Dokumente/Berufseinstieg"
                     "/Sprachtechnologie/Predicting_Bike_Rental_Demand"
                     "/Second Cycle/rf_2_trained.joblib")

rf_2_trained = joblib.load(rf_2_trained_path)

y_pred = rf_2_trained.predict(test_second_cycle)

# Export y_pred into csv

submission = numpy.column_stack((datetime,y_pred))

df_submission = pandas.DataFrame(submission, columns=["datetime", "count"])

submission_file = df_submission.to_csv("C:/Users/henri/OneDrive/Dokumente/"
                                  "Berufseinstieg/Sprachtechnologie/"
                                  "Predicting_Bike_Rental_Demand"
                     "/Second Cycle/Submission.csv")

# Measure Performance

end = time.process_time_ns()
runtime = end - start

print("Time elapsed:", runtime, "nanoseconds")
print("RAM memory used:", psutil.virtual_memory()[2], "%")