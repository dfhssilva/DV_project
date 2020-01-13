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
fig = go.Figure(f)
fig.data[0].marker.line = dict(color='black', width=2)
fig.data[1].line.color = 'red'
fig.layout.sliders = [dict(
                active=4,
                currentvalue={"prefix": "bin size: "},
                pad={"t": 20},
                steps=[dict(label=i, method='restyle',  args=['xbins.size', i]) for i in range(1, 20)]
                )]
fig.update_layout(xaxis_title='Price ($)', yaxis_title='Relative frequencies', showlegend=False, title='Price distribution')
pyo.plot(fig)


fig = go.Figure()
fig.add_trace(go.Pie(labels=df['ordinal_rating'].value_counts().index, values=df['ordinal_rating'].value_counts().values))
fig.update_layout(title="Proportion of listing's rating")
pyo.plot(fig)