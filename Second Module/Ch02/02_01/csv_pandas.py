"""Load & converting data from CSV using Pandas"""
import pandas as pd
import os

time_cols = ['tpep_dropoff_datetime', 'tpep_pickup_datetime']
os.chdir("C:\\Users\\kevin\\OneDrive\\Documents\\LinkedIn Learning\\Python for Data Science\\Second Module\\Ch02\\02_01")


def load_df(file_name):
    return pd.read_csv('taxi.csv.bz2', parse_dates=time_cols)


print(load_df('taxi.csv.bz2').head())


def iter_df(file_name):
    yield from pd.read_csv(
        'taxi.csv.bz2', parse_dates=time_cols, chunksize=100)


for i, df in enumerate(iter_df('taxi.csv.bz2')):
    if i > 10:
        break
    print(len(df))
