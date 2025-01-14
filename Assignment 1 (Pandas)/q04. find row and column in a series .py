import numpy as np
import pandas as pd

random = np.random.randint(45,60,30)
weights = pd.DataFrame(random)

row = weights.shape[0]
column = weights.shape[1]

print(f"row = {row}")
print(f"column = {column}")
