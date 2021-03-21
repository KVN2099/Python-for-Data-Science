import sqlite3
import pandas as pd

conn = sqlite3.connect('rides.db', detect_types=sqlite3.PARSE_DECLTYPES)
params = {
    'vendor': 'VeriFone'
}
sql = 'SELECT distance FROM rides WHERE vendor = :vendor'

df = pd.read_sql(sql, conn, params=params)
avg_distance = df['distance'].mean()
print(f'Average distance: {avg_distance:.2f}')