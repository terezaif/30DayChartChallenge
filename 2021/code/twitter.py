# %%

consumer_key = "idBfc3mYzrfBPxRM1z5AhXxAA"
consumer_secret = "K50925I1FObqf6LA8MwiUyCBWlOxtrXXpi0aUAFD0wNCFBPQ3j"
access_token = "1245495541330579457-6EBT7O9j98LgAt3dXxzsTK5FFAA2Lg"
access_secret = "jUP2N1nHeC6nzD30F4forjx7WxoOI603b4CqHdUnA6wqL"


# %%
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

# %%
api = tweepy.API(auth)
# %%

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
# %%
api.me().screen_name
# %%
