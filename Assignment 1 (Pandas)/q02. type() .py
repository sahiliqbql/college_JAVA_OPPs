import numpy as np
import pandas as pd

random = np.random.randint(45,60,30)
weights = pd.DataFrame(random)

dtype = type(weights)

print(dtype)  # Check the type