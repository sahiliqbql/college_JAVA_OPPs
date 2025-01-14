import numpy as np
import pandas as pd

random = np.random.randint(45,60,30)
weights = pd.DataFrame(random)

sorted_in = weights.sort_values(by=0); #by for row wise 
print(sorted_in)
