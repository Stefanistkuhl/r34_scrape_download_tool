import pandas as pd

df = pd.read_csv('unsortiert.csv')

df["charakter"] = df["charakter"].str.replace("?","", regex=False)
df["artist"] = df["artist"].str.replace("?","", regex=False)
df["charakter"] = df["charakter"].str[1:]
df["artist"] = df["artist"].str[1:]
df["rating"] = df["rating"].str.replace("Score:","", regex=False)
df["artist"] = df["artist"].str.replace("-","", regex=False)
df["charakter"] = df["charakter"].str.replace(",,",",", regex=False)
#df["charakter"] = df["charakter"].str.replace(" ",",", regex=False)


df.to_csv('sortiert.csv')