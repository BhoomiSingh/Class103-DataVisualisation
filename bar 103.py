import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.bar(df, y="cases", color="country")
fig.show()
