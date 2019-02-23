import pandas as pd
import numpy as np
csv = 'D:/task/output files/emaildf.csv'
dataset = pd.read_csv(csv)
dataset = np.array(dataset)
for row in dataset:
    print(row)