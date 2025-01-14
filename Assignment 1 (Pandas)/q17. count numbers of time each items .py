import numpy as np
import pandas as pd

random = np.random.randint(45,60,30)
weights = pd.DataFrame(random)

item_count = weights.value_counts()
print(item_count)
