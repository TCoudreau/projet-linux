import pandas as pd
from datetime import datetime, timedelta
import json

data = pd.read_csv("/home/thomas/projet/history.csv")

data['date'] = pd.to_datetime(data['date'])

now = datetime.now()
start_date = datetime(now.year, now.month, now.day - 1, 20)
end_date = datetime(now.year, now.month, now.day, 20)

doge_filtre = data[(data['date'] > start_date) & (data['date'] <= end_date)]

vol = doge_filtre['doge'].std()
start = doge_filtre.iloc[0]['doge']
end = doge_filtre.iloc[-1]['doge']
evol = (start-end)/start
minimum = doge_filtre['doge'].min()
maximum = doge_filtre['doge'].max()

stats = { "Volatilité": vol, "Open": start, "Close": end, "Evolution": str(evol*100) + "%", "Minimum": minimum, "Maximum": maximum }

with open("/home/thomas/projet/stats.json", "w") as outfile:
    json.dump(stats, outfile)

