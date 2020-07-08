import plotly.express as px
import pandas as pd


df = pd.read_csv("austpop.csv")

# Line Graphs
fig = px.line(df, x="year", y="Aust", title="Australian Population")
#fig.show()

#
fig = px.line(
    df, 
    x="year", 
    y=["NSW","Vic","Qld","SA","WA","Tas","NT","ACT"],
    title="Australian Populaton by State"
)
#fig.show()

# Line ### potentially use for project??????
df_a = {
    "our_data": [123, 132, 654, 345, 125, 498],
    "more_data": [345, 67, 176, 245, 197, 391],
    "columns": ["a", "b", "c", "d", "e", "f"]
}
fig = px.line(df_a, y="our_data", x="columns")
#fig.show()


# Scatterplots
fig = px.scatter(
    df,
    x=["NSW","Vic","Qld","SA","WA","Tas","NT","ACT"],
    y="year"
)
#fig.show()

# Barchart
fig = px.bar(df, x="year", y=["NSW"])
fig.show()

fig = px.bar(
    df,
    x="year",
    y=["NSW","Vic","Qld","SA","WA","Tas","NT","ACT"],
    barmode="group"
)
#fig.show()
