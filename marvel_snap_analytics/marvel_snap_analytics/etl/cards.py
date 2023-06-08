from datetime import datetime
import pandas as pd
import requests

def extract() -> pd.DataFrame:
    cards_url = "https://static2.marvelsnap.pro/snap/do.php?cmd=getcards"
    cards_data = requests.get(cards_url).json()
    df = pd.DataFrame(cards_data).T.reset_index(drop=True)
    df["dateCollected"] = datetime.utcnow()
    return df

if __name__ == "__main__":
    print(extract())