from pathlib import Path
import csv
from datetime import datetime
import plotly.express as px
from data_extraction import DataExtractor, DataVisualizer
# define the path to csv file
path = Path('fire_data/world_fires_1_day.csv')
extractor = DataExtractor(path)

