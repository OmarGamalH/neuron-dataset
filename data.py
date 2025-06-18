import pandas as pd


df = pd.read_csv("indexes/index_1.csv")

# df["steps"] = df[df["filename"].notna()]["filename"]

pd.options.display.max_rows = 103

print(df["weak_steps"])