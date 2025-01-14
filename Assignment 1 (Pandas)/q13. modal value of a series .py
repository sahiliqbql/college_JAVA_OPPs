import numpy as np
import pandas as pd

random = np.random.randint(45,60,30)
weights = pd.DataFrame(random)

mode_val = weights.mode().values[0]
print(mode_val)
