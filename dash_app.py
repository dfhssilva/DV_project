# imports
import zipfile as zp
import pandas as pd
import json
import plotly.offline as pyo
import plotly.graph_objs as go

# ------------------------------------------------- IMPORTING DATA -----------------------------------------------------

# Reading Airbnb df
df = pd.read_csv("./data/final_df.csv")

# # Reading GeoJSON
# with zp.ZipFile("./data/airbnb_data.zip") as myzip:
#     with myzip.open('neighbourhoods.geojson') as myfile:
#         neighborhoods = json.load(myfile)

# ------------------------------------------------- VISUALIZATIONS -----------------------------------------------------

# Data
data = go.Scattermapbox(
        lat=df["latitude"],
        lon=df["longitude"],
        mode="markers"
)
# Layout
layout = go.Layout(
            autosize=True,
            margin=go.layout.Margin(l=0, r=35, t=0, b=0),
            showlegend=False,
            mapbox=dict(
                accesstoken="pk.eyJ1IjoicjIwMTY3MjciLCJhIjoiY2s1Y2N4N2hoMDBrNzNtczBjN3M4d3N4diJ9.OrgK7MnbQyOJIu6d60j_iQ",
                center=dict(lat=-9, lon=39),  # 40.7272  # -73.991251
                style="dark"
            ))

fig = go.Figure(data=data, layout=layout)  # Figure is composed by data(what you show) and layout(how you show)
pyo.plot(fig)

