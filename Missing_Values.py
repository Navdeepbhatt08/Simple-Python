import pandas as pd
import numpy as np 

from sklearn.datasets import fetch_california_housing
california_housing=fetch_california_housing()
x=california_housing.data
feature_names=california_housing.feature_names
df=pd.DataFrame(data=x,columns=feature_names)
nan_indices=np.random.choice(df.index,size=int(0.1*df.size),replace=False)
rows,cols=np.unravel_index(nan_indices,df.shape)
df.values[rows,cols]=np.nan
missing_values_per_column=df.isnull().sum()
print("missing values in each column:")
print(missing_values_per_column)