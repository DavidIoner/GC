from datetime import datetime

import pandas as pd
from pandas.core.frame import DataFrame

from uteis import *


def auto_complete():
    pass


def analisys():

    df = pd.read_excel("teste.xlsx")

    df["total"] = df["valores"] + df["produto"]

    # write the missing values in the xlsx file
    df.to_excel("teste.xlsx", index=False)

    print(df)


analisys()
