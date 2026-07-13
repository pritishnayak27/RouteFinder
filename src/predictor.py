#predict speed

import joblib
import pandas as pd

model = joblib.load("models/decision_tree.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")
def predict_speed(distance, road_type, time, weather):

    row = {
        "time": time,
        "distance": distance,
        "weather": weather,
        "road_type": road_type
    }

    row = pd.DataFrame([row])

    row = pd.get_dummies(row)

    row = row.reindex(
        columns=feature_columns,
        fill_value=0
    )

    predicted_speed = model.predict(row)[0]

    return predicted_speed