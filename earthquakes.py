import io
import json
import plotly.express as px
import numpy as np

export_readable_data = False

with io.open('earthquakes_data/data.geojson', mode='r', encoding='utf-8') as in_file:
    json_data = json.loads(in_file.read())

if export_readable_data:
    # Open output file write-only and create it if it doesn't exist
    with io.open('earthquakes_data/data_readable.geojson', mode='w+') as out_file:
        max_num_chars = 1000
        num_chars = 0
        # Write more readable version of the data to output file
        readable_data = json.dumps(json_data, indent=4)
        for char in readable_data:
            if num_chars > max_num_chars:
                break
            out_file.write(char)
            num_chars += 1

earthquakes = json_data['features']
longitudes, latitudes, magnitudes, titles = [], [], [], []
for quake in earthquakes:
    longitudes.append(quake['geometry']['coordinates'][0])
    latitudes.append(quake['geometry']['coordinates'][1])
    magnitudes.append(quake['properties']['mag'])
    titles.append(quake['properties']['title'])

fig = px.scatter_geo(
    lat=latitudes, lon=longitudes, size=magnitudes, color=magnitudes, color_continuous_scale='viridis',
    title=json_data['metadata']['title'], labels={'color': 'Magnitude', 'size':'Magnitude', 'lat':'Latitude', 'lon':'Longitude'},
    projection='natural earth', hover_name=titles)

fig.show()
