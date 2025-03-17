import pandas as pd


def load_raw_data():
    raw_data = pd.read_csv("data/aita_clean.csv")
    return raw_data
