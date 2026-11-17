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

#%%
series_idades[7]

#%%

series_idades.iloc[0]

#%%
series_idades.iloc[-1]

#%%

series_idades.iloc[:3]

#%%

idades = [
    32, 38, 30, 30, 31, 
    35, 35, 39, 31, 37,
    27, 23, 36, 33, 47
]

indexs = [
    "Ana", "Bruno", "Carla", "Daniel",
    "Elena", "Felipe", "Gabriela", "Henrique",
    "Isabela","João","Larissa","Marcos",
    "Natália", "Otávio", "Patrícia"
]

series_idades = pd.Series(idades, index = indexs)
series_idades

#%%
series_idades.loc["Larissa"]