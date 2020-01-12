# imports
import zipfile as zp
import pandas as pd
import json

# Reading GeoJSON
with zp.ZipFile("./data/airbnb_data.zip") as myzip:
    with myzip.open('neighbourhoods.geojson') as myfile:
        neighborhoods = json.load(myfile)
import plotly.graph_objects as go

fig = go.Figure(go.Choroplethmapbox(geojson=counties, locations=df.fips, z=df.unemp,
                                    colorscale="Viridis", zmin=0, zmax=12,
                                    marker_opacity=0.5, marker_line_width=0))
fig.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129})
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()