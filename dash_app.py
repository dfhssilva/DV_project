# imports
import zipfile as zp
from typing import Type

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import numpy as np

# ------------------------------------------------- IMPORTING DATA -----------------------------------------------------

# Reading Airbnb df
from pandas import DataFrame

df = pd.read_csv("./data/final_df.csv")

#global fig_map, fig_pie, fig_bar, fig_hist

# ----------------------------------------------------- FIGURES --------------------------------------------------------
def plots_actualize(df2):

    fig_map = go.Figure(
    data=go.Scattermapbox(
        lat=df2["latitude"],
        lon=df2["longitude"],
        mode="markers"),
    layout=go.Layout(
        autosize=True,
        margin=go.layout.Margin(l=0, r=0, t=0, b=0),
        showlegend=False,
        mapbox=dict(
            accesstoken="pk.eyJ1IjoicjIwMTY3MjciLCJhIjoiY2s1Y2N4N2hoMDBrNzNtczBjN3M4d3N4diJ9.OrgK7MnbQyOJIu6d60j_iQ",
            style="dark",
            center={'lat': 39, 'lon': -9.2},
            zoom=8.5,
            )
        )
    )

    pie_colors = ["#424bf5", "#4296f5", "#42ddf5"]
    unique_rooms = list(df2.room_type.unique())
    if len(unique_rooms) == 1:
        if unique_rooms[0] == 'Private room':
            pie_colors = ["#4296f5"]
        elif unique_rooms[0] == 'Shared room':
            pie_colors = ["#42ddf5"]


    fig_pie = go.Figure(
        data=go.Pie(
            labels=df2['room_type'].value_counts().index,
            values=df2['room_type'].value_counts().values,
            textinfo='text+value+percent',
            text=df2['room_type'].value_counts().index,
            hoverinfo='label',
            marker=dict(colors=pie_colors),
            showlegend=False),
        layout=go.Layout(
            margin=go.layout.Margin(l=0, r=0, t=70, b=0),
            title='Proportion of Room Type')
    )

    fig_bar = go.Figure(
        data=go.Bar(
            x=df2['ordinal_rating'].value_counts().values,
            y=df2['ordinal_rating'].value_counts().index,
            orientation='h'),
        layout=go.Layout(
            margin=go.layout.Margin(l=0, r=0, t=70, b=0),
            title="Listing Rating Frequency",
            clickmode='event+select')
    )

    fig_hist = go.Figure(
        data=go.Histogram(
            x=df2['price'],
            histnorm=""),
        layout=go.Layout(
            margin=go.layout.Margin(l=0, r=0, t=70, b=0),
            title="Listing Rating Frequency")
    )
    fig_hist.data[0].marker.line = dict(color='black', width=1)
    fig_hist.update_layout(xaxis_title='Price ($)',
                           yaxis_title='Listing frequencies',
                           showlegend=False,
                           title='Price distribution')

    return (fig_map, fig_pie, fig_bar, fig_hist)

fig_map, fig_pie, fig_bar, fig_hist = plots_actualize(df)

# ------------------------------------------------------- APP ----------------------------------------------------------
app = dash.Dash(__name__, assets_folder="./assets")

# Add the following line before deployment
# server = app.server

# ------------------------------------------------------- HTML ---------------------------------------------------------

app.layout = html.Div([
    html.Div([
        html.Div([
            html.H1('Airbnb Lisbon: a client focused application'),
        ], id='html_title'),
        html.Div([
            html.Div([
                dcc.Graph(figure=fig_map, id="dcc_map_graph")
            ], id='html_map', className='eight columns'),
            html.Div([
                dcc.Dropdown(
                    options=[{'label': i, 'value': i} for i in
                             ["All"] + df["neighbourhood_group_cleansed"].unique().tolist()],
                    value='All',
                    style={'padding-left': 0},
                    id='dcc_neighbourhood_dropdown'
                ),
                dcc.Dropdown(
                    options=[{'label': i, 'value': j} for i, j in zip(
                        ["Availability", "Superhost", "Property Type", "Cancellation Policy"],
                        ["availability_next_30", "host_is_superhost", "property_type", "cancellation_policy"])],
                    value='availability_next_30',
                    id='dcc_variable_dropdown'
                ),
                html.Button('Reset_', id='button'),
                dcc.Graph(figure=fig_pie, selectedData={'points': []}, id="dcc_pie_graph"),
                html.Button('Submit', id='button'),
                dcc.Graph(figure=fig_bar, selectedData={'points': []}, id="dcc_bar_graph"),
                html.Div(dcc.Input(id = 'input-min-price', placeholder='Enter minimum price', type = 'text')),
                html.Div(dcc.Input(id = 'input-max-price', placeholder='Enter maximum price', type = 'text')),
                html.Button('Submit', id='button'),
                dcc.Graph(figure=fig_hist, selectedData={'points': []}, id="dcc_hist_graph")
            ], id="html_non_map", className="four columns")
        ], id="html_row", className="row")
    ])
])

# --------------------------------------------------- CALLBACKS --------------------------------------------------------
rates = list(df.ordinal_rating.unique())
neig = list(df.neighbourhood_group_cleansed.unique())
price = [df.price.min(), df.price.max()]
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
    aux = aux.loc[(aux['price'] >= price[0]) & (aux['price'] <= price[-1])]
    return aux

