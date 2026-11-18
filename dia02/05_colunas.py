#%%

import pandas as pd
df = pd.read_csv("../data/transacoes.csv")
df

#%%
df.shape

#%%
df.info(memory_usage='deep')

#%%
df.dtypes

#%%
df.rename(columns={})
