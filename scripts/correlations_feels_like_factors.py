import statsmodels.api as sm
from analysis_feels_like_factors import cold_df
from analysis_feels_like_factors import mid_df

print("(Cold) Wind vs Feels-Like: ", cold_df["wind_speed"].corr(cold_df["temperature_difference"]))
print("(Cold) Humidity vs Feels-Like: ", cold_df["humidity"].corr(cold_df["temperature_difference"]))
print()
print("(Mid) Wind vs Feels-Like: ", mid_df["wind_speed"].corr(mid_df["temperature_difference"]))
print("(Mid) Humidity vs Feels-Like: ", mid_df["humidity"].corr(mid_df["temperature_difference"]))