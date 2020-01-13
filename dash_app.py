# imports
import zipfile as zp
import pandas as pd
import json
import plotly.offline as pyo
import plotly.graph_objs as go

# ----------------------------------------------- IMPORTING DATA -------------------------------------------------------

# Reading Airbnb df
df = pd.read_csv("./data/final_df.csv")

# Reading GeoJSON
with zp.ZipFile("./data/airbnb_data.zip") as myzip:
    with myzip.open('neighbourhoods.geojson') as myfile:
        neighborhoods = json.load(myfile)

# ----------------------------------------------- VISUALIZATIONS -------------------------------------------------------
neighborhoods["features"][0]["properties"]
fig = go.Figure(go.Choroplethmapbox(geojson=neighborhoods, locations=df, z=df,
                                    colorscale="Viridis", zmin=0, zmax=12,
                                    marker_opacity=0.5, marker_line_width=0))
fig.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129})
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()