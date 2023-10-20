import pandas as pd
import os
import urllib.request
from urllib.error import HTTPError

#df = pd.read_csv('sortiert.csv')
df = pd.read_csv(os.path.join(os.getcwd(), 'sortiert.csv'))
zahl = 0

while True:
    try:
        print("Von welchem Charakter willst du alles Runterladen? ichhassemich schreiben um ALLE runterzuladen")
        charakter = str(input())
        break
    except:
        print("error xd")

if charakter != "ichhassemich":
    download_dir = os.path.join(os.getcwd(), charakter)
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)

    print("Es gibt " + str(df["charakter"].str.contains(charakter).sum()) + " bilder mit diesen Charakter möchtest du sie runterladen?")
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
    print("BIST DU DIR SICHER? schreibe Ok")
    gestige_gesundheit = str(input())
    if gestige_gesundheit == "Ich liebe Züge":
        os.system('shutdown -s -t 0')
    if gestige_gesundheit == "Kys alle buttons bestätigen es sowiso" or "Ok":
        download_dir = os.path.join(os.getcwd(), "Ultimativer Flughafen")
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)
        for index,row in df.iterrows():
            try:
                url = row["bild"]
                print(url)
                dateiname = str(os.path.join(download_dir, "Flugzeug_") + str(zahl) + ".jpg")
                zahl += 1
                urllib.request.urlretrieve(url, (dateiname))
            except HTTPError as err:
                print("error xd")