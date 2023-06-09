from datetime import datetime
import pandas as pd
import requests
import urllib
def generate_rq_payload(n_page: int) -> str:
    """Generate a rq payload that consists

    Args:
        n_page (int): _description_

    Returns:
        str: _description_
    """
    rq_payload = (
        '{"page":' + str(n_page) + ',"limit":30,"srt":"metascore","direct":"desc","type":"","my":0,"myarchive":0,"fav":0,"getdecks":{"hascrd":[],"nothascrd":[],"youtube":0,"archetype":0,"supertype":"","smartsrch":"","pool":4,"date":"","collection":""}}')

    return rq_payload

def extract() -> pd.DataFrame:
    decks_url = 'https://marvelsnap.pro/snap/do.php?cmd=getdecks&rq=' + generate_rq_payload(n_page=1)


    decks_response = requests.get(decks_url)
    decks_data = decks_response.json()
    df = pd.DataFrame(decks_data)
    df["dateCollected"] = datetime.utcnow()
    return df

if __name__ == "__main__":
    print(extract())