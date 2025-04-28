from pathlib import Path
import csv
from datetime import datetime
import plotly.express as px

# define the path to csv file
path = Path('fire_data/world_fires_1_day.csv')

try:
    # read the contents of file and split into lines
    lines = path.read_text(encoding='utf-8').splitlines()
except FileNotFoundError:
    print(f"Error: The file was not found at {path}")

# create csv reader to iterate over the lines. skip header row
reader = csv.reader(lines)
next(reader)

# initalize empty lists to store extracted data
lats = []
lons = []
brights = []
dates = []
hover_texts = []

# counter for rows and limit for data processing
row_count = 0
max_rows = 1000

# iterate over each row in CSV reader
for row in reader:
    # stop processing if maximum rows is reached
    if row_count >= max_rows:
        break

    # extract data from specific columns and convert to appropriate types
    try:
        lat = float(row[0])
        lon = float(row[1])
        bright = float(row[2])
        date = datetime.strptime(row[5], '%Y-%m-%d').date()
        hover_text = f'{lat}, {lon}/n{date}' # is this needed?
    except ValueError as e:
        print(e)
    else:
        # append the data the appropriate lists
        lons.append(lon)
        lats.append(lat)
        brights.append(bright)
        dates.append(date)
        hover_texts.append(hover_text)

    # increment the row counter
    row_count += 1

# set the title
title = 'Global Fires'

# create a geographical scatter plot
fig = px.scatter_geo(lat=lats,
                     lon=lons,
                     title=title,
                     color=brights,
                     color_continuous_scale='Bluered_r',
                     labels={'color':'Brightness'},
                     projection='natural earth',
                     custom_data=[lats, lons, dates]
                     )

# update the markers and hover text information
fig.update_traces(
                marker=dict(size=10,line=dict(width=1,color='White')),
                selector=dict(mode='markers'),
                hovertemplate=
                '(%{customdata[0]}°, ' +
                '%{customdata[1]}°)<br>' +
                '%{customdata[2]}',
                )

# show the plot
fig.show()

# additional try-except blocks?
