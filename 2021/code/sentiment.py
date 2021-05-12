# %%
from transformers import pipeline

# %%
with open("../data/abba/moneymoneymoney.txt", "r") as file:
    data = file.read().replace("\n", " ")
# %%
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained(
    "rohanrajpal/bert-base-codemixed-uncased-sentiment"
)

model = AutoModelForSequenceClassification.from_pretrained(
    "rohanrajpal/bert-base-codemixed-uncased-sentiment"
)
# %%
sentiment_analysis = pipeline(
    "sentiment-analysis", model="rohanrajpal/bert-base-codemixed-uncased-sentiment"
)
# %%
result = sentiment_analysis(data)[0]
print("Label:", result["label"])
print("Confidence Score:", result["score"])
print()
# %%

# %%
result = sentiment_analysis(data, return_all_scores=True, binary_output=True)
# %%
result
# %%
