import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
from dash.dependencies import Input, Output
from plotly import graph_objs as go
from plotly.graph_objs import *
from datetime import datetime as dt

# Plotly mapbox public token
mapbox_access_token = "pk.eyJ1IjoicjIwMTY3MjciLCJhIjoiY2s1Y2N4N2hoMDBrNzNtczBjN3M4d3N4diJ9.OrgK7MnbQyOJIu6d60j_iQ"


# ------------------------------------------------- IMPORTING DATA -----------------------------------------------------
# Reading Airbnb df
df = pd.read_csv("./data/final_df.csv")

# Dictionary of Municipalities
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

# ----------------------------------------------------- FIGURES --------------------------------------------------------
fig_map = go.Figure(
    data=go.Scattermapbox(
        lat=df["latitude"],
        lon=df["longitude"],
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

fig_pie = go.Figure(
    data=go.Pie(
        labels=df['room_type'].value_counts().index,
        values=df['room_type'].value_counts().values,
        textinfo='text+value+percent',
        text=df['room_type'].value_counts().index,
        hoverinfo='label',
        showlegend=False),
    layout=go.Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=go.layout.Margin(l=0, r=0, t=70, b=0),
        title='Proportion of Room Type')
)

fig_bar = go.Figure(
    data=go.Bar(
        x=df['ordinal_rating'].value_counts().values,
        y=df['ordinal_rating'].value_counts().index,
        orientation='h'),
    layout=go.Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=go.layout.Margin(l=0, r=0, t=70, b=0),
        title="Listing Rating Frequency")
)

fig_hist = go.Figure(
    data=ff.create_distplot(
        [df['price']],
        ['distplot'],
        bin_size=30,
        show_rug=False),
    layout=go.Layout(
        margin=go.layout.Margin(l=0, r=0, t=70, b=0),
        title="Listing Rating Frequency",
        sliders=[dict(active=4,
                      currentvalue={"prefix": "bin size: "},
                      pad={"t": 20},
                      steps=[dict(label=i,
                                  method='restyle',
                                  args=['xbins.size', i]) for i in range(1, 20)]
                      )
                 ]
        )
)

fig_hist.data[0].marker.line = dict(color='black', width=2)
fig_hist.data[1].line.color = 'red'
fig_hist.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                       plot_bgcolor='rgba(0,0,0,0)',
                       xaxis_title='Price ($)',
                       yaxis_title='Relative frequencies',
                       showlegend=False,
                       title='Price distribution')

# ------------------------------------------------------- APP ----------------------------------------------------------
app = dash.Dash(__name__)
# server = app.server

