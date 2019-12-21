# imports
import zipfile as zp
import pandas as pd

# extracting data files
with zp.ZipFile("./data/airbnb_data.zip") as myzip:
    myzip.extractall("./data/")

# reading data files
df = pd.read_csv("./data./lisbon_0619_neighbourhoods.csv")

df.head()