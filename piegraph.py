# imports
import zipfile as zp
import pandas as pd
import json
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.figure_factory as ff
import plotly.offline as pyo

# ------------------------------------------------- IMPORTING DATA -----------------------------------------------------

# Reading Airbnb df
df = pd.read_csv("./data/final_df.csv")

# # Reading GeoJSON
# with zp.ZipFile("./data/airbnb_data.zip") as myzip:
#     with myzip.open('neighbourhoods.geojson') as myfile:
#         neighborhoods = json.load(myfile)

# ------------------------------------------------- VISUALIZATIONS -----------------------------------------------------


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