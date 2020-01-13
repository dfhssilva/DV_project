# imports
import zipfile as zp
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
df = pd.read_csv("./data/final_df.csv")

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

def selection():
    pass

# fig = go.Figure(data=data, layout=layout)  # Figure is composed by data(what you show) and layout(how you show)
# pyo.plot(fig)
if __name__ == '__main__':
    app.run_server()


hist_data = [df['price']]
group_labels = ['distplot']
f = ff.create_distplot(hist_data, group_labels, bin_size=5, show_rug=False)
fig1 = go.Figure(f)
fig1.data[0].marker.line = dict(color='black', width=2)
fig1.data[1].line.color = 'red'
fig1.layout.sliders = [dict(
                active=4,
                currentvalue={"prefix": "bin size: "},
                pad={"t": 20},
                steps=[dict(label=i, method='restyle',  args=['xbins.size', i]) for i in range(1, 20)]
                )]
fig1.update_layout(xaxis_title='Price ($)', yaxis_title='Relative frequencies', showlegend=False, title='Price distribution')
pyo.plot(fig1)


data = [go.Bar(
            x=df['room_type'].value_counts().values,
            y=df['room_type'].value_counts().index,
            orientation='h', marker=dict(color=['red', 'blue', 'green'])
)]
layout = go.Layout(title=go.layout.Title(text='Room Type'))
fig2 = go.Figure(data=data, layout=layout)
fig2.update_layout(xaxis_title="Number of listings")
pyo.plot(fig2)


fig3 = go.Figure()
fig3.add_trace(go.Pie(labels=df['ordinal_rating'].value_counts().index, values=df['ordinal_rating'].value_counts().values))
fig3.update_layout(title="Proportion of listing's rating")
pyo.plot(fig3)