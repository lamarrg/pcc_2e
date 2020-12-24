# In the resources for this chapter, you’ll find a file called world_fires_1_day.csv. This file contains information about fires burning in dif- ferent locations around the globe, including the latitude and longitude, and the brightness of each fire. Using the data processing work from the first part of this chapter and the mapping work from this section, make a map that shows which parts of the world are affected by fires.
# You can download more recent versions of this data at https://earthdata .nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data/. You can find links to the data in CSV format in the TXT section.

import matplotlib.pyplot as plt
import csv
from datetime import datetime
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'json_global_data/world_fires_1_day.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# print(header_row)

    lats, lons, temps = [], [], []
    for row in reader:
        lat = row[0]
        lon = row[1]
        temp = row[2]
        temps.append(float(temp))
        lats.append(lat)
        lons.append(lon)


data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': temps,
    'marker': {
        'size': [temp/100 for temp in temps],
        'color': temps,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Current Global Fires'}
    }
}]

my_layout = Layout(title="Global Fires")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')


