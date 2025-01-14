import numpy as np
import pandas as pd

random = np.random.randint(45,60,30)
weights = pd.DataFrame(random)

max = weights.max().values[0]
min = weights.min().values[0]

print(f"max = {max}")
print(f"min = {min}")
