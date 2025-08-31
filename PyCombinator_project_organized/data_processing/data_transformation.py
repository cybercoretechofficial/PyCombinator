
import pandas as pd

# Simple data cleaning
def clean_data(data):
    df = pd.DataFrame(data)
    df = df.dropna()  # Remove missing values
    return df

data = {'name': ['Alice', 'Bob', None], 'value': [10, 20, 30]}
cleaned_data = clean_data(data)
print("Cleaned Data:")
print(cleaned_data)
