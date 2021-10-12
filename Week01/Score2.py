import pandas as pd
import csv
with open('score.csv', encoding="UTF-8") as csvfile:
    df = pd.DataFrame(pd.read_csv(csvfile, index_col="Name"))
    df = df.reindex(columns=df.columns.tolist().append("avg"))
    df["avg"] = df.mean(axis=1)
    print(df.sort_values("avg", ascending=False)[:3:])

    print(df.max(), df.idxmax())