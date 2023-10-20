import pandas as pd
import os
import urllib.request
import pyautogui as pg
import webbrowser
from urllib.error import HTTPError
#df = pd.read_csv('sortiert.csv')
df = pd.read_csv(os.path.join(os.getcwd(), 'sortiert.csv'))
zahl = 0

while True:
    try:
        charakter = pg.prompt("Von welchem Charakter willst du alles Runterladen? ichhassemich schreiben um ALLE runterzuladen", title = "Another Happy Landing :D")
        break
    except:
        print("error xd")

if charakter != "ichhassemich":
    download_dir = os.path.join(os.getcwd(), charakter)
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)

    
    entscheidung = pg.confirm("Es gibt " + str(df["charakter"].str.contains(charakter).sum()) + " bilder mit diesen Charakter möchtest du sie runterladen?", title = "Another Happy Landing :D", buttons=['Ok', 'Nein ich heiße Rafi und hasse alles was gut ist'])
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
        pg.alert("kys nutte warum willst du die bilder nicht runterladen", title = "Another Happy Landing :D", button = 'Ok moment')
        exit()
else:
    gestige_gesundheit = pg.confirm("BIST DU DIR SICHER?", title = "Another Happy Landing :DDDDD", buttons=['Ok', 'Ich liebe Züge', 'Ich liebe Femboys', 'Kys alle buttons bestätigen es sowiso'])
    if gestige_gesundheit == "Ich liebe Züge":
        os.system('shutdown -s -t 0')
    if gestige_gesundheit == "Ich liebe Femboys":
        webbrowser.open('https://www.reddit.com/r/FemBoys/comments/1787u37/would_you_date_a_school_girl_with_a_cock/', new=0, autoraise=True)
    if gestige_gesundheit == "Kys alle buttons bestätigen es sowiso" or "Ok":
        download_dir = os.path.join(os.getcwd(), "Ultimativer Flughafen")
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)
        for index,row in df.iterrows():#
            try:
                url = row["bild"]
                print(url)
                dateiname = str(os.path.join(download_dir, "Flugzeug_") + str(zahl) + ".jpg")
                zahl += 1
                urllib.request.urlretrieve(url, (dateiname))
            except HTTPError as err:
                print("error xd")