# Layout of Dash App
app.layout = html.Div(
    children=[
        html.Div(
            # TOP ROW
            className="row",
            children=[
                html.Div(
                    className="two columns div-user-controls",
                    children=[
                        html.Img(
                            className="logo", src=app.get_asset_url("airbnb_logo.png")
                        ),
                        html.H3("AIRBNB APP"),
                        dcc.Markdown(
                            children=[
                                "Source: [Inside Airbnb](http://insideairbnb.com/get-the-data.html)"
                            ]
                        )
                    ]
                ),
                html.Div(
                    className="four columns div-user-controls",
                    children=[
                        "The following application describes the airbnb listings of Lisbon."
                    ]
                ),
                html.Div(
                    className="three columns div-user-controls",
                    children=[
                        "Interact with the dashboard: ",
                        html.Div(
                            className="div-for-dropdown",
                            children=[
                                # Dropdown for locations on map
                                dcc.Dropdown(
                                    id='dcc_neighbourhood_dropdown',
                                    options=[{'label': i, 'value': i} for i in
                                        ["All"] + df["neighbourhood_group_cleansed"].unique().tolist()],
                                    # value='All',
                                    placeholder="Select Municipality",
                                    style={'max-width': '250px'}
                                )
                            ]
                        ),
                        html.Div(
                            className="div-for-dropdown",
                            children=[
                                # Dropdown to select variables
                                dcc.Dropdown(
                                    id='dcc_variable_dropdown',
                                    options=[{'label': i, 'value': j} for i, j in zip(
                                        ["Availability", "Superhost", "Property Type", "Cancellation Policy"],
                                        ["availability_next_30", "host_is_superhost", "property_type",
                                         "cancellation_policy"])],
                                    # value='availability_next_30',
                                    placeholder="Select Variable",
                                    style={'max-width': '250px'}
                                )
                            ]
                        )
                    ]
                ),
                html.Div(
                    className="three columns div-user-controls",
                    children=[
                        "Percentage of listings: ",
                        html.P(id="percentage-listings", style={"height": "35px"}),
                        "Rank of location: ",
                        html.P(id="rank-location", style={"height": "35px"}),
                    ]
                )
            ]
        ),
        html.Div(
            children=[
                html.Div(
                    # MAP
                    className="eight columns",
                    children=[
                        dcc.Graph(figure=fig_map, id="dcc_map_graph")
                    ]
                ),
                html.Div(
                    # GRAPHS
                    className="four columns scrollcol bg-grey",
                    children=[
                        dcc.Graph(figure=fig_pie, id="dcc_pie_graph"),
                        dcc.Graph(figure=fig_bar, id="dcc_bar_graph"),
                        dcc.Graph(figure=fig_hist, id="dcc_hist_graph")
                    ]
                )
            ]
        )
    ]
)
#
# # Gets the amount of days in the specified month
# # Index represents month (0 is April, 1 is May, ... etc.)
# daysInMonth = [30, 31, 30, 31, 31, 30]
#
# # Get index for the specified month in the dataframe
# monthIndex = pd.Index(["Apr", "May", "June", "July", "Aug", "Sept"])
#
# # Get the amount of rides per hour based on the time selected
# # This also higlights the color of the histogram bars based on
# # if the hours are selected
# def get_selection(month, day, selection):
#     xVal = []
#     yVal = []
#     xSelected = []
#     colorVal = [
#         "#F4EC15",
#         "#DAF017",
#         "#BBEC19",
#         "#9DE81B",
#         "#80E41D",
#         "#66E01F",
#         "#4CDC20",
#         "#34D822",
#         "#24D249",
#         "#25D042",
#         "#26CC58",
#         "#28C86D",
#         "#29C481",
#         "#2AC093",
#         "#2BBCA4",
#         "#2BB5B8",
#         "#2C99B4",
#         "#2D7EB0",
#         "#2D65AC",
#         "#2E4EA4",
#         "#2E38A4",
#         "#3B2FA0",
#         "#4E2F9C",
#         "#603099",
#     ]
#
#     # Put selected times into a list of numbers xSelected
#     xSelected.extend([int(x) for x in selection])
#
#     for i in range(24):
#         # If bar is selected then color it white
#         if i in xSelected and len(xSelected) < 24:
#             colorVal[i] = "#FFFFFF"
#         xVal.append(i)
#         # Get the number of rides at a particular time
#         yVal.append(len(totalList[month][day][totalList[month][day].index.hour == i]))
#     return [np.array(xVal), np.array(yVal), np.array(colorVal)]
#
#
# # Selected Data in the Histogram updates the Values in the DatePicker
# @app.callback(
#     Output("bar-selector", "value"),
#     [Input("histogram", "selectedData"), Input("histogram", "clickData")],
# )
# def update_bar_selector(value, clickData):
#     holder = []
#     if clickData:
#         holder.append(str(int(clickData["points"][0]["x"])))
#     if value:
#         for x in value["points"]:
#             holder.append(str(int(x["x"])))
#     return list(set(holder))
#
#
# # Clear Selected Data if Click Data is used
# @app.callback(Output("histogram", "selectedData"), [Input("histogram", "clickData")])
# def update_selected_data(clickData):
#     if clickData:
#         return {"points": []}
#
#
# # Update the total number of rides Tag
# @app.callback(Output("total-rides", "children"), [Input("date-picker", "date")])
# def update_total_rides(datePicked):
#     date_picked = dt.strptime(datePicked, "%Y-%m-%d")
#     return "Total Number of rides: {:,d}".format(
#         len(totalList[date_picked.month - 4][date_picked.day - 1])
#     )
#
#
# # Update the total number of rides in selected times
# @app.callback(
#     [Output("total-rides-selection", "children"), Output("date-value", "children")],
#     [Input("date-picker", "date"), Input("bar-selector", "value")],
# )
# def update_total_rides_selection(datePicked, selection):
#     firstOutput = ""
#
#     if selection is not None or len(selection) is not 0:
#         date_picked = dt.strptime(datePicked, "%Y-%m-%d")
#         totalInSelection = 0
#         for x in selection:
#             totalInSelection += len(
#                 totalList[date_picked.month - 4][date_picked.day - 1][
#                     totalList[date_picked.month - 4][date_picked.day - 1].index.hour
#                     == int(x)
#                 ]
#             )
#         firstOutput = "Total rides in selection: {:,d}".format(totalInSelection)
#
#     if (
#         datePicked is None
#         or selection is None
#         or len(selection) is 24
#         or len(selection) is 0
#     ):
#         return firstOutput, (datePicked, " - showing hour(s): All")
#
#     holder = sorted([int(x) for x in selection])
#
#     if holder == list(range(min(holder), max(holder) + 1)):
#         return (
#             firstOutput,
#             (
#                 datePicked,
#                 " - showing hour(s): ",
#                 holder[0],
#                 "-",
#                 holder[len(holder) - 1],
#             ),
#         )
#
#     holder_to_string = ", ".join(str(x) for x in holder)
#     return firstOutput, (datePicked, " - showing hour(s): ", holder_to_string)
#
#
# # Update Histogram Figure based on Month, Day and Times Chosen
# @app.callback(
#     Output("histogram", "figure"),
#     [Input("date-picker", "date"), Input("bar-selector", "value")],
# )
# def update_histogram(datePicked, selection):
#     date_picked = dt.strptime(datePicked, "%Y-%m-%d")
#     monthPicked = date_picked.month - 4
#     dayPicked = date_picked.day - 1
#
#     [xVal, yVal, colorVal] = get_selection(monthPicked, dayPicked, selection)
#
#     layout = go.Layout(
#         bargap=0.01,
#         bargroupgap=0,
#         barmode="group",
#         margin=go.layout.Margin(l=10, r=0, t=0, b=50),
#         showlegend=False,
#         plot_bgcolor="#323130",
#         paper_bgcolor="#323130",
#         dragmode="select",
#         font=dict(color="white"),
#         xaxis=dict(
#             range=[-0.5, 23.5],
#             showgrid=False,
#             nticks=25,
#             fixedrange=True,
#             ticksuffix=":00",
#         ),
#         yaxis=dict(
#             range=[0, max(yVal) + max(yVal) / 4],
#             showticklabels=False,
#             showgrid=False,
#             fixedrange=True,
#             rangemode="nonnegative",
#             zeroline=False,
#         ),
#         annotations=[
#             dict(
#                 x=xi,
#                 y=yi,
#                 text=str(yi),
#                 xanchor="center",
#                 yanchor="bottom",
#                 showarrow=False,
#                 font=dict(color="white"),
#             )
#             for xi, yi in zip(xVal, yVal)
#         ],
#     )
#
#     return go.Figure(
#         data=[
#             go.Bar(x=xVal, y=yVal, marker=dict(color=colorVal), hoverinfo="x"),
#             go.Scatter(
#                 opacity=0,
#                 x=xVal,
#                 y=yVal / 2,
#                 hoverinfo="none",
#                 mode="markers",
#                 marker=dict(color="rgb(66, 134, 244, 0)", symbol="square", size=40),
#                 visible=True,
#             ),
#         ],
#         layout=layout,
#     )
#
#
# # Get the Coordinates of the chosen months, dates and times
# def getLatLonColor(selectedData, month, day):
#     listCoords = totalList[month][day]
#
#     # No times selected, output all times for chosen month and date
#     if selectedData is None or len(selectedData) is 0:
#         return listCoords
#     listStr = "listCoords["
#     for time in selectedData:
#         if selectedData.index(time) is not len(selectedData) - 1:
#             listStr += "(totalList[month][day].index.hour==" + str(int(time)) + ") | "
#         else:
#             listStr += "(totalList[month][day].index.hour==" + str(int(time)) + ")]"
#     return eval(listStr)
#
#
# # Update Map Graph based on date-picker, selected data on histogram and location dropdown
# @app.callback(
#     Output("map-graph", "figure"),
#     [
#         Input("date-picker", "date"),
#         Input("bar-selector", "value"),
#         Input("location-dropdown", "value"),
#     ],
# )
# def update_graph(datePicked, selectedData, selectedLocation):
#     zoom = 12.0
#     latInitial = 40.7272
#     lonInitial = -73.991251
#     bearing = 0
#
#     if selectedLocation:
#         zoom = 15.0
#         latInitial = list_of_locations[selectedLocation]["lat"]
#         lonInitial = list_of_locations[selectedLocation]["lon"]
#
#     date_picked = dt.strptime(datePicked, "%Y-%m-%d")
#     monthPicked = date_picked.month - 4
#     dayPicked = date_picked.day - 1
#     listCoords = getLatLonColor(selectedData, monthPicked, dayPicked)
#
#     return go.Figure(
#         data=[
#             # Data for all rides based on date and time
#             Scattermapbox(
#                 lat=listCoords["Lat"],
#                 lon=listCoords["Lon"],
#                 mode="markers",
#                 hoverinfo="lat+lon+text",
#                 text=listCoords.index.hour,
#                 marker=dict(
#                     showscale=True,
#                     color=np.append(np.insert(listCoords.index.hour, 0, 0), 23),
#                     opacity=0.5,
#                     size=5,
#                     colorscale=[
#                         [0, "#F4EC15"],
#                         [0.04167, "#DAF017"],
#                         [0.0833, "#BBEC19"],
#                         [0.125, "#9DE81B"],
#                         [0.1667, "#80E41D"],
#                         [0.2083, "#66E01F"],
#                         [0.25, "#4CDC20"],
#                         [0.292, "#34D822"],
#                         [0.333, "#24D249"],
#                         [0.375, "#25D042"],
#                         [0.4167, "#26CC58"],
#                         [0.4583, "#28C86D"],
#                         [0.50, "#29C481"],
#                         [0.54167, "#2AC093"],
#                         [0.5833, "#2BBCA4"],
#                         [1.0, "#613099"],
#                     ],
#                     colorbar=dict(
#                         title="Time of<br>Day",
#                         x=0.93,
#                         xpad=0,
#                         nticks=24,
#                         tickfont=dict(color="#d8d8d8"),
#                         titlefont=dict(color="#d8d8d8"),
#                         thicknessmode="pixels",
#                     ),
#                 ),
#             ),
#             # Plot of important locations on the map
#             Scattermapbox(
#                 lat=[list_of_locations[i]["lat"] for i in list_of_locations],
#                 lon=[list_of_locations[i]["lon"] for i in list_of_locations],
#                 mode="markers",
#                 hoverinfo="text",
#                 text=[i for i in list_of_locations],
#                 marker=dict(size=8, color="#ffa0a0"),
#             ),
#         ],
#         layout=Layout(
#             autosize=True,
#             margin=go.layout.Margin(l=0, r=35, t=0, b=0),
#             showlegend=False,
#             mapbox=dict(
#                 accesstoken=mapbox_access_token,
#                 center=dict(lat=latInitial, lon=lonInitial),  # 40.7272  # -73.991251
#                 style="dark",
#                 bearing=bearing,
#                 zoom=zoom,
#             ),
#             updatemenus=[
#                 dict(
#                     buttons=(
#                         [
#                             dict(
#                                 args=[
#                                     {
#                                         "mapbox.zoom": 12,
#                                         "mapbox.center.lon": "-73.991251",
#                                         "mapbox.center.lat": "40.7272",
#                                         "mapbox.bearing": 0,
#                                         "mapbox.style": "dark",
#                                     }
#                                 ],
#                                 label="Reset Zoom",
#                                 method="relayout",
#                             )
#                         ]
#                     ),
#                     direction="left",
#                     pad={"r": 0, "t": 0, "b": 0, "l": 0},
#                     showactive=False,
#                     type="buttons",
#                     x=0.45,
#                     y=0.02,
#                     xanchor="left",
#                     yanchor="bottom",
#                     bgcolor="#323130",
#                     borderwidth=1,
#                     bordercolor="#6d6d6d",
#                     font=dict(color="#FFFFFF"),
#                 )
#             ],
#         ),
#     )


if __name__ == "__main__":
    app.run_server()