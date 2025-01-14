import numpy as np
import pandas as pd

random = np.random.randint(45,60,30)
weights = pd.DataFrame(random)

# weights[5]: This syntax is used for selecting a column
# in the DataFrame, not a row. Since weights has only one column
# (column 0 by default), the code will look for a column labeled 5,
# which doesn't exist. To select a row by its index, 
# you need to use .iloc[] for integer-based indexing.
    
item_at_5 = weights.iloc[5]
print(item_at_5)
