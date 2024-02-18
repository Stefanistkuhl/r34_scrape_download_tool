import pandas as pd
import os
import urllib.request
import pyautogui as pg
import webbrowser
from urllib.error import HTTPError
#df = pd.read_csv('sortiert.csv')
df = pd.read_csv(os.path.join(os.getcwd(), 'sorted.csv'))
zahl = 0

while True:
    try:
        charakter = pg.prompt("What Character do you want to donwload enter the name or type ALL to donwload everything", title = "Amazing Download Tool")
        break
    except:
        print("error xd")

if charakter != "ALL":
    download_dir = os.path.join(os.getcwd(), charakter)
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)

    
    entscheidung = pg.confirm("There are " + str(df["charakter"].str.contains(charakter).sum()) + " Images with that Character you want to download them?", title = "Amazing Download Tool", buttons=['Yes', 'No'])
    if entscheidung == "Yes":
        
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
        pg.alert("Why wouldnt you wanna do that lol", title = "Amazing Download Tool", button = 'Ok moment')
        exit()
else:
    gestige_gesundheit = pg.confirm("Are you sure?", title = "Amazing Download Tool", buttons=['Yes', 'I love Trains', 'I love Femboys', 'Kys all buttons confirm it anyway'])
    if gestige_gesundheit == "I love trains":
        os.system('shutdown -s -t 0')
    if gestige_gesundheit == "Ich liebe Femboys":
        for i in range (69):
            webbrowser.open('https://youtu.be/dQw4w9WgXcQ?si=UkaaG4ZudxCTcH97', new=0, autoraise=True)
    if gestige_gesundheit == "Kys all buttons confirm it anyway" or "Yes":
        download_dir = os.path.join(os.getcwd(), "You asked for it")
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)
        for index,row in df.iterrows():#
            try:
                url = row["bild"]
                print(url)
                dateiname = str(os.path.join(download_dir, "you_asked_for_it_") + str(zahl) + ".jpg")
                zahl += 1
                urllib.request.urlretrieve(url, (dateiname))
            except HTTPError as err:
                print("error xd")