"""Load rides data from XML"""

import bz2
import xml.etree.ElementTree as xml # Standard library in Python

import pandas as pd
import os

os.chdir("C:\\Users\\kevin\\OneDrive\\Documents\\LinkedIn Learning\\Python for Data Science\\Second Module\\Ch02\\02_02")
# Data conversions
conversion = [ # Define variable types
    ('vendor', int),
    ('people', int),
    ('tip', float),
    ('price', float),
    ('pickup', pd.to_datetime),
    ('dropoff', pd.to_datetime),
    ('distance', float),
]


def iter_rides(file_name): # Iterate through each "row"
    with bz2.open(file_name, 'rt') as fp:
        tree = xml.parse(fp) # Convert file information to XML tree

    rides = tree.getroot() # Store tree root in a variable to iterate each element
    for elem in rides:
        record = {}
        for tag, func in conversion:
            text = elem.find(tag).text
            record[tag] = func(text)
        yield record # Return each record one at a time


def load_xml(file_name):
    records = iter_rides(file_name)
    return pd.DataFrame.from_records(records) # Return a data table to show records


# Example
if __name__ == '__main__':
    df = load_xml('taxi.xml.bz2')
    print(df.dtypes)
    print(df.head())
