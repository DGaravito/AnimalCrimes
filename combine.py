import pandas as pd
from pathlib import Path
import os


def cleaner(dataset):

    cleaned = dataset

    return cleaned


def processor(data):

    joined_data = pd.DataFrame()
    data_list = []

    for state in data:

        path = str(Path('Data/' + state).resolve())

        df = pd.read_excel(path)

        cleaned_data = cleaner(df)

        data_list.append(cleaned_data)

        joined_data = pd.concat(
            [
                joined_data, cleaned_data
            ]
        )

    return joined_data, data_list


def main():

    datapath = str(Path('Data').resolve())

    datalist = os.listdir(datapath)

    finaldata_list = processor(datalist)

    finaldata_list[0].to_csv('animal.csv')

    n = 0

    for dataset in finaldata_list[1]:

        filename = datalist[n].strip('.xlsx') + '.csv'

        dataset.to_csv(filename)

        n += 1
