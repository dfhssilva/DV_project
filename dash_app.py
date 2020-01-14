# imports
import zipfile as zp
from typing import Type

import pandas as pd
import json
import plotly.offline as pyo
import plotly.figure_factory as ff
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# ------------------------------------------------- IMPORTING DATA -----------------------------------------------------

# Reading Airbnb df
from pandas import DataFrame

df = pd.read_csv("./data/final_df.csv")

# -------------------------- Slice df Function for Graphs ------------------------------------------
rates = list(df.ordinal_rating.unique())
neig = list(df.neighbourhood_group_cleansed.unique())
price = [[df.price.min(), df.price.max()]]
room = list(df.room_type.unique())


def slice_df(neig=neig, rates=rates, price=price, room=room):
    aux = df.copy()
    # slice neighbourhood
    aux = aux.loc[aux['neighbourhood_group_cleansed'].isin(neig)]
    # slice rating
    aux = aux.loc[aux['ordinal_rating'].isin(rates)]
    # slice room type
    aux = aux.loc[aux['room_type'].isin(room)]
    # slice price
    aux = aux.loc[(aux['price'] > price[0]) & (aux['price'] < price[-1])]

    return aux
# -------------------------------------------------------------------------------------------------


# # Reading GeoJSON
# with zp.ZipFile("./data/airbnb_data.zip") as myzip:
#     with myzip.open('neighbourhoods.geojson') as myfile:
#         neighborhoods = json.load(myfile)

# ------------------------------------------------- VISUALIZATIONS -----------------------------------------------------
app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='neighbourhood-dropdown',
                options=[{'label': i, 'value': i} for i in ["All"] + df["neighbourhood_group_cleansed"].unique().tolist()],
                value='All'
            ),
            dcc.Dropdown(
                id='variable-dropdown',
                options=[{'label': i, 'value': j} for i, j in zip(
                    ["Availability", "Superhost", "Property Type", "Cancellation Policy"],
                    ["availability_next_30", "host_is_superhost", "property_type", "cancellation_policy"])],
                value='availability_next_30'
            )
        ], style=dict(width='50%', display='inline-block')
        ),
        dcc.Graph(id="map-graph")
    ])
])

# locations = set((df["neighbourhood_group_cleansed"].values))

list_of_neighbourhoods= {
    "All" : {"lat": 39, "lon": -9.2, "zoom": 8.5},
    "Amadora":{"lat": 38.7578 , "lon": -9.2245, "zoom": 11},
    "Cascais":{"lat": 38.6979 , "lon": -9.42146, "zoom": 11},
    "Cadaval":{"lat": 39.2434 , "lon": -9.1027, "zoom": 11},
    "Arruda Dos Vinhos":{"lat": 38.9552 , "lon":  -8.989, "zoom": 11},
    "Vila Franca De Xira":{"lat": 38.9552 , "lon": -8.989, "zoom": 11},
    "Oeiras":{"lat": 38.6969 , "lon": -9.3146, "zoom": 11},
    "Loures":{"lat": 38.8315, "lon": -9.1741, "zoom": 11},
    "Sobral De Monte Agrao":{"lat": 39.0188 , "lon": -9.1505, "zoom": 11},
    "Alenquer":{"lat": 39.0577 , "lon": -9.014, "zoom": 11},
    "Odivelas":{"lat": 38.7954 , "lon":  -9.1852, "zoom": 11},
    "Torres Vedras":{"lat": 39.0918, "lon": -9.26, "zoom": 11},
    "Lourinhã":{"lat": 39.2415 , "lon": -9.313, "zoom": 11},
    "Mafra":{"lat": 38.9443, "lon": -9.3321, "zoom": 11},
    "Sintra":{"lat": 38.8029 , "lon":  -9.3817, "zoom": 11},
    "Lisboa":{"lat": 38.7223 , "lon": -9.1393, "zoom": 11},
    "Azambuja":{"lat": 39.0696 , "lon": -8.8693, "zoom": 11},
}

@app.callback(
    Output("map-graph", "figure"),
    [
        Input("neighbourhood-dropdown", "value"),
        Input("variable-dropdown", "value")
    ],
)
def update_graph(selectedlocation, selectedVariable):
    latInitial = 39
    lonInitial = -9.2
    bearing = 0

    if selectedlocation:
        latInitial = list_of_neighbourhoods[selectedlocation]["lat"]
        lonInitial = list_of_neighbourhoods[selectedlocation]["lon"]
        zoomInitial = list_of_neighbourhoods[selectedlocation]["zoom"]
    return go.Figure(
    # Data
        data = [
            go.Scattermapbox(
                lat=df["latitude"],
                lon=df["longitude"],
                mode="markers"
            ),
            # # Plot of important locations on the map
            # go.Scattermapbox(
            #     lat=[list_of_neighbourhoods[i]["lat"] for i in list_of_neighbourhoods],
            #     lon=[list_of_neighbourhoods[i]["lon"] for i in list_of_neighbourhoods],
            #     #Visible = True,
            #     mode= "none",
            #     text=[i for i in list_of_neighbourhoods],
            # ),
        ],
    # Layout
        layout = go.Layout(
                autosize=True,
                margin=go.layout.Margin(l=0, r=35, t=0, b=0),
                showlegend=False,
                mapbox=dict(
                    accesstoken="pk.eyJ1IjoicjIwMTY3MjciLCJhIjoiY2s1Y2N4N2hoMDBrNzNtczBjN3M4d3N4diJ9.OrgK7MnbQyOJIu6d60j_iQ",
                    center={'lat': latInitial , 'lon': lonInitial },
                    zoom = zoomInitial,
                    style="dark"
                )
        )
    )


@app.callback([
    Output("map-graph", "figure"),
    Output('room-graph', "figure"),
    Output('rating-graph', "figure"),
    Output('price-graph', "figure")
], [Input("neighbourhood-dropdown", "value"),
    Input('room-value', "value"),
    Input('rating-value', "value"),
    Input('price-value', "value")]
)
def update_graph (sel_neig, sel_room, sel_rate, sel_price):

    df_sliced = slice_df(sel_neig, sel_room, sel_rate, sel_price)



if __name__ == '__main__':
    app.run_server()

