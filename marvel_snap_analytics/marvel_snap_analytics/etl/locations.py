import pandas as pd
import requests

def extract() -> pd.DataFrame:
    cards_url = "https://marvelsnap.io/api/search.php?database&type=location"
    cards_data = requests.get(cards_url).json()["card"]
    return pd.DataFrame(cards_data)

if __name__ == "__main__":
    print(extract())