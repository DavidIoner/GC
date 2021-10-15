from datetime import datetime

import pandas as pd

# df = r"planilhas/test.xlsx"

date = datetime.today().strftime("%Y-%m-%d")

df = pd.DataFrame(columns=["data", "produto", "preco"])
df.to_excel("manilha.xlsx", index=False)
