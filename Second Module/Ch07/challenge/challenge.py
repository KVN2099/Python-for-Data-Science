import sqlite3
import pandas as pd
from datetime import datetime

conn = sqlite3.connect('rides.db', detect_types=sqlite3.PARSE_DECLTYPES)
df = pd.read_sql('SELECT * FROM rides', conn)
conn.close()
print(df)

df['ride_duration'] = df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']

print(df)