import pandas as pd

from src.graph import build_graph
from src.dijkstra import dijkstra
from src.visualization import draw_graph

roads = pd.read_csv("data/roads.csv")

start = "A"
end = "L"

time = 8
weather = "Rain"

G = build_graph(
    roads,
    time,
    weather
)

path, cost = dijkstra(
    G,
    start,
    end
)

print("Shortest Path:", path)
print("Travel Time:", cost)

draw_graph(
    G,
    path,
    cost
)