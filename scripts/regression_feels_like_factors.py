import statsmodels.api as sm
from analysis_feels_like_factors import cold_df
from analysis_feels_like_factors import mid_df


y_cold = cold_df["temperature_difference"]
x_cold = cold_df[["humidity", "wind_speed"]]
x_cold = sm.add_constant(x_cold)

model_cold = sm.OLS(y_cold, x_cold)
results_cold = model_cold.fit()
print("COLD RESULTS:")
print()
print(results_cold.summary())
print(results_cold.params)



y_mid = mid_df["temperature_difference"]
x_mid = mid_df[["humidity", "wind_speed"]]
x_mid = sm.add_constant(x_mid)

model_mid = sm.OLS(y_mid, x_mid)
results_mid = model_mid.fit()
print("MID RESULTS:")
print()
print(results_mid.summary())
print(results_mid.params)

print("The correlation: ", mid_df["wind_speed"].corr(mid_df["temperature_difference"]))