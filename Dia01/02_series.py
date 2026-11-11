#%%
idades = [
    32, 38, 30, 30, 31, 
    35, 35, 39, 31, 37,
    27, 23, 36, 33, 32
]

media = sum(idades) / len(idades)


diff = 0

for i in idades:
    diff+= (i - media) ** 2
    
variancia = diff / (len(idades)- 1)

print(media)
print(variancia)

#%%
import pandas as pd

series_idade = pd.Series(idades)
series_idade

#%%
media_idade = series_idade.mean()
var_idade = series_idade.var()
sumary = series_idade.describe()
sumary


#%%

