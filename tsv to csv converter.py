import pandas as pd
dfs = pd.read_csv('data.tsv', sep='\t', chunksize=50)
for df in dfs:
    df.to_csv('file.csv', sep=',', mode='a')