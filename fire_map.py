from pathlib import Path
import csv
from datetime import datetime
import plotly.express as px

path = Path('fire_data/world_fires_1_day.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# extract data
lats = []
lons = []
brights = []
dates = []
hover_texts = []

# counter for rows
row_count = 0
max_rows = 1000

for row in reader:
    if row_count >= max_rows:
        break

    lat = float(row[0])
    lon = float(row[1])
    bright = float(row[2])
    date = datetime.strptime(row[5], '%Y-%m-%d').date()
    hover_text = f'{lat}, {lon}/n{date}'
    lons.append(lon)
    lats.append(lat)
    brights.append(bright)
    dates.append(date)
    hover_texts.append(hover_text)

    row_count += 1

title = 'Global Fires'
fig = px.scatter_geo(lat=lats,
                     lon=lons,
                     title=title,
                     color=brights,
                     color_continuous_scale='Bluered_r',
                     labels={'color':'Brightness'},
                     projection='natural earth',
                     custom_data=[lats, lons, dates]
                     )
fig.update_traces(
                hovertemplate=
                '(%{customdata[0]}°, ' +
                '%{customdata[1]}°)<br>' +
                '%{customdata[2]}'
                )

fig.show()
