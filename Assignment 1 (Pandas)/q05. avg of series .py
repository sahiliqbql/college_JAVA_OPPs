import numpy as np
import pandas as pd

random = np.random.randint(45,60,30)
weights = pd.DataFrame(random)

avg = weights.mean().values[0]
print(f"avg = {avg}")
