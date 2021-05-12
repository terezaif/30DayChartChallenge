#%%
import pandas as pd
import numpy as np

df_male = pd.read_csv("../data/API_SE.ADT.LITR.MA.ZS_DS2_en_csv_v2_2252517.csv")
df_female = pd.read_csv("../data/API_SE.ADT.LITR.FE.ZS_DS2_en_csv_v2_2252514.csv")
# %%

# %%
df_female.columns
# %%


# %%
aggregate_cols = (df_female[df_female["2019"] > 0].iloc[:, 1]).tolist()
# %%

# (df_female[df_female["2019"] >0].iloc[:,1]).tolist()
exclude = [
    "ARB",
    "EAP",
    "EAR",
    "EAS",
    "ECA",
    "ECS",
    "FCS",
    "HPC",
    "IBD",
    "IBT",
    "IDB",
    "IDX",
    "LAC",
    "LCN",
    "LDC",
    "LIC",
    "LMC",
    "LMY",
    "LTE",
    "MEA",
    "MIC",
    "MNA",
    "OSS",
    "PRE",
    "SAS",
    "SSA",
    "SSF",
    "SST",
    "TEA",
    "TEC",
    "TLA",
    "TMN",
    "TSA",
    "TSS",
    "UMC",
    "WLD",
]

# %%

data_female = df_female[["CountryName", "CountryCode", "2018"]][
    (df_female["2018"] > 0) & (~df_female["CountryCode"].isin(exclude))
]

data_male = df_male[["CountryName", "CountryCode", "2018"]][
    (df_male["2018"] > 0) & (~df_male["CountryCode"].isin(exclude))
]
# %%
data_female.rename(columns={"2018": "percentage"}, inplace=True)
data_male.rename(columns={"2018": "percentage"}, inplace=True)

data_female.to_csv("../datasets/female_literacy_2018.csv", index=False)
data_male.to_csv("../datasets/male_literacy_2018.csv", index=False)
# %%
data_female["gender"] = "Female"
data_male["gender"] = "Male"
data = pd.concat([data_female, data_male])
data.to_csv("../datasets/literacy_2018.csv", index=False)
# %%
aggr = (
    data.groupby("gender")
    .agg(
        max=("percentage", "max"),
        min=("percentage", "min"),
        mean=("percentage", "mean"),
        std=("percentage", "std"),
        count=("percentage", "count"),
    )
    .reset_index()
)
aggr.head()
# %%

# %%
intervals = {
    "80": 1.282,
    "85": 1.440,
    "90": 1.645,
    "95": 1.960,
    "99": 2.576,
    "995": 2.807,
    "999": 3.291,
}

for key, z in intervals.items():
    aggr[f"ci_{key}"] = z * aggr["std"] / np.sqrt(aggr["count"])
# %%
aggr.to_csv("../datasets/literacy_ci_2018.csv", index=False)
# %%
aggr
# %%
