#%%
import pandas as pd
import numpy as np

data = pd.read_csv("../data/ColonialTransformationData.tab", sep="\t")
# %%
data.head()
# %%
data["colpower"].unique()
# %%
data[data["colpower"] == "x"]
# %%
data.info()
# %%
# DOMFORM: how direct colonial rule
# VIOLRES: how violent
# TRADEPOL: the trade policy strength/control

data.describe()
# %%
data.sort_values(by=["COLYEARS"])

# %%
def percentile(n):
    def percentile_(x):
        return np.percentile(x, n)

    percentile_.__name__ = "percentile_%s" % n
    return percentile_


# %%

aggr2 = data.groupby("colpower").agg(medianVIOLTOT=("VIOLTOT", "median")).reset_index()
aggr2
# %%
# aggr = (
#    data.groupby("colpower")["COLYEARS"]
#    .agg([np.median, np.max, np.min, percentile(25), percentile(75), np.size, np.sum])
#    .reset_index()
# )
aggr = (
    data.groupby("colpower")
    .agg(
        max=("COLYEARS", "max"),
        min=("COLYEARS", "min"),
        mean=("COLYEARS", "mean"),
        std=("COLYEARS", "std"),
        size=("COLYEARS", "count"),
        medianVIOLTOT=("VIOLTOT", "median"),
    )
    .reset_index()
)


# %%
# aggr.join(aggr2.set_index("colpower"), on="colpower").sort_values(
#    by=["size", "median"], ascending=False
# ).to_csv("../datasets/colonialism.csv", index=False)
# %%
aggr["mean_wo"] = aggr["mean"] - aggr["std"]
aggr["mean_w"] = aggr["mean"] + aggr["std"]
aggr.sort_values(by=["size", "mean"], ascending=False).to_csv(
    "../datasets/colonialism.csv", index=False
)
# %%

# %%
aggr
# %%
data["COLONSET"].min()
# %%
