

import pandas as pd
num=43
var="remada curvada"
dfInsert=pd.DataFrame()
dfInsert[var]=[num]
dfInsert["stiff"]=[56]

df=pd.read_csv("treinos.csv",sep=",")
print(df)
dfResul=pd.concat([df,dfInsert],ignore_index=True)
print(dfResul)
dfResul.to_csv("treinos.csv",index=False)