#%%
import datetime
from astral.sun import sun
from astral import LocationInfo
import pandas as pd


def get_minutes(d):
    return d.hour * 60 + d.minute


city_name = "Hamburg"

city = LocationInfo("Hamburg", "Germany", "Europe/Berlin", 53.551086, 9.993682)
d1 = datetime.date(2020, 1, 1)
d2 = datetime.date(2020, 12, 31)
days = [d1 + datetime.timedelta(days=x) for x in range((d2 - d1).days + 1)]
len(days)
sunset = []
for day in days:
    s = sun(city.observer, date=day, tzinfo=city.timezone)

    entry = {}
    max = 24 * 60
    entry["date"] = day
    entry["dawn"] = get_minutes(s["dawn"])
    entry["sunrise"] = get_minutes(s["sunrise"]) - get_minutes(s["dawn"])
    entry["noon"] = get_minutes(s["noon"]) - get_minutes(s["sunrise"])
    entry["sunset"] = get_minutes(s["sunset"]) - get_minutes(s["noon"])
    entry["dusk"] = get_minutes(s["dusk"]) - get_minutes(s["sunset"])
    entry["eod"] = max - get_minutes(s["dusk"])

    sunset.append(entry)

    # print(day.strftime('%Y%m%d'))
df = pd.DataFrame.from_dict(sunset)

df.to_csv(f"datasets/sunrise_{city_name}.csv", index=False)

print(df.head())
print("Exported dataframe")
# %%
