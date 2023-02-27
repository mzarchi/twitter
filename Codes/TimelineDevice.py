import config as cf
import tweepy

api = cf.api()

username = "1500tasvir"
for tweet in tweepy.Cursor(api.user_timeline, screen_name=username).items(10000):
    if hasattr(tweet, "retweeted_status"):
        print(f"{username} RT {tweet.retweeted_status.id}, device {tweet.source}")
    else:
        print(f"{username} TW {tweet.id}, device {tweet.source}")
