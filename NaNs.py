import pandas as pd
import numpy as np
df=pd.read_csv("train.csv")
df['LotFrontage'] = df['LotFrontage'].replace(np.nan, 0)
df = df.replace(np.nan, 0)
df.replace(np.nan, 0, inplace=True)
pfrint(df)


import pandas as pd 
df=pd.read_csv("train.csv")
lotFrontage= df[['LotFrontage']]
df = df.fillna(0)  
df.fillna(0, inplace=True)
print(df)