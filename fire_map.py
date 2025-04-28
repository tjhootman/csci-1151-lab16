from pathlib import Path
import csv
from datetime import datetime
import plotly.express as px

path = Path('fire_data/world_fires_1_day.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# extract brights
brights = []
lons = []
lats = []
dates = []
hover_texts = []

for row in reader:
    lat = float(row[0])
    lon = float(row[1])
    bright = float(row[2])
    date = datetime.strptime(row[5], '%Y-%m-%d')
    hover_text = f'{lat}, {lon}/n{date}'
    lons.append(lon)
    lats.append(lat)
    brights.append(bright)
    dates.append(date)
    hover_texts.append(hover_text)

title = 'Global Fires'
fig = px.scatter_geo(lat=lats,
                     lon=lons,
                     title=title,
                     color=brights,
                     color_continuous_scale='Bluered_r',
                     labels={'color':'Brightness'},
                     projection='natural earth',
                     )

fig.show()
