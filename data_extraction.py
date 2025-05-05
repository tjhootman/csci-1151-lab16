"""Module containing classes for data extraction and data visualization 
using plotly."""
from pathlib import Path
import csv
from datetime import datetime
import plotly.express as px

class DataExtractor:
    """Extracts data from a CSV file."""
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.lats = []
        self.lons = []
        self.brights = []
        self.dates = []

    def extract(self, max_rows: int = 1000):
        """Extracts the data from a CSV file.

        Args:
            max_rows (int, optional): The maximum bumber of rows to extract.
                                        Defaults to 1000.

        Returns:
            tuple: A tuple containing the four lists: latitudes, longitudes,
            brightness and dates.
        
        Raises:
            FileNotFoundError: If the specified file_path does not exist.
        """
        try:
            # read the contents of file and split into lines
            lines = self.file_path.read_text(encoding='utf-8').splitlines()
        except FileNotFoundError:
            print(f"Error: The file was not found at {self.file_path}")

        # create csv reader to iterate over the lines. skip header row
        reader = csv.reader(lines)
        next(reader)

        # counter for rows
        row_count = 0

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
            except ValueError as e:
                print(e)
            else:
                # append the data the appropriate lists
                self.lons.append(lon)
                self.lats.append(lat)
                self.brights.append(bright)
                self.dates.append(date)

            # increment the row counter
            row_count += 1

        return self.lats, self.lons, self.brights, self.dates

class DataVisualizer:
    """Visualizes data on a geographical scatter plot using Plotly."""
    def __init__(self, title: str = 'Global Fires'):
        self.title = title

    def create_plot(self, lats, lons, brights, dates):
        """Creates a geographical scatter plot of the data using Plotly Express.

        Args:
            lats (list[float]): A list of latitudes.
            lons (list[float]): A list of longitudes.
            brights (list[float]): A list of brightness values.
            dates (list[datetime.date]): A list of dates.

        Returns:
            px.scatter_geo: A Plotly Express Figure object representing the 
            scatter plot.
        """
        # create a geographical scatter plot
        fig = px.scatter_geo(lat=lats,
                            lon=lons,
                            title=self.title,
                            color=brights,
                            color_continuous_scale='Reds_r',
                            labels={'color':'Brightness'},
                            projection='natural earth',
                            custom_data=[lats, lons, dates]
                            )

        # update the markers and hover text information
        fig.update_traces(
                        marker=dict(size=10,line=dict(width=1,color='White')),
                        selector=dict(mode='markers'),
                        hovertemplate=
                        '(%{customdata[0]:.2f}°, %{customdata[1]:.2f}°)<br>' +
                        '%{customdata[2]}',
                        )

        return fig

    def show_plot(self, fig):
        """Displays the generated Plotly figure.

        Args:
            fig (px.scatter_geo): The Plotly Express Figure object to display.
        """
        fig.show()
