import pandas as pd
from pathlib import Path
import os


def cleaner(dataset):

    cleaned = dataset

    return cleaned


def processor(data):

    joined_data = pd.DataFrame()

    for state in data:

        path = str(Path('Data/' + state).resolve())

        df = pd.read_excel(path)

        cleaned_data = cleaner(df)

        joined_data = pd.concat(
            [
                joined_data, cleaned_data
            ]
        )

    return joined_data


def main():

    datapath = str(Path('Data').resolve())

    datalist = os.listdir(datapath)

    finaldata = processor(datalist)

    finaldata.to_csv('animal.csv')
