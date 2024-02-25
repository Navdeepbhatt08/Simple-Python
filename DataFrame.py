import numpy as np
import pandas as pd

num_rows = 100
num_classes = 4

col1 = np.random.randint(0, num_classes, num_rows)
col2 = np.random.randint(0, num_classes, num_rows)
col3 = np.random.randint(0, num_classes, num_rows)
col4 = np.random.randint(0, num_classes, num_rows)

Data = pd.DataFrame(
    {
        'Column1':col1,
        'Column2':col2,
        'Column3':col3,
        'Column4':col4
    }
)
print(Data)