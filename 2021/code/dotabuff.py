import requests
import json
import pandas as pd

r = requests.get(
    "https://api.opendota.com/api/players/113916764/matches?win=1&date=365&hero_id=5"
)
wins = json.loads(r.text)

df_wins = pd.DataFrame(wins)
df_wins["win"] = 1
df_wins.shape

r = requests.get(
    "https://api.opendota.com/api/players/113916764/matches?win=0&date=365&hero_id=5"
)
loss = json.loads(r.text)

df_loss = pd.DataFrame(loss)
df_loss["win"] = 0


games = pd.concat([df_wins, df_loss])

games.tail()
print(games.shape)

from datetime import datetime

games["start_time"] = [datetime.fromtimestamp(x) for x in games["start_time"]]
games["date"] = games["start_time"].dt.date
games["hour"] = games["start_time"].dt.hour
games["month"] = games["start_time"].dt.month
games["dow"] = games["start_time"].dt.dayofweek
games.info()

winrate_dow = games.groupby("dow").agg({"win": sum, "match_id": "count"}).reset_index()

winrate_dow["winrate"] = winrate_dow["win"] / winrate_dow["match_id"]
winrate_dow

winrate_h = games.groupby("hour").agg({"win": sum, "match_id": "count"}).reset_index()
winrate_h["winrate"] = winrate_h["win"] / winrate_h["match_id"]
winrate_h.to_csv("winrate_h.csv")


winrate_m = games.groupby("month").agg({"win": sum, "match_id": "count"}).reset_index()
winrate_m["winrate"] = winrate_m["win"] / winrate_m["match_id"]
winrate_m.to_csv("winrate_m.csv")

df_loss.shape
games.head()

games.shape

# getting all heros .. cm is 5
# r = requests.get('https://api.opendota.com/api/heroes')
# heroes = json.loads(r.text)
# df = pd.DataFrame(heroes)
# df


r = requests.get(
    "https://api.opendota.com/api/players/113916764/matches?win=0&game_mode=22"
)
loss = json.loads(r.text)

df_loss = pd.DataFrame(loss)
df_loss["win"] = 0

r = requests.get(
    "https://api.opendota.com/api/players/113916764/matches?win=1&game_mode=22"
)
wins = json.loads(r.text)

df_wins = pd.DataFrame(wins)
df_wins["win"] = 1

games = pd.concat([df_wins, df_loss])

games.tail()
print(games.shape)

from datetime import datetime

games["start_time"] = [datetime.fromtimestamp(x) for x in games["start_time"]]
games["date"] = games["start_time"].dt.date
games["year"] = games["start_time"].dt.year
games["hour"] = games["start_time"].dt.hour
games["month"] = games["start_time"].dt.month
games["dow"] = games["start_time"].dt.dayofweek
games.info()

games["duration"] = round(games["duration"] / 60)


winrate_d = games.groupby("date").agg({"win": sum, "match_id": "count"}).reset_index()
winrate_d["winrate"] = winrate_d["win"] / winrate_d["match_id"]
winrate_d
winrate_d.to_csv("winrate_d.csv", index=False)


games = games[games["year"] >= 2018]
min_date = games["date"].min()
min_date

games["days_count"] = (games["date"] - min_date).dt.days


games_y = games[["year", "duration", "days_count", "win"]]

games_y.to_csv("games_y_d.csv", index=False)

games[["date", "duration", "win"]]
