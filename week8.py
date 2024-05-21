import numpy as np
import pandas as pd

# Load the datasets
d1 = pd.read_csv("student-mat.csv", sep=";")
d2 = pd.read_csv("student-por.csv", sep=";")

# Define the columns to merge on
merge_columns = ["school", "sex", "age", "address", "famsize", "Pstatus", 
                 "Medu", "Fedu", "Mjob", "Fjob", "reason", "nursery", "internet"]

# Merge the datasets
df = pd.merge(d1, d2, on=merge_columns, suffixes=('_mat', '_por'))
df.to_csv('student1.csv')