list_of_neighbourhoods = {
    "All": {"lat": 39, "lon": -9.2, "zoom": 8.5},
    "Amadora": {"lat": 38.7578, "lon": -9.2245, "zoom": 11},
    "Cascais": {"lat": 38.6979, "lon": -9.42146, "zoom": 11},
    "Cadaval": {"lat": 39.2434, "lon": -9.1027, "zoom": 11},
    "Arruda Dos Vinhos": {"lat": 38.9552, "lon": -8.989, "zoom": 11},
    "Vila Franca De Xira": {"lat": 38.9552, "lon": -8.989, "zoom": 11},
    "Oeiras": {"lat": 38.6969, "lon": -9.3146, "zoom": 11},
    "Loures": {"lat": 38.8315, "lon": -9.1741, "zoom": 11},
    "Sobral De Monte Agrao": {"lat": 39.0188, "lon": -9.1505, "zoom": 11},
    "Alenquer": {"lat": 39.0577, "lon": -9.014, "zoom": 11},
    "Odivelas": {"lat": 38.7954, "lon": -9.1852, "zoom": 11},
    "Torres Vedras": {"lat": 39.0918, "lon": -9.26, "zoom": 11},
    "Lourinhã": {"lat": 39.2415, "lon": -9.313, "zoom": 11},
    "Mafra": {"lat": 38.9443, "lon": -9.3321, "zoom": 11},
    "Sintra": {"lat": 38.8029, "lon": -9.3817, "zoom": 11},
    "Lisboa": {"lat": 38.7223, "lon": -9.1393, "zoom": 11},
    "Azambuja": {"lat": 39.0696, "lon": -8.8693, "zoom": 11},
}


@app.callback(
    Output("dcc_map_graph", "figure"),
    [
        Input("dcc_neighbourhood_dropdown", "value"),
        Input("dcc_variable_dropdown", "value")
    ],
)
def update_map(selectedlocation, selectedvariable):

    if selectedlocation:
        latInitial = list_of_neighbourhoods[selectedlocation]["lat"]
        lonInitial = list_of_neighbourhoods[selectedlocation]["lon"]
        zoomInitial = list_of_neighbourhoods[selectedlocation]["zoom"]

        return go.Figure(
            data=[
                go.Scattermapbox(
                    lat=df["latitude"],
                    lon=df["longitude"],
                    mode="markers"
                )
            ],
            layout=go.Layout(
                autosize=True,
                margin=go.layout.Margin(l=0, r=0, t=0, b=0),
                showlegend=False,
                mapbox=dict(
                    accesstoken="pk.eyJ1IjoicjIwMTY3MjciLCJhIjoiY2s1Y2N4N2hoMDBrNzNtczBjN3M4d3N4diJ9.OrgK7MnbQyOJIu6d60j_iQ",
                    center={'lat': latInitial, 'lon': lonInitial},
                    zoom=zoomInitial,
                    style="dark"
                )
            )
        )


@app.callback([
     Output('dcc_pie_graph', "figure"),
     Output('dcc_bar_graph', "figure"),
     Output('dcc_hist_graph', "figure"),
     # Output('input-max-price', "value"),
     # Output('input-min-price', "figure")
    ]
    , [Input("dcc_neighbourhood_dropdown", "value"),
       Input("dcc_pie_graph", "clickData"),
       Input("dcc_bar_graph", "selectedData"),
       Input("button", "n_clicks")],
       [State('input-min-price', 'value'),
        State('input-max-price', 'value')])


def update_graph(sel_neig, selected_pie, selected_bar, button, min_price, max_price):

    if sel_neig!="All":
        selected_neig = []
        selected_neig.append(sel_neig)
    else:
        selected_neig = neig

    if selected_pie:
        selected_pie_unique = []
        selected_pie_unique.append(selected_pie['points'][0]['label'])
    else:
        selected_pie_unique = room

    if len(selected_bar['points']) != 0:
        selected_bar_unique = list(np.intersect1d(rates, [b['y'] for b in selected_bar['points']]))
    else:
        selected_bar_unique = rates


    if min_price and max_price:
        selected_hist_unique = [int(min_price), int(max_price)]
    elif min_price:
        selected_hist_unique = [int(min_price), price[-1]]
    elif max_price:
        selected_hist_unique = [price[0], int(max_price)]
    else:
        selected_hist_unique = price

    df_sliced = slice_df(selected_neig, selected_bar_unique, selected_hist_unique, selected_pie_unique)


    fig_map_update, fig_pie_update, fig_bar_update, fig_hist_update = plots_actualize(df_sliced)

    return fig_pie_update, fig_bar_update, fig_hist_update

# for selected_data in [selected_pie, selected_bar, selected_hist]:
#     if selected_data and selected_data['points']:
#         selectedpoints = np.intersect1d(selectedpoints,
#                                         [p['y'] for p in selected_data['points']])
#     print(selectedpoints['points'])
#     # df_sliced = df_sliced.iloc[selectedpoints, ]
#
# fig_map_update, fig_pie_update, fig_bar_update, fig_hist_update = plots_actualize(df_sliced)
#
# return fig_pie_update, fig_bar_update, fig_hist_update



if __name__ == '__main__':
    app.run_server()
