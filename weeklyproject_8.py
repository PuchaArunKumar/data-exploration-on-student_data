import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Load the Dataset into DataFrame
data = pd.read_csv('student1.csv')
#Explore Datatypes
print(data.dtypes)
#Explore Value Ranges and Distinct Values
for col in data.select_dtypes(include=[np.number]):
    print(f" {col}  Range: {data[col].min()} - {data[col].max()}")
for col in data.select_dtypes(include=[object]):
    print(f"{col}  Distinct values: {data[col].unique()}")

#Explore Data Distribution 
data.hist(figsize=(10, 6))# Numerical columns
plt.tight_layout()
plt.show()
# Handle missing values
data = data.dropna()

#Explore Relationships Between Columns
def handle_conversion(data):
    string_cols = data.select_dtypes(include=[object]).columns
    for col in string_cols:
        try:
            data[col] = pd.to_numeric(data[col], errors='coerce')
        except:
            print(f"Error converting '{col}' column. Dropping it.")
            data.drop(col, axis=1, inplace=True)
    return data
data = handle_conversion(data.copy())
data = pd.get_dummies(data, drop_first=True)
correlation = data.corr()
print(correlation)

# Rank all the features that would determine the Overall grade
if 'Overall Grade' in correlation.columns:
    sorted_features = correlation['Overall Grade'].abs().sort_values(ascending=False).index[1:]
    print("Features ranked by absolute correlation with 'Overall Grade':")
    for feature in sorted_features:
        print(f"- {feature} (correlation: {correlation['Overall Grade'][feature]})")
else:
    print("'Overall Grade' column not found in the dataset.")
