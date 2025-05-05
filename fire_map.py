"""Create a fire map figure using Plotly."""
from pathlib import Path
from data_extraction import DataExtractor, DataVisualizer

path = Path('fire_data/world_fires_1_day.csv')
extractor = DataExtractor(path)

try:
    lats, lons, brights, dates = extractor.extract(max_rows=1000) #utilizing tuple unpacking
    visualizer = DataVisualizer()
    fig = visualizer.create_plot(lats, lons, brights, dates)
    visualizer.show_plot(fig)
except FileNotFoundError as e:
    print(e)
