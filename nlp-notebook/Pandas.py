import pandas as pd
import numpy as np

fullData = pd.read_csv('unstructures.tsv', sep='\t', engine='python', skiprows=1)
# print(fullData.columns)  # Check the columns in the DataFrame
fullData['price'].value_counts() # no column price is found check if the column exists
fullData['price'] = pd.to_numeric(fullData['price'], errors='coerce')
fullData.dropna(subset=['price'], inplace=False)
# fullData['priceX2'] = fullData['price'].astype(int) * 2

dataframe = pd.DataFrame({
    "Date": fullData['date'],
    "Price": fullData['price'],
})
print(dataframe.head())