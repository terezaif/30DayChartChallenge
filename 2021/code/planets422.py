# −3000 to 3000

# https://iopscience.iop.org/article/10.3847/1538-3881/abd414

import pandas as pd
import numpy as np
from skyfield.api import load, load_file

ts = load.timescale()
t = ts.now()

planets = load_file("de422.bsp")

earth, moon = planets["earth"], planets["sun"]

astrometric = earth.at(t).observe(moon)

yearsall = ts.utc(range(-2999, 3000))

ra, dec, dist = earth.at(yearsall).observe(moon).radec()

year_data = []

for dt_i, dist_i in zip(yearsall, dist.au):
    yd = {}
    yd["date"] = dt_i.utc_strftime("%Y-%m-%d")
    yd["distance"] = dist_i
    year_data.append(yd)


yearall_df = pd.DataFrame.from_dict(year_data)

# first = yearall_df.iloc[0]["distance"]


# yearall_df["diff_km"]=(yearall_df["distance"] - first)*1.495978707*pow(10,8)

# yearall_df["diff"]=(yearall_df["distance"] - first)*1000

# print(yearall_df.describe())
yearall_df.describe()


yearall_df[["date", "distance"]].to_csv("earth_sun_yearly_422.csv", index=False)


years = ts.utc(range(0, 5))
years

astrometric = earth.at(years).observe(moon)
ra, dec, distance = astrometric.radec()
print(ra)
print(dec)
print(distance)


yearall_df["date"].max()
len(dist.au)
len(year_data)