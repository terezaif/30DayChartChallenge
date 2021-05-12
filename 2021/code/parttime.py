#%%
import pandas as pd
import numpy as np

data = pd.read_csv("../data/30daychart-parttime_15_64.csv")


dw = pd.melt(
    data, id_vars=["sex", "n_child", "geo"], var_name="year", value_name="percent"
)
dw["percent"] = dw["percent"].astype(float)
dw["year"] = dw["year"].astype(int)


# per sex/child/year count/avg/std for non na
aggr = (
    dw.groupby(["sex", "n_child", "year"])
    .agg(mean=("percent", "mean"), std=("percent", "std"), count=("percent", "count"))
    .reset_index()
)
aggr.head()
aggr["ci_95"] = 1.96 * aggr["std"] / np.sqrt(aggr["count"])
aggr["low"] = aggr["mean"] - aggr["ci_95"]
aggr["high"] = aggr["mean"] + aggr["ci_95"]

#%%
aggr.head()
#%%
from scipy.stats import linregress

trended = pd.DataFrame()

for s in ["F", "M"]:
    for c in [0, 1, 2]:
        series = aggr[(aggr.sex == s) & (aggr.n_child == c)]
        x = series["year"]
        y = series["mean"]
        slope, intercept, r_value, p_value, std_err = linregress(x, y)
        print("gender: %s, ch: %d" % (s, c))
        print("slope: %f, intercept: %f" % (slope, intercept))
        print("R-squared: %f" % r_value ** 2)
        series["trend"] = intercept + slope * series["year"]
        trended = pd.concat([trended, series])
# %%
trended[["sex", "n_child", "year", "low", "mean", "high", "trend"]].to_csv(
    "../datasets/europe_parttime_trend_15_64.csv", index=False
)
# %%
intercept_f_0 = 649.615753
slope_f_0 = -0.314216
intercept_m_0 = 234.898313
slope_m_0 = -0.112440

print(intercept_f_0 + slope_f_0 * 2041)
print(intercept_m_0 + slope_m_0 * 2075)
# %%
trended
# %%
intercept_f_2 = 584.586252
slope_f_2 = -0.277102
intercept_m_2 = 159.483599
slope_m_2 = -0.076857

print(intercept_f_2 + slope_f_2 * 2091)
print(intercept_m_2 + slope_m_2 * 2075)
# %%

dw["geo"].unique()
# %%
