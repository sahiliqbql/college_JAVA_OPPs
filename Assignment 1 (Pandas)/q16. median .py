import numpy as np
import pandas as pd

random = np.random.randint(45,60,30)
weights = pd.DataFrame(random)

med = weights[0].median()
print(f"median = {med}")
