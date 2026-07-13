from src.predictor import predict_speed
import networkx as nx


def build_graph(roads, time, weather):

    G = nx.from_pandas_edgelist(
        roads,
        source="source",
        target="destination",
        edge_attr=True
    )

    for u, v, data in G.edges(data=True):

        predicted_speed = predict_speed(
            distance=data["distance"],
            road_type=data["road_type"],
            time=time,
            weather=weather
        )

        data["travel_time"] = data["distance"] / predicted_speed

    return G