import numpy as np
import pandas as pd

data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 6, 7, np.nan, 9],
    'C': [10, 11, 12, np.nan, 14],
    'D': [np.nan, np.nan, np.nan, np.nan, np.nan]
}
df = pd.DataFrame(data)

df_dropped = df.dropna()

df_filled = df.fillna(0)

df_mean_filled = df.fillna(df.mean())

df_median_filled = df.fillna(df.median())

df_ffilled = df.ffill()

df_bfilled = df.bfill()

print("Original DataFrame:")
print(df)

print("\nDataFrame after removing rows with missing values:")
print(df_dropped)

print("\nDataFrame after filling missing values with 0:")
print(df_filled)

print("\nDataFrame after filling missing values with column means:")
print(df_mean_filled)

print("\nDataFrame after filling missing values with column medians:")
print(df_median_filled)

print("\nDataFrame after forward filling missing values:")
print(df_ffilled)

print("\nDataFrame after backward filling missing values:")
print(df_bfilled)
