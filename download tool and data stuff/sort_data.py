import pandas as pd
#simply move the .csv from the output from scrapy in the same folder as this and have matching file names
df = pd.read_csv('output.csv')

df["charakter"] = df["charakter"].str.replace("?","", regex=False)
df["artist"] = df["artist"].str.replace("?","", regex=False)
df["charakter"] = df["charakter"].str[1:]
df["artist"] = df["artist"].str[1:]
df["rating"] = df["rating"].str.replace("Score:","", regex=False)
df["artist"] = df["artist"].str.replace("-","", regex=False)
df["charakter"] = df["charakter"].str.replace(",,",",", regex=False)
#df["charakter"] = df["charakter"].str.replace(" ",",", regex=False)


df.to_csv('sorted.csv')