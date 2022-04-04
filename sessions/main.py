# from sys import path
# path.append("..")
import pandas as pd
from utils import greetings
import os

other = - 1

def preprocess_text(dataframe: pd.DataFrame, other:int=10) -> pd.DataFrame:
    """
    apply text transform to news data
    """
    dataframe["news"] = dataframe["news"].apply(lambda string: string.split(".")[0])
    dataframe["close"] += other
    return dataframe

def main():
    """
    this is the main function
    """
    folder = "../other"
    for file in os.listdir(folder):
        if file.endswith(".csv"):
            df = pd.read_csv(f"{folder}/{file}")
            analyse(df)

    preprocess_text(df)



main()