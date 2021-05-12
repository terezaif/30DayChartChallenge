# %%
import pandas as pd
import numpy as np
from skyfield.api import load

# %%
ts = load.timescale()
t = ts.now()
# %%
planets = load("de440.bsp")  # load('de421.bsp')
earth, moon = planets["earth"], planets["moon"]
# %%

astrometric = earth.at(t).observe(moon)
ra, dec, distance = astrometric.radec()
# %%
print(ra)
print(dec)
print(distance)

#%%


planets = load("de441.bsp")


# %%
ra, dec, dist = earth.at(years).observe(mars).radec()

# %%
earth, moon = planets["earth"], planets["moon"]

# %%
yearsall = ts.utc(range(1970, 17191))
# yearsall = ts.utc(range(1550, 2650))
# year2020 = ts.utc(2020, day =range(1, 13))
# year = ts.utc(2000, range(1, 13))
# %%
ra, dec, dist = earth.at(yearsall).observe(moon).radec()

# %%
# years100  = [y for i,y in enumerate(yearsall) if i%101 ==0]
# year_data = []

# ra, dec, dist = earth.at(yearsall).observe(moon).radec()
for dt_i, dist_i in zip(yearsall, dist.au):
    yd = {}
    yd["date"] = dt_i.utc_strftime("%Y-%m-%d")
    # yd["year"]=y
    yd["distance"] = dist_i
    year_data.append(yd)

#%%
yearall_df = pd.DataFrame.from_dict(year_data)


#%%
ra, dec, dist = earth.at(yearsall).observe(moon).radec()
# %%
year2020 = ts.utc(2020, day=range(1, 365))
year2000 = ts.utc(2000, day=range(1, 365))
year1980 = ts.utc(1980, day=range(1, 365))

# %%
ra, dec, dist = earth.at(year2020).observe(mars).radec()

# %%
year_data = []

years = [1980, 2000, 2020]
for y in years:
    yeary = ts.utc(y, day=range(1, 365))
    ra, dec, dist = earth.at(yeary).observe(moon).radec()
    for dt_i, dist_i in zip(yeary, dist.au):
        yd = {}
        yd["date"] = dt_i.utc_strftime("%Y-%m-%d")
        yd["year"] = y
        yd["distance"] = dist_i
        year_data.append(yd)

# %%
year_df = pd.DataFrame.from_dict(year_data)

#%%
yearall_df.describe()
first = yearall_df.iloc[0]["distance"]

yearall_df["diff_km"] = round(
    (yearall_df["distance"] - first) * 1.495978707 * pow(10, 8)
)

#%%
yearall_df.describe()
yearall_df[["date", "diff_km"]].to_csv("earth_moon_yearly_441.csv", index=False)

# %%
mean = year_df["distance"].mean()
# %%
year_df["diff_km"] = round((year_df["distance"] - mean) * 1.495978707 * pow(10, 8))
# %%
year_df[year_df.year == 2000][["date", "diff_km"]].to_csv(
    "earth_moon_2000.csv", index=False
)
year_df[year_df.year == 2020][["date", "diff_km"]].to_csv(
    "earth_moon_2020.csv", index=False
)
year_df[year_df.year == 1980][["date", "diff_km"]].to_csv(
    "earth_moon_1980.csv", index=False
)

# %%
round(mean * 1.495978707 * pow(10, 8))
# %%
import math

math.sqrt(30442)
# %%
