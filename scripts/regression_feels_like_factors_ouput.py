import pandas as pd


data = [
    {"temp_range": "cold", "variable": "wind_speed", "coefficient": -0.49, "significant": "yes"},
    {"temp_range": "cold", "variable": "humidity", "coefficient": 0.01, "significant": "no"},
    {"temp_range": "mid", "variable": "humidity", "coefficient": 0.05, "significant": "yes"},
    {"temp_range": "mid", "variable": "wind_speed", "coefficient": 0.01, "significant": "no"},
]

df = pd.DataFrame(data)
df.to_csv("data/regression_summary.csv", index=False)