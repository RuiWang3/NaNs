# NaNs
import pandas as pd 
df=pd.read_csv("train.csv")
alley= df[['Alley']]
df = df.groupby(df.columns, axis = 1).transform(lambda x: x.fillna(x.mean()))
print(df)

import pandas as pd
df=pd.read_csv("train.csv")
df["LotArea"].fillna(df.groupby("Alley")["LotArea"].transform("mean"), inplace=True)
print(df)
