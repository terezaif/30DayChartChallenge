# %%
import pandas as pd
import numpy as np

# %%
data = pd.read_json("dataset/book1-100k.json")
data = pd.concat([data, pd.read_json("dataset/book100k-200k.json")], ignore_index=True)
data = pd.concat([data, pd.read_json("dataset/book200k-300k.json")], ignore_index=True)
data = pd.concat([data, pd.read_json("dataset/book300k-400k.json")], ignore_index=True)
# %%
data.head()
# %%
data.shape
# %%
stats = data[data["Name"].str.contains("statistics|Statistics")]
# %%
stats.shape

# %%
stats[
    ["Name", "CountsOfReview", "PublishYear", "pagesNumber", "Authors", "Rating"]
].to_csv("statistics_books.csv")
stats["pageRating"] = (1 + stats["Rating"]) * np.log(stats["pagesNumber"])
stats["Rating1"] = 1 + stats["Rating"]


# %%
statscv = stats.groupby("Authors")["pagesNumber", "Rating1"].sum()
# %%


interim = stats.groupby(["Authors"], as_index=False).agg(
    {"Name": " ".join, "pagesNumber": np.sum, "Rating1": np.mean}
)
interim["Rating1"] = np.round(interim["Rating1"])
interim.head()

interim.to_csv("authors_pages_rating_books.csv", index=False)
# %%
interim.head()

# %%
