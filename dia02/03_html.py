#%%

import pandas as pd

URL = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
dfs = pd.read_html(URL, storage_options={"User-Agent": "Mozilla/5.0"})
dfs

#%%
df_uf = dfs[1]
df_uf.to_csv("Ufs.csv",sep=";", index=False)