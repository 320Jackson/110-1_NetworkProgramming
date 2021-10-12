from numpy.lib.function_base import place
import pandas as pd
import numpy as np
NameList = []

for Run in range(0, 5):
    NameList.append(input())

PL = pd.Series(np.random.rand(5) * 100, NameList)
Math = pd.Series(np.random.rand(5) * 100, NameList)
English = pd.Series(np.random.rand(5) * 100, NameList)

Data = {
    "Programming Language" : PL,
    "Math" : Math,
    "English" : English
}
df = pd.DataFrame(Data)
print(df.max(), "\n", df.idxmax(), "\n")
print(df.mean())
print(df.median())