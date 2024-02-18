import pandas as pd
import os
import urllib.request
from urllib.error import HTTPError

#df = pd.read_csv('sortiert.csv')
df = pd.read_csv(os.path.join(os.getcwd(), 'sorted.csv'))
zahl = 0

while True:
    try:
        print("What Character do you want to donwload enter the name or type ALL to donwload everything")
        charakter = str(input())
        break
    except:
        print("error xd")

if charakter != "ALL":
    download_dir = os.path.join(os.getcwd(), charakter)
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)

    print("There are " + str(df["charakter"].str.contains(charakter).sum()) + " images with that character do you want to download?")
    entscheidung = str(input())
    if entscheidung == "Ok":
        
        df = df.dropna(subset=['charakter'])
        df_neu = df[df["charakter"].str.contains(charakter)]
        for index,row in df_neu.iterrows():
            try:
                url = row["bild"]
                print(url)
                dateiname = str(os.path.join(download_dir, charakter) + str(zahl) + ".jpg")
                zahl += 1
                urllib.request.urlretrieve(url, (dateiname))
            except HTTPError as err:
                print("error xd")

    else:
        exit()
else:
    print("Are you sure you want to that? y/n")
    gestige_gesundheit = str(input())
    if gestige_gesundheit == "Ich liebe Züge":
        os.system('shutdown -s -t 0')
    if gestige_gesundheit == "y":
        download_dir = os.path.join(os.getcwd(), "you asked for it lol")
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)
        for index,row in df.iterrows():
            try:
                url = row["bild"]
                print(url)
                dateiname = str(os.path.join(download_dir, "you_wanted_it_") + str(zahl) + ".jpg")
                zahl += 1
                urllib.request.urlretrieve(url, (dateiname))
            except HTTPError as err:
                print("error xd")