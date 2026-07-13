import streamlit as st
from src.graph import build_graph
import pandas as pd
from src.dijkstra import dijkstra
from src.visualization import draw_graph

roads = pd.read_csv("data/roads.csv")

nodes = sorted(
    set(roads["source"]).union(
        set(roads["destination"])
    )
)



st.set_page_config(page_title="SmartRoute",page_icon="🚗")

st.title("🚗RouteFinder")

st.markdown("Traffic Route Optimization")

start = st.selectbox(
    "Select Location",
    nodes
)

end = st.selectbox(
    "Select Destination",
    nodes
)

time=st.slider(
    "Hour of Day",0,23,8
)

weather=st.selectbox(
    "Weather",["Sunny","Cloudy","Rain"]
)

if st.button("Find Best Route🚀",   use_container_width=True):
    if start==end:
        st.error("start and destination cannot be same!")
    else:
        G=build_graph(
            roads,time,weather
        )
        path,cost=dijkstra(G,start,end)

        st.success("Route Found...")

        st.subheader("📍 Shortest Path")
        st.code(" → ".join(path))

        st.metric(
            "Estimated Travel Time:",f"{cost:.2f} hours"
            )
        st.divider()

        fig = draw_graph(G, path, cost)
        st.pyplot(fig)
        st.divider()