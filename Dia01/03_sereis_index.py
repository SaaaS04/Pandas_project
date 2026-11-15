#%%
import pandas as pd

idades = [
    32, 38, 30, 30, 31, 
    35, 35, 39, 31, 37,
    27, 23, 36, 33, 47
]

series_idades = pd.Series(idades)
series_idades

#%%

idades[0]
#%%
series_idades[-1]
#%%
series_idades = series_idades.sort_values()
series_idades
