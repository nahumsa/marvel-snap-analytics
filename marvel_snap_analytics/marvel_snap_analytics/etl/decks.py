from datetime import datetime
import pandas as pd
import requests
import urllib

def extract() -> pd.DataFrame:

    page = 1

    decks_url = 'https://marvelsnap.pro/snap/do.php?cmd=getdecks&rq=' + f'{"page":{page},"limit":30,"srt":"metascore","direct":"desc","type":"","my":0,"myarchive":0,"fav":0,"getdecks":{"hascrd":[],"nothascrd":[],"youtube":0,"archetype":0,"supertype":"","smartsrch":"","pool":4,"date":"","collection":""}}'



    decks_response = requests.get(decks_url)
    decks_data = decks_response.json()
    df = pd.DataFrame(decks_data)
    df["dateCollected"] = datetime.utcnow()
    return df

if __name__ == "__main__":
    print(extract())