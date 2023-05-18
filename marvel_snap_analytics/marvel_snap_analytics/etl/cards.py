import pandas as pd
import requests

def extract() -> pd.DataFrame:
    cards_url = "https://marvelsnap.io/api/search.php?database&type=character"
    cards_data = requests.get(cards_url).json()
    return pd.DataFrame(cards_data)