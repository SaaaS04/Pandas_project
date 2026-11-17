#%%

import pandas as pd

idades = [
    32, 38, 30, 30, 31, 
    35, 35, 39, 31, 37,
    27, 23, 36, 33, 47,
]
nomes = [
    "Ana", "Bruno", "Carla", "Daniel",
    "Elena", "Felipe", "Gabriela", "Henrique",
    "Isabela","João","Larissa","Marcos",
    "Rabinos", "Otávio", "Patrícia"
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)
series_nomes

#%%
dados = {
    "nome": nomes,
    "idade": idades
}
df = pd.DataFrame(dados)
df
#%%

df.iloc[0]["nome"]

#%%
for i in df["idade"]:
    if i % 2 == 0:
        print(i)