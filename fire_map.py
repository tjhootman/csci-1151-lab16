from pathlib import Path
import csv
from datetime import datetime

path = Path('fire_data/world_fires_1_day.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# extract brights
brights = []
lons = []
lats = []
dates = []

for row in reader:
    lon = float(row[0])
    lat = float(row[1])
    bright = float(row[2])
    date = datetime.strptime(row[5], '%Y-%m-%d')
    lons.append(lon)
    lats.append(lat)
    brights.append(bright)
    dates.append(date)
