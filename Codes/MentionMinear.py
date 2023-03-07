import config as cf
import tweepy

api = cf.api()

tweet_id = "1631968588306235393"
tweet_data = api.get_status(id=tweet_id)
print(f"Tweet-id: {tweet_id}, Author: {tweet_data.user.screen_name}")
repeat = False
counter = 1
repliesUserId = []

f = open(f"Mentions-{tweet_id}.txt", "a")
for tweet in tweepy.Cursor(
        api.search_tweets,
        q=f"conversation_id:{tweet_id} filter:replies to:{tweet_data.user.screen_name}",
        result_type="recent").items(100000):
    value = tweet.user.id
    name = tweet.user.screen_name
    # Check for duplicates user.id
    valueIs = value in repliesUserId
    if (valueIs and repeat) or not valueIs:
        repliesUserId.append(value)
        link = f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
        line = f"{counter}, Created: {tweet.created_at}, Link: {link}"
        f.write(line + "\n")
        print(line)
        counter += 1
f.close()
