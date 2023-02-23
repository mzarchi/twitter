# rename file to config.py
import tweepy


def api():
    cf = {
        "key": "*****",
        "kse": "*****",
        "tok": "*****",
        "tse": "*****"
    }

    auth = tweepy.OAuthHandler(cf["key"], cf["kse"])
    auth.set_access_token(cf["tok"], cf["tse"])
    return tweepy.API(auth, wait_on_rate_limit=True)
